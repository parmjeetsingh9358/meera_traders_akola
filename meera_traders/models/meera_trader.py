# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MeeraTraders(models.Model):
    _name = 'meera.traders'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Meera Traders'

    name = fields.Char(default=lambda self: _('New'))
    date = fields.Date('Date', default=lambda self: fields.datetime.now())
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done'),
        ],
        string='Status',
        tracking=True,
        default='draft',
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.user.company_id,
        string='Company'
    )
    # Dealer Details.
    dealer_id = fields.Many2one("meera.traders.customer", "Factory", tracking=True)
    dealer_mobile = fields.Char("Mobile", compute="_dealer_address")
    dealer_address = fields.Text("Address", compute="_dealer_address")

    # Seller Details.
    seller_id = fields.Many2one("meera.traders.customer", "Party", tracking=True)
    seller_mobile = fields.Char("Mobile", compute="_seller_address")
    seller_address = fields.Text("Address", compute="_seller_address")
    total_qty = fields.Float('Total quantity')
    total_amount = fields.Float('Amount', compute="_total_amount")
    note = fields.Text('Note')

    meera_trader_ids = fields.One2many('meera.traders.line', 'meera_trader_id', 'Meera Traders')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('meera.trader.sequence')
        return super(MeeraTraders, self).create(vals)

    def set_to_done(self):
        self.state = "done"

    def set_to_drat(self):
        self.state = "draft"

    @api.depends('meera_trader_ids',)
    def _total_amount(self):
        for record in self:
            rec = sum(line.total_commission_rate for line in record.meera_trader_ids)
            record.update({'total_amount': rec})

    @api.depends('dealer_id',)
    def _dealer_address(self):
        for rec in self:
            # Ensure each attribute is converted to string before concatenation
            street = str(rec.dealer_id.street) if rec.dealer_id.street else ""
            street2 = str(rec.dealer_id.street2)  if rec.dealer_id.street2 else ""
            city = str(rec.dealer_id.city) if rec.dealer_id.city else ""
            zip = str(rec.dealer_id.zip) if rec.dealer_id.zip else ""

            # Concatenate the strings
            rec.dealer_address = street + " " + street2 + " " + city + " " + zip
            rec.dealer_mobile = rec.dealer_id.mobile

    @api.depends('seller_id',)
    def _seller_address(self):
        for rec in self:
            # Ensure each attribute is converted to string before concatenation
            street = str(rec.seller_id.street) if rec.seller_id.street else ""
            street2 = str(rec.seller_id.street2) if rec.seller_id.street2 else ""
            city = str(rec.seller_id.city) if rec.seller_id.city else ""
            zip = str(rec.seller_id.zip) if rec.seller_id.zip else ""

            # Concatenate the strings
            rec.seller_address = street + " " + street2 + " " + city + " " + zip
            rec.seller_mobile = rec.seller_id.mobile


class MeeraTradersLine(models.Model):
    _name = 'meera.traders.line'
    _description = "Meera Traders Line"

    meera_trader_id = fields.Many2one('meera.traders', string='Meera Traders')
    product_id = fields.Many2one('meera.trader.product', string='Product')
    qty = fields.Float('Quantity')
    commission_rate = fields.Float('Rate')
    product_notes = fields.Text('Notes')
    total_commission_rate = fields.Float('Total Amount', compute="_total_commission_rate")

    @api.depends('qty', 'commission_rate')
    def _total_commission_rate(self):
        '''Method to compute Total Price'''
        for rec in self:
            rec.total_commission_rate = rec.qty * rec.commission_rate

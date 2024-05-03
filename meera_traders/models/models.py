# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MeeraTraders(models.Model):
    _name = 'meera.traders'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Meera Traders'

    name = fields.Char(default=lambda self: _('New'))
    partner_id = fields.Many2one("res.partner", tracking=True,)
    street = fields.Char("Street")
    street2 = fields.Char("Street2")
    city = fields.Char("City")
    state_id = fields.Many2one("res.country.state", "State")
    zip = fields.Char("Zip")
    country_id = fields.Many2one("res.country", "Country")
    mobile = fields.Text()
    email = fields.Char()
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('posted', 'Posted'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        tracking=True,
        default='draft',
    )
    meera_trader_ids = fields.One2many('meera.traders.line', 'meera_trader_id', 'Meera Traders')


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('meera.trader.sequence')
        return super(MeeraTraders, self).create(vals)


class MeeraTradersLine(models.Model):
    _name = 'meera.traders.line'
    _description = "Meera Traders Line"

    meera_trader_id = fields.Many2one('meera.traders', string='Meera Traders')
    product_id = fields.Char(string='Product')
    qty = fields.Float('Quantity')
    price = fields.Float('Price')
    commission_rate = fields.Float('Commission Price')
    total_commission_rate = fields.Float('Total Price')


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MeeraTradersCustomer(models.Model):
    _name = 'meera.traders.customer'
    _description = 'Meera Traders Customer'

    serial_no = fields.Char(default=lambda self: _('New'))
    name = fields.Char( tracking=True,)
    street = fields.Char("Street")
    street2 = fields.Char("Street2")
    city = fields.Char("City")
    state_id = fields.Many2one("res.country.state", "State")
    zip = fields.Char("Zip")
    country_id = fields.Many2one("res.country", "Country")
    mobile = fields.Char()
    customer_type = fields.Selection(
        selection=[
            ('seller', 'Party'),
            ('dealer', 'Factory'),
        ],
        string='Customer Type',
        tracking=True,
        default='seller',
    )

    @api.model
    def create(self, vals):
        vals['serial_no'] = self.env['ir.sequence'].next_by_code('meera.trader.customer.sequence')
        return super(MeeraTradersCustomer, self).create(vals)

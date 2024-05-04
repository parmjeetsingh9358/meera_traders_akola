# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MeeraTraderProduct(models.Model):
    _name = 'meera.trader.product'
    _description = 'Meera Trader Product'
    _rec_name = 'product_name'

    product_name = fields.Char()

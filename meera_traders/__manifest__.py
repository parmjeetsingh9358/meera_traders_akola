# -*- coding: utf-8 -*-
{
    'name': "Meera Traders Est.19996",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Parmjeet Singh",
    "license": "LGPL-3",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '16.0.0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/meera_trader.xml',
        'views/meera_trader_customer.xml',
        'views/meera_trader_product.xml',
        'report/meera_traders_report.xml',
        'report/menu.xml',

    ],
}




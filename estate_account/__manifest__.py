# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate Account',
    'author': 'SC BISSTECH SRL',
    'version': '17.0.0.1.0',
    'category': 'Accounting',
    'sequence': 10,
    'summary': '',
    'description': """
Real Estate Account
===================

Training Module
    """,
    'website': 'https://www.information-systems.ro',
    'depends': ['estate', 'account'],
    'data': [
        'report/estate_account_property_templates.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}

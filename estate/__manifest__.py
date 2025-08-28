# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate',
    'author': 'SC BISSTECH SRL',
    'version': '17.0.0.1.0',
    'category': 'Base',
    'sequence': 10,
    'summary': '',
    'description': """
Real Estate
===========

Training Module
    """,
    'website': 'https://www.information-systems.ro',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

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
        'views/res users_views.xml',
        'views/estate_menus.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}

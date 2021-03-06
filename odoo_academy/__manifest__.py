# -*- coding: utf-8 -*-.

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
    """,
    'author': 'Bisstech SRL',
    'category': 'Training',
    'version': '4.2',
    'depends': ['base', 'web_map', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/book_views.xml',
        'views/rental_views.xml',
        'views/library_web_templates.xml',
        'wizard/book_wizard_view.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

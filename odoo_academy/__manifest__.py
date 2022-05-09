# -*- coding: utf-8 -*-.

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'Bisstech SRL',
    'category': 'Training',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

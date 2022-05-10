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
    'version': '1.3',
    'depends': ['base'],
    'data': [
        # 'views/sale_order_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

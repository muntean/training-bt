# -*- coding: utf-8 -*-.

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
    """,
    'author': 'Bisstech SRL',
    'category': 'Training',
    'version': '1.5',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/book_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

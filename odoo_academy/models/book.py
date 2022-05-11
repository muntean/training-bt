# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Book(models.Model):
    _name = "academy.book"
    _description = "Book"

    name = fields.Char(string='Name')
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    # year = fields.Datetime(string='Date')
    year = fields.Char(string='Year')
    genre = fields.Selection(string='Genre', selection=[('scifi', 'Science Fiction'),
                                                        ('fantasy', 'Fantasy'),
                                                        ('romance', 'Romance'),
                                                        ('action', 'Action & Adventure'),
                                                        ('mystery', 'Mystery')
                                                        ])
    description = fields.Text(string='Description')
    is_rented = fields.Boolean(string='Is Rented', default=False)

# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


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
    isbm = fields.Char(string='ISBM', default=False)
    is_rented = fields.Boolean(string='Is Rented', default=False)
    rented_id = fields.Many2one('academy.rental')

    @api.onchange('isbm')
    def _check_isbm(self):
        if len(self.isbm) > 13:
            raise ValidationError(_('ISBM must contain maximum 13 numbers.'))

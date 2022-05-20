# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class BookCopy(models.Model):
    _name = "academy.book.copy"
    _description = "Book Copy"
    _inherits = {'academy.book': 'book_id'}

    book_id = fields.Many2one(comodel_name='academy.book', string='Book', ondelete='cascade')
    ref = fields.Char(string='Internal Reference')
    is_rented = fields.Boolean(string=_('Is Rented'), default=False)

    _sql_constraints = [
        ('ref_uniq', 'unique(ref)', "A reference can only be assigned to one book !"),
    ]

# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Rental(models.Model):
    _name = "academy.rental"
    _description = "Rental"

    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    # book_id = fields.Many2one(comodel_name='academy.book', string='Book', ondelete='cascade')
    book_ids = fields.Many2many(comodel_name='academy.book', inverse_name='rented_id', string='Books')
    name = fields.Char(string='Name')


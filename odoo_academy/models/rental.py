# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Rental(models.Model):
    _name = "academy.rental"
    _description = "Rental"

    partner_id = fields.Many2one('res.partner')
    book_ids = fields.One2many('academy.book', 'rented_id')

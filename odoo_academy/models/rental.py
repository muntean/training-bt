# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import timedelta


class Rental(models.Model):
    _name = "academy.rental"
    _description = "Rental"

    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    # book_id = fields.Many2one(comodel_name='academy.book', string='Book')
    book_ids = fields.Many2many(comodel_name='academy.book', inverse_name='rented_id', string='Books')
    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    duration = fields.Integer(string='Rent Duration', default=1)
    end_date = fields.Date(string='End Date', compute='_compute_end_date', inverse='_inverse_end_date', store=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.duration):
                rec.end_date = rec.start_date
            else:
                duration = timedelta(days=rec.duration)
                rec.end_date = rec.start_date + duration

    def _inverse_end_date(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.duration = (rec.end_date - rec. start_date).days + 1
            else:
                continue

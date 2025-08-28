# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='type_id', string='Properties')
    sequence = fields.Integer(string='Sequence', default=1)
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_type_id', string='Offers')
    offer_count = fields.Integer(string='Offer Count', compute='_compute_offer_count')

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'The name of a type must be unique.')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            if bool(rec.offer_ids):
                rec.offer_count = len(rec.offer_ids)
            else:
                rec.offer_count = 0



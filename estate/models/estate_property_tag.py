# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'The name of a tag must be unique.')
    ]


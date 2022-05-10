# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Spaceship(models.Model):
    _name = "academy.spaceship"
    _description = "Spaceship"

    name = fields.Char(string='Name')
    fuel_type = fields.Selection(string='Fuel Type', selection=[('lox', 'Liquid Oxygen'),
                                                                ('lhy', 'Liquid Hydrogen')])
    ship_type = fields.Selection(string='Ship Type', selection=[('carrier', 'Carrier'),
                                                                ('fighter', 'Fighter'),
                                                                ('destroyer', 'Destroyer')])
    passengers = fields.Integer(string='Passengers No')
    active = fields.Boolean(string='Active', default=True)

# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_is_zero

orientations = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
states = [('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Cancelled')]

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'
    _order = 'id desc'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', default=fields.Date.today() + relativedelta(months=3), copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(orientations, string='Garden Orientation')
    state = fields.Selection(states, string='Status', copy=False, required=True,default='new')
    active = fields.Boolean(string='Active', default=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Salesman', index=True, tracking=True,default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, tracking=True, copy=False)
    type_id = fields.Many2one('estate.property.type', string='Property Type', index=True)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')
    total_area = fields.Integer(string='Total Area', compute='_compute_total_area')
    best_price = fields.Float(string='Best Offer', compute='_compute_best_price')

    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be positive.'),
        ('positive_selling_price', 'CHECK(selling_price > 0)', 'The selling price must be positive.'),
    ]

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for rec in self:
            if not bool(rec.living_area) and not bool(rec.garden_area):
                rec.total_area = 0
            else:
                rec.total_area = rec.living_area + rec.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for rec in self:
            if bool(rec.offer_ids):
                rec.best_price = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_price = 0.0

    @api.onchange('garden')
    def onchange_garden(self):
        if bool(self.garden):
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False

    def action_sold(self):
        for rec in self:
            if rec.state == 'cancel':
                raise UserError(_('Properties on "Cancel" state can\'t be set as sold.'))
            rec.state = 'sold'

    def action_cancel(self):
        for rec in self:
            if rec.state == 'sold':
                raise UserError(_('Properties on "Sold" state can\'t be set as canceled.'))
            rec.state = 'cancel'

    @api.constrains('selling_price', 'expected_price')
    def check_selling_price(self):
        for rec in self:
            if not float_is_zero(rec.selling_price, precision_digits=6) and rec.selling_price < rec.expected_price * 0.9:
                raise ValidationError(_("Selling price must be 90% or more from expected price."))

    @api.ondelete(at_uninstall=False)
    def _unlink_active_property(self):
        if self.state not in ['new', 'cancel']:
            raise UserError("Can't delete an property in this state!")
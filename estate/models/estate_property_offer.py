# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

states = [('accepted', 'Accepted'), ('refused', 'Refused')]

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'
    _order = 'price desc'

    price = fields.Float(string='Price')
    state = fields.Selection(states, string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner',index=True, required=True)
    property_id = fields.Many2one('estate.property', string='Properties', index=True, required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline')
    property_type_id = fields.Many2one(related="property_id.type_id", string='Property Type', store=True)

    _sql_constraints = [
        ('positive_price', 'CHECK(price > 0)', 'The offer price must be positive.')
    ]

    @api.model_create_multi
    def create(self, vals):
        """
        Change property state to received when a offer is created
        :param vals:
        :return:
        """
        res_ids = super(EstatePropertyOffer, self).create(vals)
        for res in res_ids:
            if res.property_id.state not in ['received']:
                res.property_id.state = 'received'
        return res_ids

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        """
        Compute date_deadline field
        """
        for rec in self:
            if bool(rec.create_date) and bool(rec.validity):
                rec.date_deadline = rec.create_date + relativedelta(days=rec.validity)
            else:
                rec.date_deadline = False

    def action_accept(self):
        """
        Action accept change state to accepted
        """
        for rec in self:
            if rec.property_id.state == 'received':
                rec.state = 'accepted'
                rec.property_id.selling_price = rec.price
                rec.property_id.buyer_id = rec.partner_id
                rec.property_id.state = 'accepted'
                for offer in rec.property_id.offer_ids:
                    if not offer.id == rec.id:
                        offer.state = 'refused'
            else:
                raise UserError(_('Property not in Offer Received state.'))

    def action_refuse(self):
        """
        Action refuse change state to refuse
        """
        for rec in self:
            if rec.property_id.state == 'received':
                rec.state = 'refused'
            else:
                raise UserError(_('Property not in Offer Received state.'))


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class BookWizard(models.TransientModel):
    _name = 'library.book.wizard'
    _description = 'Book Wizard'

    book_id = fields.Many2one(comodel_name='academy.book', string='Books')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    rental_ids = fields.Many2many(comodel_name='academy.rental', readonly=True)

    def action_search(self):
        self.rental_ids = self.env['academy.rental'].search([('partner_id', '=', self.partner_id.id)])
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new'
        }

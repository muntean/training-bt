# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.fields import Command


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        """
        Override action for sold property button to create an invoice to partner
        :return: True
        """
        invoice_vals_list = []
        invoice_line_vals = []
        for rec in self:
            invoice_vals = rec._prepare_invoice()
            main_invoice_line = Command.create(rec._prepare_invoice_line())
            invoice_line_vals.append(main_invoice_line)
            aditional_taxes = Command.create({
                'display_type': 'product',
                'name': 'Aditional Taxes',
                'quantity': 1,
                'price_unit': self.selling_price * 0.06,
            })
            invoice_line_vals.append(aditional_taxes)
            administrative_fees = Command.create({
                'display_type': 'product',
                'name': 'Administrative Fees',
                'quantity': 1,
                'price_unit': 100.00,
            })
            invoice_line_vals.append(administrative_fees)
            invoice_vals['invoice_line_ids'] += invoice_line_vals
            invoice_vals_list.append(invoice_vals)
        moves = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals_list)
        return super(EstateProperty, self).action_sold()

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice.
        """
        self.ensure_one()
        values = {
            'ref': '',
            'move_type': 'out_invoice',
            'currency_id': self.user_id.company_id.currency_id.id,
            'partner_id': self.buyer_id.id,
            'invoice_origin': self.name,
            'invoice_line_ids': [],
            'user_id': self.user_id.id,
        }
        return values

    def _prepare_invoice_line(self):
        """
        Prepare the dict of values to create the new invoice line.
        """
        self.ensure_one()
        product_id = self.env['product.product'].search([('default_code', '=', 'estate')])
        res = {
            'display_type': 'product',
            'name': self.name,
            'product_id': product_id.id,
            'quantity': 1,
            'price_unit': self.selling_price,
            'tax_ids': self.user_id.company_id.account_purchase_tax_id.ids,
        }
        return res
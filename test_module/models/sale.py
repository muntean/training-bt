from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    work_test = fields.Boolean('Test Field', default=False)

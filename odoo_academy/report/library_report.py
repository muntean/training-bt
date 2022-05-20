from odoo import api, models, fields, _
import datetime


class LibraryReport(models.AbstractModel):
    _name = 'report.odoo_academy.library_report'
    _description = 'Library Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('create_date', '>=', data['form']['date_start']),
                  ('create_date', '<=', data['form']['date_end']),
                  '|',
                  ('active', '=', True),
                  ('active', '=', False)]

        report_name = 'mrp_portal_form.mrp_portal_production_report'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        report.name = _('Production Report - %s - %s' % (data['form']['date_start'], data['form']['date_end']))

        mrp_production_ids = self.env['mrp.production.portal'].search(domain)
        language = self.env['res.lang'].search([("code", "=", self.env.user.lang)])
        report_date = fields.Datetime.context_timestamp(self, datetime.datetime.now()).strftime(language.date_format)
        return {
            'report_data': mrp_production_ids,
            'totals': self._get_totals_report(mrp_production_ids),
            'report_date': report_date,
        }
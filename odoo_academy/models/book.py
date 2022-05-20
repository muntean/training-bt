# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Book(models.Model):
    _name = "academy.book"
    _description = "Book"
    _order = "name"

    name = fields.Char(string=_('Name'))
    author = fields.Char(string=_('Author'))
    publisher = fields.Char(string=_('Publisher'))
    year = fields.Char(string=_('Year'))
    genre = fields.Selection(string=_('Genre'), selection=[('scifi', _('Science Fiction')),
                                                           ('fantasy', _('Fantasy')),
                                                           ('romance', _('Romance')),
                                                           ('action', _('Action & Adventure')),
                                                           ('mystery', _('Mystery'))
                                                           ])
    description = fields.Text(string=_('Description'))
    isbm = fields.Char(string=_('ISBM'))

    @api.onchange('isbm')
    def _check_isbm(self):
        if bool(self.isbm) and len(self.isbm) > 13:
            raise ValidationError(_('ISBM must contain maximum 13 numbers.'))

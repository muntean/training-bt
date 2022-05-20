# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Library(http.Controller):
    @http.route('/library/', auth='public', website=True)
    def index(self, **kw):
        vals = {}
        return request.render('odoo_academy.library_website_index', vals)

    @http.route('/library/books', auth='public', website=True)
    def books(self, **kw):
        vals = {}
        book_ids = http.request.env['academy.book'].sudo().search([])
        vals.update({'books': book_ids})
        return request.render('odoo_academy.library_website', vals)

# -*- coding: utf-8 -*-
from odoo import http

# class ExtraAddons/library(http.Controller):
#     @http.route('/extra_addons/library/extra_addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra_addons/library/extra_addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra_addons/library.listing', {
#             'root': '/extra_addons/library/extra_addons/library',
#             'objects': http.request.env['extra_addons/library.extra_addons/library'].search([]),
#         })

#     @http.route('/extra_addons/library/extra_addons/library/objects/<model("extra_addons/library.extra_addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra_addons/library.object', {
#             'object': obj
#         })
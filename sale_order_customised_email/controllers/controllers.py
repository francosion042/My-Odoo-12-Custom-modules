# -*- coding: utf-8 -*-
from odoo import http

# class SaleOrderCustomisedEmail(http.Controller):
#     @http.route('/sale_order_customised_email/sale_order_customised_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_customised_email/sale_order_customised_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_customised_email.listing', {
#             'root': '/sale_order_customised_email/sale_order_customised_email',
#             'objects': http.request.env['sale_order_customised_email.sale_order_customised_email'].search([]),
#         })

#     @http.route('/sale_order_customised_email/sale_order_customised_email/objects/<model("sale_order_customised_email.sale_order_customised_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_customised_email.object', {
#             'object': obj
#         })
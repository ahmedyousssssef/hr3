# -*- coding: utf-8 -*-
from openerp import http

# class HrCustomiz(http.Controller):
#     @http.route('/hr_customiz/hr_customiz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_customiz/hr_customiz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_customiz.listing', {
#             'root': '/hr_customiz/hr_customiz',
#             'objects': http.request.env['hr_customiz.hr_customiz'].search([]),
#         })

#     @http.route('/hr_customiz/hr_customiz/objects/<model("hr_customiz.hr_customiz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_customiz.object', {
#             'object': obj
#         })
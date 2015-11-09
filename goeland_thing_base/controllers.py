# -*- coding: utf-8 -*-
from openerp import http

# class GoelandThingBase(http.Controller):
#     @http.route('/goeland_thing_base/goeland_thing_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/goeland_thing_base/goeland_thing_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('goeland_thing_base.listing', {
#             'root': '/goeland_thing_base/goeland_thing_base',
#             'objects': http.request.env['goeland_thing_base.goeland_thing_base'].search([]),
#         })

#     @http.route('/goeland_thing_base/goeland_thing_base/objects/<model("goeland_thing_base.goeland_thing_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('goeland_thing_base.object', {
#             'object': obj
#         })
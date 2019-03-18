# -*- coding: utf-8 -*-
from odoo import http

# class Hello-world(http.Controller):
#     @http.route('/hello-world/hello-world/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hello-world/hello-world/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hello-world.listing', {
#             'root': '/hello-world/hello-world',
#             'objects': http.request.env['hello-world.hello-world'].search([]),
#         })

#     @http.route('/hello-world/hello-world/objects/<model("hello-world.hello-world"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hello-world.object', {
#             'object': obj
#         })
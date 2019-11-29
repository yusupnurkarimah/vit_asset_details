# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetDetails(http.Controller):
#     @http.route('/vit_asset_details/vit_asset_details/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_asset_details/vit_asset_details/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_asset_details.listing', {
#             'root': '/vit_asset_details/vit_asset_details',
#             'objects': http.request.env['vit_asset_details.vit_asset_details'].search([]),
#         })

#     @http.route('/vit_asset_details/vit_asset_details/objects/<model("vit_asset_details.vit_asset_details"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_asset_details.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons.base_geoengine import geo_model, fields


class GoelandThingBase(geo_model.GeoModel):
    _name = 'goeland.thingbase'
    name = fields.Char()
    geo_point = fields.GeoPoint(
        'Addresses coordinate', related='partner_id.geo_point')

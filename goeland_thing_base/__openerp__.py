# -*- coding: utf-8 -*-
{
    'name': "Goeland Thing Base Class",

    'summary': """
        goeland_thing_base is the base class for goeland objects,
        here we are talking about objects of real life like a building""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ville de Lausanne - TRX - SCC",
    'website': "http://www.lausanne.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'goeland',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                 'geoengine_partner',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
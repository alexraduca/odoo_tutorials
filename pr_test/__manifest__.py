# -*- coding: utf-8 -*-
{
    'name': 'PR Test',
    'author': 'PRConsulting',
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tags_views.xml',
        'views/estate_property_offer_views.xml',
        'views/users_views.xml',
        'views/customers_views.xml',
        'views/estate_menus.xml',
    ],
    'depends': ['base'],
    'license': 'LGPL-3'
}

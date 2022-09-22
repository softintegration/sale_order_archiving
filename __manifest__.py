# -*- coding: utf-8 -*-

{
    'name': 'Sale order archiving',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'summary': 'Sale order archiving',
    'description': "",
    'depends': [
        'sale'
    ],
    'data': [
        'security/sale_order_archiving_security.xml',
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

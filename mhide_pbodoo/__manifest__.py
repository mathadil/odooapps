# -*- coding: utf-8 -*-
{
    'name': ' Hide Powered By Odoo',
    'version': '0.1',
    'summary': 'Hide Powered By Odoo',
    'sequence': -100,
    'description': """
        Hide Powered By Odoo""", 
    'author': "ADIL",
    'website': "#",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


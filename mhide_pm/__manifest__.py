# -*- coding: utf-8 -*-
{
    'name': "Hide Manage Databases & Powered By Odoo",
    'version': '0.1',
    'summary': 'Hide Manage Databases & Powered By Odoo',
    'sequence': -100,
    'description': """
        Hide Manage Databases & Powered By Odoo in Login Page
    """,
    'author': "InnoSA",
    'website': "#",
    'category': 'Uncategorized',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'data': [
        'views/views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 10.00,
    'currency': 'EUR', 
    'license': 'LGPL-3',
}


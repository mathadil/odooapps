# -*- coding: utf-8 -*-
{
    'name': "Hide any menu by user group",
    'summary': "Hide any menu by user group",
    'description': """
        Hide any menu by user group
    """,
    'author': "InnoSA",
    'website': "#",
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'data': [
        'security/security.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


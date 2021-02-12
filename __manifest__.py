# -*- coding: utf-8 -*-
{
    'name': "Delivery Note On Purchase",
    'summary': """
        Add the delivery note count and state on purchase order view tree""",
    'author': "Aresoltec Canarias S.L.",
    'website': "http://www.aresoltec.com",
    'category': 'Purchase',
    'version': '0.1',
    'depends': ['purchase', 'stock'],
    'data': [
        'views/views.xml',
    ],
}
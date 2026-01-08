# -*- coding: utf-8 -*-
{
    'name': 'Etiqueta Zebra para Recepciones',
    'version': '18.0',
    'category': 'Inventory',
    'author': "Mauro Bogado, Exemax",
    'website': "http://www.exemax.com.ar",
    'summary': 'Impresión de etiquetas Zebra desde recepciones',
    'depends': ['stock'],
    'data': [
        #'views/stock_picking_views.xml',
        'report/report_action.xml',
        'report/report_template.xml',
    ],
    'installable': True,
}
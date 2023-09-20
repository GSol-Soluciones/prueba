# -*- coding: utf-8 -*-
#????????????????????????????????????????????????????????????????????????????
#?                                                                          ?
#?			 ,o888888o.      d888888o.       ,o888888o.     8 8888          ?
#?			8888     `88.  .`8888:' `88.  . 8888     `88.   8 8888          ?
#?		 ,8 8888       `8. 8.`8888.   Y8 ,8 8888       `8b  8 8888          ?
#?		 88 8888           `8.`8888.     88 8888        `8b 8 8888          ?
#?		 88 8888            `8.`8888.    88 8888         88 8 8888          ?
#?		 88 8888             `8.`8888.   88 8888         88 8 8888          ?
#?		 88 8888   8888888    `8.`8888.  88 8888        ,8P 8 8888          ?
#?		 `8 8888       .8'8b   `8.`8888. `8 8888       ,8P  8 8888          ?
#?			8888     ,88' `8b.  ;8.`8888  ` 8888     ,88'   8 8888          ?
#?			 `8888888P'    `Y8888P ,88P'     `8888888P'     8 888888888888  ? 
#?                                                                          ?
#?     SOFTWARE DEVELOPED AND SUPPORTED BY GSol Soluciones Informáticas     ?
#?                       COPYRIGHT (C) 2020 - TODAY                         ?
#?                           http://www.gsol.es                             ?
#?                                                                          ?
#????????????????????????????????????????????????????????????????????????????
{
    'name': "Documents Filter Custom",

    'summary': """
        Filtro para mostrar los documentos de un pedido de compras""",

    'description': """
    Filtro en documentos para mostrar los documentos de un pedido de compras,
    contenidos en cada uno de los productos del pedido.
    """,

    'author': "Jorge Aparici",
    'website': "https://www.gsol.es",

    'category': 'documents',
    'version': '16.0.0.1',

    'depends': ['documents'],
    'license': 'AGPL-3',
    'data': [
        'views/views.xml'
    ],
    'installable' : True,
}
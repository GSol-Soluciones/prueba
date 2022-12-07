# -*- coding: utf-8 -*-
#╔══════════════════════════════════════════════════════════════════════════╗
#║                                                                          ║
#║           ,o888888o.      d888888o.       ,o888888o.     8 8888          ║
#║          8888     `88.  .`8888:' `88.  . 8888     `88.   8 8888          ║
#║       ,8 8888       `8. 8.`8888.   Y8 ,8 8888       `8b  8 8888          ║
#║       88 8888           `8.`8888.     88 8888        `8b 8 8888          ║
#║       88 8888            `8.`8888.    88 8888         88 8 8888          ║
#║       88 8888             `8.`8888.   88 8888         88 8 8888          ║
#║       88 8888   8888888    `8.`8888.  88 8888        ,8P 8 8888          ║
#║       `8 8888       .8'8b   `8.`8888. `8 8888       ,8P  8 8888          ║
#║          8888     ,88' `8b.  ;8.`8888  ` 8888     ,88'   8 8888          ║
#║           `8888888P'    `Y8888P ,88P'     `8888888P'     8 888888888888  ║ 
#║                                                                          ║
#║     SOFTWARE DEVELOPED AND SUPPORTED BY GSol Soluciones Informáticas     ║
#║                       COPYRIGHT (C) 2020 - TODAY                         ║
#║                           http://www.gsol.es                             ║
#║                                                                          ║
#╚══════════════════════════════════════════════════════════════════════════╝
{
    'name': 'Factura cliente como empresa',
    'version': '14.0.0.1',
    'category': 'Accounting',
    'summary': 'Conmuta cliente por empresa en el informe',
    'license': 'OPL-1',
    'description': """
En la impresión de las facturas de cliente, cambia cliente por empresa y viceversa, mostrando los NIF en ambos casos.
    """,
    'website': 'https://www.gsol.es',
    'author': 'Jorge Aparici',
    'depends': ['account'],
    'data': [
        'views/paper_format.xml',
        'views/layout.xml',
        'views/report_header.xml',
        'views/report_footer.xml',
        'report/report_factura.xml',
    ],
    'installable': True,
    'auto_install': False,
}

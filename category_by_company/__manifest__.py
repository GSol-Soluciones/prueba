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
    "name": "Category by company",

    'summary': """
        Filter the product categories by company""",

    'description': """
        This module allows to Filter the categories product by company, in the
        list of product categories and filtering the categories when adding them to
        products.
    """,

    'author': "GSol Soluciones Informáticas",
    'website': "https://www.gsol.es",
    'license': "AGPL-3",
    'category': "Uncategorized",
    'version': "14.0.1.0.1",
    'price': 17.99,
    'currency': "EUR",
    'images': ['images/main_screenshot.png'], 
    'depends': ["base", "sale"],
    "data": [
        'views/category.xml',
    ],
    "installable": True,
}

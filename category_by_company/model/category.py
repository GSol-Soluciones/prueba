# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class ProductCategory(models.Model):
    _inherit = 'product.category'

    company_id = fields.Many2one('res.company', string="Company")

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        """
        """
        domain.append(('company_id','in', [False, self.env.company.id]))
        categories = super(ProductCategory, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        return categories

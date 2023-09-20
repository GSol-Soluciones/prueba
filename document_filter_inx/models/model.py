from odoo import api, fields, models, SUPERUSER_ID, _


class Document(models.Model):
    _inherit = 'documents.document'

    po_ids = fields.Text(string="PO", compute='_compute_purchase_order_value', store=True)

    @api.depends('res_model','res_id')
    def _compute_purchase_order_value(self):
        for rec in self:
            if rec.res_model == 'product.template':
                purchase = self.env['purchase.order.line'].search([('product_id.product_tmpl_id','=',rec.res_id)])
                rec_list = purchase.order_id.mapped('name')
                res = ', '.join(map(str, rec_list))
                rec.po_ids = res
            else:
                rec.po_ids = False
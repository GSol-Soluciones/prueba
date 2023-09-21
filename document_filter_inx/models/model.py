from odoo import api, fields, models, SUPERUSER_ID, _


class Document(models.Model):
    _inherit = 'documents.document'

    po_ids = fields.Text(string="PO", compute='_compute_purchase_order_value', store=True)
    purchase_line = fields.Many2many('purchase.order.line', string="Purchase Order Line", compute='_compute_purchase_order_get')

    def _compute_purchase_order_get(self):
        for rec in self:
            if rec.res_model == 'product.template':
                purchase = self.env['purchase.order.line'].search([('product_id.product_tmpl_id', '=', rec.res_id)])
                rec.purchase_line = purchase
                rec._compute_purchase_order_value()
            else:
                rec.purchase_line = False

    # @api.depends('res_model', 'res_id', 'purchase_line')
    def _compute_purchase_order_value(self):
        for rec in self:
            if rec.res_model == 'product.template':
                purchase = self.env['purchase.order.line'].search([('product_id.product_tmpl_id', '=', rec.res_id)])
                rec_list = purchase.order_id.mapped('name')
                res = ', '.join(map(str, rec_list))
                rec.po_ids = res
            else:
                rec.po_ids = False

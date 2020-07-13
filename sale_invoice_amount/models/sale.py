from odoo import models, fields, tools, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoiced_amount = fields.Monetary(
        string='Invoiced', store=True, readonly=True, compute='_compute_invoice_amount')
    balance_amount = fields.Monetary(
        string='Balance', store=True, readonly=True, compute='_compute_invoice_amount')

    @api.one
    @api.depends('order_line.qty_invoiced')
    def _compute_invoice_amount(self):
        sale = self.sudo()
        invoiced_amount = sum(inv.amount_total for inv in sale.invoice_ids.filtered(
            lambda x: x.state in ('draft', 'open', 'paid') and x.type in ('out_invoice','out_refund')))
        if invoiced_amount:
            sale.invoiced_amount = invoiced_amount
            sale.balance_amount = sale.amount_total - invoiced_amount
        else:
            sale.balance_amount = sale.amount_total

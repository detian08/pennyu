# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockImmediateTransfer(models.TransientModel):
    _inherit = 'stock.immediate.transfer'

    @api.one
    def process(self, cancel_backorder=False):
        return super(StockImmediateTransfer, self.sudo()).process(cancel_backorder)

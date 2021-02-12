# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    actual_state = fields.Char(compute='_compute_actual_state')

    def _compute_actual_state(self):
        if self.state == 'draft':
            value = 'Borrador'
        elif self.state == 'waiting':
            value = 'Esperando otra operación'
        elif self.state == 'confirmed':
            value = 'En espera'
        elif self.state == 'assigned':
            value = 'Preparado'
        elif self.state == 'done':
            value = 'Hecho'
        if self.state == 'cancel':
            value = 'Cancelado'

        self.actual_state = value

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    picking_count = fields.Integer()
    delivery_state = fields.Char(compute='_compute_delivery_state')

    @api.one
    def _compute_delivery_state(self):
        sp = self.env['stock.picking'].search([('origin', '=', self.name)], limit=1)
        self.delivery_state = sp.actual_state
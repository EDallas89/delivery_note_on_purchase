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

#    @api.onchange('actual_state')
#    def _onchange_actual_state(self):
#        if self.origin:
#            po =  self.env['purchase.order'].search([('name', '=', self.origin)], limit=1)
#            po.write({'delivery_state' : "Meh"})

#        if self.origin:
#            origin_split = self.origin.split(", ")
#            for origin in origin_split:   
#                ## purchase order - search purchase orders
#                po =  self.env['purchase.order'].search([('name', '=', origin)], limit=1)
#                po.write({'internal_note' : self.internal_note})
#


#    @api.model
#    def cron_previus_deliverys(self):
#        for record in self.search([]):
#            po = self.env['purchase.order'].search([('name', '=', record.origin)])
#            po.write({'delivery_state' : self.actual_state})

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    picking_count = fields.Integer()
    delivery_state = fields.Char(compute='_compute_delivery_state')

    @api.one
    def _compute_delivery_state(self):
        sp = self.env['stock.picking'].search([('origin', '=', self.name)], limit=1)
        self.delivery_state = sp.actual_state
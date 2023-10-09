# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    scale_no = fields.Char()
    moisture = fields.Float(digits = (12,2))
    truck_no = fields.Char()
    truck_driver = fields.Char()
    driver_mobile = fields.Char()
    loose_sale = fields.Boolean()
    harm_date = fields.Date(required=True)
    harm_reference = fields.Char(required=True)
    
    # @api.onchange('moisture')
    # def _onchange_moisture(self):
    #     for rec in self:
    #         if rec.moisture and rec.order_line:
    #             for line in rec.order_line:
    #                 line.moisture = rec.moisture
    
    def action_confirm(self):
        if not self.order_line:
            raise UserError(_("You can not confirm this sale order. No sale order line provided."))
        return super(SaleOrder, self).action_confirm()

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    moisture = fields.Float(digits = (12,3))
    loose_sale = fields.Boolean(related='order_id.loose_sale')
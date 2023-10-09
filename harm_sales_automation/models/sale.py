from odoo import models, fields, api


class SeleOrder(models.Model):
    _inherit = "sale.order"

    payment_type = fields.Selection(selection=[('cash', 'Cash'), ('credit', 'Credit')], default='cash')
    src_location_id = fields.Many2one(comodel_name='stock.location', required=True, string='Source Location')

    def action_confirm(self):
        res = super(SeleOrder, self).action_confirm()
        invoice_ids = self.invoice_ids
        if invoice_ids.state == 'posted' and invoice_ids.payment_state == 'not_paid':
            invoice_ids.action_cash_payment()

        #return res





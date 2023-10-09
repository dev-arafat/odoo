from odoo import models, fields, api

class SeleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string="Sale Description")

    def action_confirm(self):
        print('click')

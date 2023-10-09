from odoo import models, fields, api


class Harm_Inventory(models.Model):
    _inherit = "product.template"

    show_price_set = fields.Boolean()

    def action_button(self):
        line = self.attribute_line_ids.filtered(lambda l: l.attribute_id.name == 'Packing Size')
        value_id = line.value_ids.filtered(lambda l: l.name == 'Bag of 50 kg')
        ptav_id = self.env['product.template.attribute.value'].search(
            [('product_tmpl_id', '=', self.id), ('product_attribute_value_id', '=', value_id.id)])
        ptav_id.price_extra = self.list_price

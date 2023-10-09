# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    

    def action_create_harm_rice_attributes(self):
        # ptal = self.env['product.template.attribute.line']
        pav = self.env['product.attribute.value']
        attribute_id = self.env['product.attribute'].search([('name', '=', 'Packing Size')])
        attribute_line_ids = pav.search([('name', 'in', ('Bag of 25 kg', 'Bag of 50 kg'))])
        if attribute_id and attribute_line_ids and not self.attribute_line_ids:
            self.write({
                    'attribute_line_ids' : [(0, 0, {
                    'attribute_id' : attribute_id.id,
                    'value_ids' : attribute_line_ids.ids,
                })]
            })

    def action_create_harm_paddy_attributes(self):
        # ptal = self.env['product.template.attribute.line']
        pav = self.env['product.attribute.value']
        attribute_id = self.env['product.attribute'].search([('name', '=', 'Packing Size')])
        attribute_line_ids = pav.search([('name', 'in', ('Bag of 72 kg', 'Bag of 75 kg'))])
        if attribute_id and attribute_line_ids and not self.attribute_line_ids:
            self.write({
                'attribute_line_ids' : [(0, 0, {
                    'attribute_id' : attribute_id.id,
                    'value_ids' : attribute_line_ids.ids,
                })]
            })


    


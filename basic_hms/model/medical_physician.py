# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_physician(models.Model):
    _name = "medical.physician"
    _description = 'medical physician'


    #_rec_name = 'partner_id'

    def name_get(self):
        res = super(medical_physician, self).name_get()
        res = []
        for record in self:
            name = record.partner_id.name   #+(record.partner_id.email or '')
            res.append((record.id, name))
        return res


    partner_id = fields.Many2one('res.partner','Physician',required=True)
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string='Institution')
    code = fields.Char('Id')
    info = fields.Text('Extra Info')

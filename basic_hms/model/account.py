from odoo import models, fields, api
from odoo.exceptions import ValidationError
class AccountMove(models.Model):
    _inherit = "account.move"

    patient_id = fields.Many2one(string='Patient', comodel_name='medical.patient', ondelete='restrict',)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        for rec in self:
            rec.partner_id = rec.patient_id.patient_id.id
            res = {'domain': {'partner_id': [('id', '=', rec.patient_id.patient_id.id)]}}
            return res
            










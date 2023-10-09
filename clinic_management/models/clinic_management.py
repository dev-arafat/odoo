from odoo import models, fields, api

class Clinic(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string='Is Patient?')
    is_doctor = fields.Boolean(string='Is Doctor?')










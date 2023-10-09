from odoo import models, fields, api, _

class HospitalPatient(models.Model):
    _name = "hospital.doctor"
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
    ]
    _description = "Hospital Doctor"
    _rec_name = 'name'

    name = fields.Char(string="Doctor name", tracking=True)
    age = fields.Char(string="age", tracking=True, copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ],
       default='Male', tracking=True
    )
    # appointment_count = fields.Integer(string="Appointment Count", compute='_compute_appointment_count')

    note = fields.Text(string='Description')
    img = fields.Binary(string='Img')
    active = fields.Boolean(string='Active', default=True)

    # def _compute_appointment_count(self):
    #     for rec in self:
    #         appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
    #         rec.appointment_count = appointment_count

    def copy_data(self, default=None):
        if default is None:
           # print("hello")
            default = {}
            if not default.get('name'):
                default['name'] = _("%s (Ccopy)", self.name)
            # default['note'] = 'Copied Recode'
            return super(HospitalPatient, self).copy_data(default=default)



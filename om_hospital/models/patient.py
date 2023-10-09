from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
    ]
    _description = "Hospital Patient"
    _order = "id desc"

    name = fields.Char(string="name", required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    age = fields.Char(string="age", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ],
       default='Male', tracking=True
    )
    note = fields.Text(string='Description')
    state = fields.Selection([
                ('draft', 'Draft'),
                ('confirm', 'Confirm'),
                ('done', 'Done'),
                ('cancel', 'Cancel'),
    ],default='draft', string="State", tracking=True)
    img = fields.Binary(string='Img')
    responsible_id = fields.Many2one(string='Responsible', comodel_name='res.partner')
    appointment_count = fields.Integer(string="Appointment Count", compute='_compute_appointment_count')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointment')

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"



    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'new patient'
        res = super(HospitalPatient, self).create(vals)
        return res


    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['note'] = 'New patient'
        res['gender'] = 'other'
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            #print("Test")
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError("Name %s Already Exists" % rec.name)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError("Age cannot be Zero")

    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'view_mode': 'tree,form',
            'context': {'default_patient_id':self.id},
            'target': 'current'
        }
            # print("click")


    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = '[' + rec.name+']'+ rec.age
    #         result.append((rec.id, name))
    #     return result
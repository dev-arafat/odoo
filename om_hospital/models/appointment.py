from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
    ]
    _description = "Hospital Patient"
    _order = "patient_id, age"
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    age = fields.Char(string="age", related='patient_id.age', tracking=True, store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ],
        string='Gender'
    )
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', string="State", tracking=True)
    responsible_id = fields.Many2one(string='Responsible', comodel_name='res.partner')
    date_appointment = fields.Date(string='Date', required=True)
    prescription = fields.Text(string='Prescription')
    prescription_line_ids = fields.One2many('appointment.prescription.line', 'appointment_id', string='Prescription Line')

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
        # else:
        #     self.gender = ''

    def unlink(self):
        print("delete")
        if self.state == 'done':
            raise ValidationError("You Cannot Delete %s as it is in Done State" % self.name)


        # for record in self:
        #     account_ids = self.env['account.account'].search([('group_id', '=', record.id)])
        #     account_ids.write({'group_id': record.parent_id.id})
        #
        #     children_ids = self.env['account.group'].search([('parent_id', '=', record.id)])
        #     children_ids.write({'parent_id': record.parent_id.id})
        return super(HospitalAppointment, self).unlink()

    def action_url(self):
        return {
            # 'name': _("Visit Webpage Statistics"),
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.facebook.com/%s/' % self.prescription,

        }

class PrescriptionLine(models.Model):
    _name = "appointment.prescription.line"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string='Medicine')
    qty = fields.Char(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
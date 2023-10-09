from odoo import models, fields, api, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "crate.appointment.wizard"
    _description = "Create Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        # print(".........."self._context)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res

    #date_appointment = fields.Date(string="Date")
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)


    def action_create_appointment(self):
        # print("click button")
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            #'date': self.date_appointment,
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new'
            #'context': dict(self.env.context, edit=True, form_view_initial_mode='edit')
        }

    # def action_view_appointment(self):
    #     action = self.env.ref('om_hospital.action_appointment').read()[0]
    #     action['domain'] = [('patient_id','=', self.patient_id.id)]
    #     return action


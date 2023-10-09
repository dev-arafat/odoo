from odoo import models, fields, api, _


class SearchAppointmentWizard(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = "Search Appointment Wizard"

    #date_appointment = fields.Date(string="Date")
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        # print("click button")
        vals = {
            'patient_id': self.patient_id.id,
            #'date': self.date_appointment,
        }
        # appointment_rec = self.env['hospital.appointment'].create(vals)
        # return {
        #     'name': _('Appointment'),
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'hospital.appointment',
        #     'res_id': appointment_rec.id,
        #     'target': 'new'
        #     #'context': dict(self.env.context, edit=True, form_view_initial_mode='edit')
        # }

    def action_search_appointment_m1(self):
        action = self.env.ref('om_hospital.action_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action




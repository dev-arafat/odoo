from odoo import models, fields, api, _


class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Report Appointment Wizard"


    #date_appointment = fields.Date(string="Date")
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)

    def action_print_appointment(self):
        appointments = self.env['hospital.appointment'].search_read([])
        data = {
            'form':self.read()[0],
            'appointments':appointments
        }
        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
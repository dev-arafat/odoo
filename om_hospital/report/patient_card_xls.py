from odoo import models, fields, api

from odoo import models
class PartnerXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_detail_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
            sheet.write(0,1, obj.age)
            sheet.write(0,2, obj.gender)




    # def generate_xlsx_report(self, workbook, data, patient):
    #     sheet = workbook.add_worksheet('Patient ID card')
    #     bold = workbook.add_format({'bold': True})
    #     format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
    #     # sheet = workbook.add_worksheet('Patient ID Card')
    #     # sheet.set_column('D:E', 30)
    #     row = 3
    #     col = 3
    #     sheet.set_column('D:D', 12)
    #     for obj in patient:
    #         row += 1
    #         sheet.merge_range(row, col, row, col+1, 'Id Card', format_1)
    #
    #         row += 1
    #         sheet.write(row, col, 'Name', bold)
    #         sheet.write(row, col +1, obj.name)
    #         # sheet = workbook.add_worksheet(report_name[:31])
    #         # sheet.write(row, col +1, obj.name)
    #         row += 1
    #         #sheet.write(1, 1, obj.name)
    #         sheet.write(row, col, 'age', obj.age)
    #

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'hospital',
    'version' : '1.2',
    'summary': 'hospital managemente software',
    'sequence': 10,
    'description': """ hospital managemente software """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : ['sale','mail', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/kids.xml',
        'views/gender.xml',
        'views/sale.xml',
        'views/partner.xml',
        'data/data.xml',
        'report/report_view.xml',
        'report/patient_card.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}

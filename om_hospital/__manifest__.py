# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Hospital',
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/patient_female_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/odoo_playground_view.xml'
    ],

    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

from odoo import api,fields,models

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "patient tag"
    name=fields.Char(string="name" ,required=True)
    active=fields.Boolean(string="active",default=True)
    color=fields.Integer(string="color")
    color_2=fields.Char(string="color_2")
 
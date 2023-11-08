from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    name = fields.Char(string='Name', tracking=True)
    date_of_birth=fields.Date(string="Date of birth")
    age = fields.Integer(string='Age',compute='_compute_age', tracking=True)
    ref = fields.Char(string='reference')
    image=fields.Image(string='image')
    # ref = fields.Char(string='reference' ,default="hrx")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True,default="female")
    appointment_id=fields.Many2one('hospital.appointment',string='appointment')
    tag_ids = fields.Many2many('patient.tag', string='tags')
    active = fields.Boolean(string="active", default=True)

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        print("hello", vals)

    def write(self,vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        print("write method executed",vals)
        return super(HospitalPatient,self).write(vals)

        return super(HospitalPatient, self).create(vals)
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age=today.year-rec.date_of_birth.year
            else:
                rec.age=1


    def name_get(self):
       patient_list= []
       for record in self:
           print (type (record.ref),type(record.name))
           name= str(record.ref) + str(record.name)
           patient_list.append((record.id,name))
       return  patient_list



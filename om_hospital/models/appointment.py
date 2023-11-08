from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    patient_id = fields.Many2one('hospital.patient', string="patient")
    gender = fields.Selection(string='Gender', related='patient_id.gender',
    readonly=False)  # bydefault readonly true hota ha
    ref = fields.Char(string='reference')
    # ref=fields.Char(string='reference',related='patient_id.ref',default="hhh")
    appointment_time = fields.Datetime(string='appointment time', default=fields.Datetime.now)
    booking_date = fields.Date(string='booking date', default=fields.Date.context_today)
    _rec_name = 'patient_id'
    prescription = fields.Html(string='prescription')
    hide_sales_price = fields.Boolean(string="hide sales price")
    priority = fields.Selection([('0', 'Normal'), ('1', 'low'), ('2', 'High'), ('3', 'very High')], string='priority')
    # state = fields.Selection([('draft', 'Draft'), ('in_consultation', 'in_consultation'), ('done', 'Done')],
    # #string='Type',default='manual', readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('in_consultation', 'in_consultation'),('done','Done'),('cancel','cancel')], string='Type',default='draft',required=True)
    doctor_id=fields.Many2one('res.users',string='Doctor')
    pharmacy_line_ids=fields.One2many('appointment.pharmacy.lines','appointment_id', string="pharmacy lines")
    def action_test(self):
        print("Button clicked!!!!!")
        return {
            'effect': {
                          'fadeout': 'slow',
                          'message': "click sucessfully",
                          'type': 'rainbow_man',
                      }
        }

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id.ref:
            self.ref = self.patient_id.ref
        else:
            self.ref = "hhh"
        # self.ref=self.patient_id.ref
        # print(self.ref)
class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"
    product_id=fields.Many2one('product.product')
    price_unit=fields.Float(string='price')
    qty=fields.Integer(string="quantity")
    appointment_id = fields.Many2one('hospital.appointment',string="appointment")
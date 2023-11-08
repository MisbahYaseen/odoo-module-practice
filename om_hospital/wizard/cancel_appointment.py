from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "cancel appointment wizard"

    @api.model
    def default_get(self, fields):
        # print("Default get executed", fields)
        # return  super(CancelAppointmentWizard, self).default_get(fields)

        res = super(CancelAppointmentWizard, self).default_get(fields)
        print(".......context", self.env.context)
        if self.env.context.get('active_id'):
            res['appointment_id']= self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment",domain=[('state','=','draft')])
    reason = fields.Text(string="Reason" , default='Test Reason')
    date_cancel = fields.Date(string="Cancellation Date")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("sorry,cancellation is not allowed on the same day"))
        return
    # def action_cancel(self):
    #     action=self.env.ref('om_hospital.action_cancel_appointment').read()[0]
    #     return action

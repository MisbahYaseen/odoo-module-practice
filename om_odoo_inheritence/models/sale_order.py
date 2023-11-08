
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    # name=fields.Char(string='Name',required=True)
    # def test_function(self):
    #     return
    confirmed_user_id=fields.Many2one('res.users',string='Confirmed user')

    def action_confirm(self):
        print("sucess............")
        super(SaleOrder,self).action_confirm()
        self.confirmed_user_id=self.env.user.id
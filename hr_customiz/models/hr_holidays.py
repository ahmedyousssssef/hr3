from openerp.exceptions import UserError, AccessError
from openerp import models, fields, api, _


class hr_holidays(models.Model):
    _inherit = "hr.holidays"

    employee_position = fields.Many2one(related='employee_id.job_id', string='Employee Position' , readonly=True)
    emp_id = fields.Char(related='employee_id.employee_id', string='Employee ID' , readonly=True)
    # personal_charge = fields.Many2one('hr.employee', string='Contact During The Leave'),

    # @api.one
    # @api.depends('employee_id')
    # def get_id(self):
    #     self.emp_id = self.employee_id.id

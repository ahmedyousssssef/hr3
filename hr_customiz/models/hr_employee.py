#	-*-	coding:	utf-8	-*-
from openerp import models, fields, api, _
import re
from openerp.osv import osv
from datetime import date, datetime , time


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    employee_insurance_num = fields.Char(string='Social Insurance Number', copy=False, required=False)
    mobile_phone = fields.Char(string='Work Mobile', readonly=False)
    # mobile_phone = fields.D(string='Work Mobile', readonly=False)
    resignation_date = fields.Date('Resignation Date')
    birthdate_alterformat = fields.Char( string="Date of Birth", compute='get_birthdate_format')
    employment_alterformat = fields.Char(compute='get_employment_format')

    @api.one
    @api.depends('employment')
    def get_employment_format(self):
        if self.employment:
            self.employment_alterformat = datetime.strptime(self.employment, '%Y-%m-%d').strftime('%e %b %Y')

    @api.one
    @api.depends('birthday')
    def get_birthdate_format(self):
        if self.birthday:
            self.birthdate_alterformat = datetime.strptime(self.birthday, '%Y-%m-%d').strftime('%e %b %Y')




    def create(self,cr,uid,vals,context=None):
        if 'employee_insurance_num' in vals and vals['employee_insurance_num']:
            if re.match("^[0-9]*$", vals['employee_insurance_num']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Social Insurance Number'), _('Please enter a valid Social Insurance Number'))
        return super(HrEmployee, self).create(cr, uid,vals, context=context)

    @api.multi
    def write(self, vals):
        if 'employee_insurance_num' in vals and vals['employee_insurance_num']:
            if re.match("^[0-9]*$", vals['employee_insurance_num']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Social Insurance Number'), _('Please enter a valid Social Insurance Number'))
        return super(HrEmployee, self).write(vals)



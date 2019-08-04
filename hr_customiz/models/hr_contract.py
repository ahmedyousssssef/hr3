# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
from datetime import datetime
from dateutil import relativedelta
from openerp.exceptions import ValidationError


class hr_contract_inherit(models.Model):
    _inherit = 'hr.contract'



    @api.model
    def notify_emp_probabtion_end(self):
        # print(fields.Date.today() , "date")
        users=[]
        for rec in self.env['hr.contract'].search(['|' , ('trial_date_end' , '=' , fields.Date.today()),('date_end' , '=' , fields.Date.today())]):
            users.append(rec.employee_id.parent_id.user_id.partner_id.id)
            if rec.trial_date_end ==  fields.Date.today():
                post_vars = {'subject': "Employee Contract Renewal",
                             'body': '<a target=_BLANK href="/web?#id=' + str(
                                 rec.employee_id.id) + '&view_type=form&model=hr.employee&action=" style="font-weight: bold">' + rec.employee_id.name + '</a> Contract : ( <a target=_BLANK href="/web?#id=' + str(
                                 rec.id) + '&view_type=form&model=hr.contract&action=" style="font-weight: bold">' + rec.name + '</a> ) Probation period has ended today. ',
                             'partner_ids': users}
                thread_pool = self.env['mail.thread']
                thread_pool.message_post(
                    type="notification",
                    subtype="mt_comment",
                    **post_vars)
            if rec.date_end ==  fields.Date.today():
                post_vars = {'subject': "Employee Contract Ended",
                             'body': '<a target=_BLANK href="/web?#id=' + str(
                                 rec.employee_id.id) + '&view_type=form&model=hr.employee&action=" style="font-weight: bold">' + rec.employee_id.name + '</a> Contract : ( <a target=_BLANK href="/web?#id=' + str(
                                 rec.id) + '&view_type=form&model=hr.contract&action=" style="font-weight: bold">' + rec.name + '</a> ) has ended today. ',
                             'partner_ids': users}
                thread_pool = self.env['mail.thread']
                thread_pool.message_post(
                    type="notification",
                    subtype="mt_comment",
                    **post_vars)
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = "res.company"
    users_count = fields.Integer(string="Users",
                                   compute='compute_users_count',
                                   default=0)
    def compute_users_count(self):
        for record in self:
            record.users_count = self.env['res.users'].search_count([('company_id', '=', self.id)])

    def action_get_users_record(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Users',
            'view_mode': 'tree',
            'res_model': 'res.users',
            'domain': [('company_id', '=', self.id)],
            'context': "{'create': False}"
        }
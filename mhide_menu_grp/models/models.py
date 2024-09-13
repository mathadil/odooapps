# -*- coding: utf-8 -*-
from odoo import fields, models

class ResGroups(models.Model):
    _inherit = 'res.groups'

    def write(self, vals):
        res = super(ResGroups, self).write(vals)
        for record in self:
            for menu in record.hide_menu_ids:
                menu.write({
                    'restrict_group_ids': [fields.Command.link(record.id)]
                })
        return res

    def _get_is_admin(self):
        for rec in self:
            rec.is_admin = False
            if rec.id == self.env.ref('base.user_admin').id:
                rec.is_admin = True

    hide_menu_ids = fields.Many2many(
        'ir.ui.menu', string="Hidden Menu",
        store=True, help='Select menu items that need to be hidden to this Group.')
    
    is_admin = fields.Boolean(compute=_get_is_admin, string="Is Admin",
                              help='Check if the user is an admin.')




class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    restrict_group_ids = fields.Many2many(
        'res.groups', string="Restricted Groups", help='Groups restricted from accessing this menu.')

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_pbo = fields.Boolean(
        string='Hide Powered By Odoo', 
        help="Hide Powered By Odoo in Login Page",
        config_parameter='mhide_pm.hide_pbo')

    hide_mdb = fields.Boolean(
        string='Hide Manage Database', 
        help="Hide Manage Database in Login Page",
        config_parameter='mhide_pm.hide_mdb')

    # hide_pbo = self.env['ir.config_parameter'].sudo().get_param(mhide_pm.hide_pbo)
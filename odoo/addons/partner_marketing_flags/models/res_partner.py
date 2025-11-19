from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_is_vip = fields.Boolean("VIP")

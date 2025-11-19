from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_contact_comment = fields.Char("Contact Comment")

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_category_label = fields.Char("Category Label")

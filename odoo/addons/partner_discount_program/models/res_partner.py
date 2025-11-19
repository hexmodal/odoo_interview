from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_base_discount = fields.Float("Base Discount (%)", default=0.0)
    x_extra_discount = fields.Float("Extra Discount (%)", default=0.0)
    x_total_discount = fields.Float("Total Discount (%)", default=0.0)

    @api.onchange("x_base_discount", "x_extra_discount")
    def _onchange_discounts(self):
        for partner in self:
            base = partner.x_base_discount or 0.0
            extra = partner.x_extra_discount or 0.0
            partner.x_total_discount = base + extra

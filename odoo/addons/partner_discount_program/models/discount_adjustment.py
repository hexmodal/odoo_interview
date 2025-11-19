from odoo import fields, models


class PartnerDiscountAdjustment(models.Model):
    _name = "partner.discount.adjustment"
    _description = "Partner Discount Adjustment"

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    base_delta = fields.Float("Base Discount Change (%)", default=0.0)
    extra_delta = fields.Float("Extra Discount Change (%)", default=0.0)
    state = fields.Selection(
        [("draft", "Draft"), ("applied", "Applied")],
        string="Status",
        default="draft",
    )

    def action_apply(self):
        for adj in self:
            if not adj.partner_id:
                continue
            partner = adj.partner_id
            partner.x_base_discount = (partner.x_base_discount or 0.0) + (adj.base_delta or 0.0)
            partner.x_extra_discount = (partner.x_extra_discount or 0.0) + (adj.extra_delta or 0.0)
            adj.state = "applied"

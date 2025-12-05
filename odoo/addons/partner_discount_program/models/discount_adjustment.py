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
            # Calculate new discount values
            new_base = (partner.x_base_discount or 0.0) + (adj.base_delta or 0.0)
            new_extra = (partner.x_extra_discount or 0.0) + (adj.extra_delta or 0.0)
            # Update partner discounts using write() to persist changes
            partner.write({
                'x_base_discount': new_base,
                'x_extra_discount': new_extra,
            })
            # Mark adjustment as applied
            adj.write({'state': 'applied'})
        return True

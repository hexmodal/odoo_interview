from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_total_child_tree = fields.Integer(
        string="Total Contacts in Tree",
        compute="_compute_total_child_tree",
        store=True,
    )

    @api.depends("child_ids", "child_ids.x_total_child_tree")
    def _compute_total_child_tree(self):
        for partner in self:
            total = len(partner.child_ids)
            for child in partner.child_ids:
                total += child.x_total_child_tree
            partner.x_total_child_tree = total

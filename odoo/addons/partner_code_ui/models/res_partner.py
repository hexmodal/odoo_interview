from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_customer_code = fields.Char("Customer Code")

    @api.model
    def check_customer_code_unique(self, code, current_id=None):
        """Utility to check whether a given customer code is already used."""
        if not code:
            return {"exists": False}
        domain = [("x_customer_code", "=", code)]
        if current_id:
            domain.append(("id", "!=", current_id))
        exists = bool(self.search_count(domain))
        return {"exists": exists}

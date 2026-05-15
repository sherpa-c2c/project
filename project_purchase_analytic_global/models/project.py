# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class Project(models.Model):
    _inherit = "project.project"

    def action_open_project_purchase_orders(self):
        action_window = super().action_open_project_purchase_orders()
        context = dict(action_window.get("context") or {})
        for project in self:
            if project.account_id:
                context["default_analytic_distribution"] = {
                    str(project.account_id.id): 100
                }
                break
        context["create"] = True
        action_window["context"] = context
        if action_window.get("res_id"):
            action_window.update(
                {"views": [[False, "list"], [False, "form"]], "res_id": None}
            )
        return action_window

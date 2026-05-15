# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tests.common import TransactionCase


class TestProjectPurchaseAnalyticGlobal(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Project = cls.env["project.project"]
        cls.Partner = cls.env["res.partner"]
        cls.PurchaseOrder = cls.env["purchase.order"]
        cls.partner1 = cls.Partner.create({"name": "Partner1"})
        cls.project1 = cls.Project.create({"name": "Project1"})

    def test_analytic_distribution_context(self):
        action = self.project1.action_open_project_purchase_orders()
        distribution = action["context"].get("default_analytic_distribution")
        self.assertEqual(distribution, {str(self.project1.account_id.id): 100})
        purchase_order = self.PurchaseOrder.with_context(**action["context"]).create(
            {"partner_id": self.partner1.id}
        )
        self.assertEqual(purchase_order.analytic_distribution, distribution)

# Copyright 2025 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    stage_id = fields.Many2one(check_company=True)

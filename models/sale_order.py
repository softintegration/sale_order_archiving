# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    active = fields.Boolean('Active', default=True)

    def write(self,vals):
        if 'active' in vals and not self.user_has_groups("sale_order_archiving.group_sale_order_archiving"):
            raise UserError(_("You have not necessary rights to do this action,please contact the administrator"))
        return super(SaleOrder, self).write(vals)
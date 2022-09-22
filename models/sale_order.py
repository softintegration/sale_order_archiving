# -*- coding: utf-8 -*-

from odoo import models,fields,api,_


class SaleOrder(models.Model):
    _inherit = "sale.order"

    active = fields.Boolean('Active', default=True)



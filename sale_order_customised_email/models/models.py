# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_estimate(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.replace(hour=15, minute=0, second=0)
        return tomorrow

    est_delivery = fields.Datetime(string='Estimated Delivery Time', default=_get_estimate)

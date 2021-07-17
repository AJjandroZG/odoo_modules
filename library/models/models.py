# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBooks(models.Model):
    _name = 'library.book'

    @api.multi
    def compute_field(self):
        if self.active:
            self.page = 250
        else:
            self.page = 500


    name = fields.Char(string='Name')
    active = fields.Boolean('is active')
    page = fields.Integer(string='# Pages', compute=compute_field)
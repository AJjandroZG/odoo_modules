from odoo import models, fields, api

class FieldsModel(models.Model):
    # _inherit = 'sale.order'

    fiels_Many2one = fields.Many2one('product.tamplate', 'Campo Many2one')
    fiels_onChange = fields.Many2one('product.tamplate', 'Campo Many2one onChange')
    fiels_bool = fields.Boolean( 'Campo bool')
    fiels_char = fields.Char( 'Campo char')
from odoo import fields, models, api

class HrUniform(models.Model):
    _inherit = 'hr.employee'

    test = fields.Char(string="Size Zapato")
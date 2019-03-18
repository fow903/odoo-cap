from odoo import fields, models, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    uniformes = fields.One2many('hr.uniform','employee_id',string="uniformes")


class HrUniform(models.Model):
    _name = 'hr.uniform'

    employee_id = fields.Many2one(comodel_name='hr.employee')
    test = fields.Char()



from odoo import models, fields

class ResPartnerExtended(models.Model):
    _inherit = 'res.partner'
    
    rfc = fields.Char(string='RFC')
    tipo_operador = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ], string='tipo de operador')



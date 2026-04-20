from odoo import models, fields, api
class Envio(models.Model):
    _name = 'trade.envio'
    _description = 'Envío'


    id_envio = fields.Char(string='ID Envío')
    name = fields.Char(string='Referencia', required=True)

    modo_transporte = fields.Selection([

        ('maritimo', 'Marítimo'),
        ('aereo', 'Aéreo'),
        ('terrestre', 'Terrestre')
    ], string='Modo de Transporte')


    master_bl = fields.Char(string='Master BL')

    peso = fields.Float(string='Peso')


    @api.depends('peso')
    def compute_peso_total(self):
        for record in self:
         record.peso_total = record.peso + record.peso


    peso_total = fields.Float('peso total', compute= compute_peso_total)

    id_exp = fields.Many2one('trade.exp', string='Expediente')
    producto_ids = fields.Many2many('trade.producto', string='Productos')

    def nombre_funcion_python(self):
        return True



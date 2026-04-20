from odoo import models, fields
class AModel(models.Model):
    _name = 'trade.aduana'
    _description = "modelo sobre aduana"


    id_exp = fields.Many2one('trade.exp', string='Expediente')

    name = fields.Char(string='Referencia', required=True)

    id_aduana = fields.Char(string = "id ")
    codigo = fields.Char(string = "codigo")
    ubicacion = fields.Char(string = "ubicacion")
    tipo = fields.Selection([
        ('maritimo', 'Marítimo'),
        ('aereo', 'Aéreo'),
        ('terrestre', 'Terrestre')
        ], string='tipo de aduana')


    def _default_name(self):
     return self.get_value() 
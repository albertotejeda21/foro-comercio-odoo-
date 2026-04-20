from odoo import models, fields
class AModel(models.Model):
    _name = 'trade.exp'
    _description = "modelo sobre expediente"


    cliente_id = fields.Many2one('res.partner', string='Cliente')
    aduana_ids = fields.One2many('trade.aduana', 'id_exp', string='Aduanas')
    envio_ids = fields.One2many('trade.envio', 'id_exp', string='Envíos')

    name = fields.Char(string='Referencia', required=True)

    id_exp = fields.Char(string = "id del expediente ")
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('proceso', 'En Proceso'),
    
        ('finalizado', 'Finalizado')
    ], string='Estado', default='borrador')
    fecha = fields.Date(string='Fecha')


    def _default_name(self):
     return self.get_value() 
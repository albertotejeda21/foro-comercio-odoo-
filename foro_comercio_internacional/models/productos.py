from odoo import models, fields
class AModel(models.Model):
    _name = 'trade.product'
    _description = "modelo sobre producto"

    name = fields.Char(string='Referencia', required=True)

    id_producto = fields.Char(string='ID Producto')
    frac = fields.Char(string='Fracción Arancelaria')
    descripcion = fields.Text(string='Descripción')
    valor = fields.Float(string='Valor')



    env_id = fields.Many2many('trade.envio', string='envios del producto')



    def boton_hola_mundo(self):
        print("hola mundo desde odoo")
        return True

    def _default_name(self):
     return self.get_value() 
    
    
    def nombre_funcion_python(self):
        return True

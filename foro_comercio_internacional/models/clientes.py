from odoo import models, fields, api 
class AModel(models.Model):
    _name = 'trade.customer'
    _description = "modelo sobre el cliente"


    razon_social = fields.Char(string = "razon social")
    vat= fields.Char(string = 'id fiscal')
    nombre_comercial= fields.Char()
    email = fields.Char()
    lname = fields.Char('nombre', compute = 'get_nombre')

    @api.depends('nombre_comercial')
    def get_nombre(self):
        for record in self:
            record.lname = record.nombre_comercial 



    def nombre_funcion_python (self):
     return True; 
    

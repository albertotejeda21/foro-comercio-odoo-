from odoo import models, fields

class MiWizard(models.TransientModel):
    _name = 'trade.cerrar.expediente.wizard'
    _description = 'Asistente de Ejemplo'

    fecha_cierre = fields.Date(string="Fecha de Cierre", default=fields.Date.today(), required=True)
    comentario = fields.Text(string="Comentario", required=True)


    def confirmar_cierre(self):
        expediente_ids = self.env.context.get('active_ids')
        expedientes = self.env['trade.exp'].browse(expediente_ids)
        
        expedientes.write({
            'estado': 'finalizado',
            'fecha': self.fecha_cierre,
        })
        for exp in expedientes:
            exp.message_post(body=f"Cierre masivo: {self.comentario}")
            
        return {'type': 'ir.actions.act_window_close'}
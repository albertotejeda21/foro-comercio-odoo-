from odoo import http
from odoo.http import request
import json 
from odoo.http import Response

class TradeController(http.Controller):
    @http.route('/trade/expediente/<int:id>', auth='public', type='http')
    def get_expediente(self, id):
    
        expediente = request.env['trade.exp'].sudo().browse(id)
        if not expediente.exists():

            return Response(
                json.dumps({'error': 'Expediente no encontrado'}),
                content_type='application/json'
            )
        datos = {
            'id': expediente.id_exp,
            'nombre':expediente.name,
            'estado': expediente.estado,

        }
        return Response(json.dumps(datos), 
                        content_type='application/json'
                        )

    @http.route('/trade/expediente/', auth='public', type='json', methods=['POST'], csrf=False)
    def crear_expediente(self, **kwargs):
        #datos = request.jsonrequest
        datos = request.get_json_data()

        if not datos:
            return {'success': False, 'error': 'No se recibieron datos'}

        nuevo_expediente = request.env['trade.exp'].sudo().create(datos)

        return {
            'success': True, 
            'id': nuevo_expediente.id
        }


    @http.route('/trade/expediente/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def eliminar_expediente(self, id):
        expediente = request.env['trade.exp'].sudo().browse(id)
        
        if expediente.exists():
            expediente.unlink()
            return {'success': True, 'message': 'Expediente eliminado'}
        
        return {'success': False, 'error': 'No se encontró el registro'}


    @http.route('/trade/expediente/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def actualizar_expediente(self, id, **kwargs):
        datos = kwargs
        
        expediente = request.env['trade.exp'].sudo().browse(id)

        if expediente.exists():
            expediente.write(datos)
            return {
                'success': True,
                'message': f'Expediente {id} actualizado correctamente'
            }

        return {'success': False, 'error': 'Registro no encontrado'}



#@http.route('/add_partner', type='http', auth="public", website=True)
#def add_partner(self, **post):
 #   return json.dump({success:True })



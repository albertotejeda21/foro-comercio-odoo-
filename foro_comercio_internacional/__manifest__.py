{
    'name': 'Foro_comercio_internacional',
    'version': '1.0',
     'data':[
       'security/ir.model.access.csv',
       'views/envio_views.xml',
        'views/expediente_views.xml',
       'views/cliente_views.xml',
        'views/aduana_views.xml',
        'views/producto_views.xml',
        # 'views/report.xml',
      
       
    ],
    'author': 'Tu nombre',
    'category': 'Sales/International Trade',
    'summary': 'Gestion de operaciones de comercio internacional',
    'description': 'Modulo para gestionar importaciones, exportaciones y documentacion aduanal',
    'depends': ['base', 'sale', 'purchase', 'stock',],
    'installable': True,
    'auto_install': False,
    'application': True,
  
     
}


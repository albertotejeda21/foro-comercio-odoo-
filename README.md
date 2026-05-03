**Módulo personalizado para Odoo 18**
Módulo de gestión de operaciones de comercio exterior desarrollado sobre Odoo 18. Permite administrar clientes, expedientes, envíos, productos y puntos de aduana desde una interfaz integrada, con flujos de estado, validaciones y generación de reportes PDF.

CapaTecnologíaBackendPython 3.11FrameworkOdoo 18 (ORM, QWeb, XML)Base de datosPostgreSQLVistasXML (form, list, kanban)ReportesQWeb PDF

Modelos
ModeloDescripcióntrade.customerClientes con razón social, RFC y emailtrade.expExpedientes con flujo de estados y fechastrade.envioEnvíos con modo de transporte, peso y BLtrade.aduanaPuntos de aduana clasificados por tipotrade.productoProductos con fracción arancelaria

Funcionalidades

Funcionalidades

Flujo de estados en expedientes — transiciones borrador → en proceso → finalizado controladas por botones con validaciones en Python
Relaciones entre modelos — Many2one, One2many y Many2many entre expedientes, envíos, clientes y productos
Campos computados — cálculo automático de peso total y conteo de envíos con @api.depends
Validaciones de negocio — reglas con @api.constrains que protegen la integridad de los datos
Reactividad en formularios — limpieza automática de campos con @api.onchange
Vistas personalizadas — formularios, listas y vista kanban con widgets de estado, prioridad y etiquetas
Reportes PDF — generación de documentos con QWeb y layout corporativo de Odoo
Chatter y tracking — registro automático de cambios de estado con usuario y fecha
Wizard masivo — cierre de múltiples expedientes con fecha y comentario desde la vista lista
Herencia de modelos nativos — extensión de res.partner con campos propios de comercio exterior
API REST — endpoints CRUD para expedientes consumibles desde sistemas externos
Seguridad por grupos — control de acceso definido por roles de usuario
Menús y submenús propios — navegación independiente del módulo

API REST
MétodoEndpointDescripciónGET/trade/expediente/<id>Obtiene un expediente por IDPOST/trade/expediente/Crea un nuevo expedientePUT/trade/expediente/<id>Actualiza un expediente existenteDELETE/trade/expediente/<id>Elimina un expediente

Estructura del módulo
foro-comercio-internacional/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── clientes.py
│   ├── expediente.py
│   ├── envio.py
│   ├── aduana.py
│   ├── productos.py
│   └── partner.py
├── views/
│   ├── clientes_views.xml
│   ├── expediente_views.xml
│   ├── envio_views.xml
│   ├── aduana_views.xml
│   ├── productos_views.xml
│   ├── partner_views.xml
│   └── menus.xml
├── controllers/
│   ├── __init__.py
│   └── main.py
├── wizard/
│   ├── __init__.py
│   ├── wizard_model.py
│   └── mi_wizard_views.xml
├── report/
│   └── reporte_envio.xml
└── security/
    ├── ir.model.access.csv
    └── groups.xml

Instalación
Requisitos previos:

Odoo 18 instalado y corriendo
PostgreSQL configurado
Python 3.11+

Pasos:

Clona el repositorio dentro de la carpeta de addons de Odoo:

bashgit clone https://github.com/tu-usuario/foro-comercio-internacional.git

Agrega la ruta al addons_path en tu archivo odoo.conf:

addons_path = /ruta/a/tus/addons

Reinicia el servidor de Odoo:

bash./odoo-bin -c odoo.conf

Activa el modo desarrollador:
Ajustes → Activar modo desarrollador
Ve a Aplicaciones, busca Foro Comercio Internacional e instala 

Autor: Erick T.

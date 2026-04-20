**Módulo personalizado para Odoo 18**
Módulo de gestión de operaciones de comercio exterior desarrollado sobre Odoo 18. Permite administrar clientes, expedientes, envíos, productos y puntos de aduana desde una interfaz integrada, con flujos de estado, validaciones y generación de reportes PDF.

CapaTecnologíaBackendPython 3.11FrameworkOdoo 18 (ORM, QWeb, XML)Base de datosPostgreSQLVistasXML (form, list, kanban)ReportesQWeb PDF

Modelos
ModeloDescripcióntrade.customerClientes con razón social, RFC y emailtrade.expExpedientes con flujo de estados y fechastrade.envioEnvíos con modo de transporte, peso y BLtrade.aduanaPuntos de aduana clasificados por tipotrade.productoProductos con fracción arancelaria

Funcionalidades

Relaciones entre modelos — Many2one, One2many y Many2many entre expedientes, envíos, clientes y productos
Vistas personalizadas — formularios, listas y vista kanban con widgets de estado, prioridad y etiquetas
Reportes PDF — generación de documentos con QWeb y layout corporativo de Odoo
Seguridad por grupos — control de acceso definido por roles de usuario
Menús y submenús propios — navegación independiente del módulo

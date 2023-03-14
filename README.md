# Proyecto Modelos de Programación

Este proyecto se centra en la creación de un Ecommerce de Software, donde desarrolladores y personas de toda índole puedan navegar, subir y adquirir el software  
que deseen, claro es que este proceso implica gestión de usuarios, pagos, ventas, productos, etc. De esta manera se plantea la necesidad de implementar  
APIs, con las cuales se pueda gestionar de manera eficiente la interacción del backend con el usuario.

## APIs

Para la creación de las APIs y desarrollo del backend se utilizará el lenguaje de programación Python, con la librería Django es posible crear de manera  
rápida y eficiente las funcionalidades necesarias en este proyecto.

La API DAO_db administra todo el flujo de la base de datos, separando la lógica en 3 grandes aspectos, el usuario, el producto y la venta,  
esto se ve reflejado por medio de comentarios en cada archivo dentro de la API.

La configuración de la API está preestablecida para conectarse a una base de datos MySQL, no obstante, para conectarse por default  
con la configuración de Django, por favor reemplazar la variable "DATABASES" dentro del archivo APIs.settings.py con la siguiente variable:

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
  }
}

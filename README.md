# DestinyStoreBot 🎯
Bot desarrollado en Python con el uso de la librería nextcord para el servidor Destiny.

# Funcionalidades (Administrador)👑
- '/setup': Configurar el bot para la creación de los canales de 'bienvenida' y 'compras'.
- '/setup_bot': Configuración de la interfaz de compra. (Preferiblemente, debe hacerse en el canal 'compras').
- '/delete_tickets': Borrar los canales de tickets que estén inactivos. (Los canales inactivos se crean a través de la interfaz de compra).

# Funcionalidades (Todos) 👥
'/info': Muestra información sobre el servidor.
Guía de uso 🤔
Antes de ejecutar el archivo, desde la terminal dirígete a la carpeta raíz del proyecto y ejecuta pip install -r requirements.txt para instalar las dependencias requeridas.

1. Ejecuta el archivo 'main.py'. (Si todo salió correctamente, se mostrará un mensaje en la consola: '¡Destiny está en línea!')
2. Desde el canal general de tu servidor, ejecuta el comando '/setup'. Esto creará dos canales nuevos: 'bienvenido' y 'comprar'.
3. Ve al canal 'comprar' y ejecuta el comando '/setup_bot'. Se creará una interfaz de compra donde tendrás acceso a diferentes opciones.
- ¡Importante! Si el bot deja de funcionar, debes borrar la interfaz que se creó en 'compras' y volver a ejecutar el comando '/setup_bot'.
- En la ejecución de cada comando, espera al menos unos segundos antes de ejecutar el siguiente.

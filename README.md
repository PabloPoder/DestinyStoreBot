# DestinyStoreBot 🎯
Bot desarrollado en Python con uso de libreria nextcord para server Destiny.

# Funcionalidades (Administrador)👑
- '/setup': Configurar bot para la creacion de canal de 'bienvenida' y 'compras'.
- '/setup_bot': Configuracion de interfaz de compra. (Preferiblemente debe hacerce en canal 'compras').
- '/delete_tickets': Borrar canales de tickets que esten inactivos. (Los canales inactivos se crean en con la interfaz de compra).

# Funcionalidades (Todos) 👥
- '/info': Muestra info sobre el server.

# Guia de uso 🤔
Antes de ejecutar el archivo, desde la terminal dirigete a la carpeta raiz del proyecto y ejecuta ```pip install -r requirements.txt``` para instalar las dependencias requeridas.

1. Ejecutar archivo 'main.py'. (Si todo salio correctamente se vera un mensaje en consola: 'Destiny is On!')
2. Desde en canal general de su server ejecutar comando '/setup'. Esto creara dos canales nuevos: 'bienvenido' y 'comprar'.
3. Ir a canal 'comprar' y ejecutar comando '/setup_bot'. Se creara una interfaz de compra donde tendra acceso a diferentes opciones.
4. Importante! Si el bot dejase de funcionar debe borrar la interfaz que se creo en 'compras' y volver a ejecutar el comando '/setup_bot'
5. En la ejecucion de cada comando espere al menos unos segundos antes de ejecutar el siguiente.
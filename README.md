# Pokédex

Pokédex es una aplicación web que te permite buscar información sobre diferentes Pokémon. Utiliza la PokéAPI para recuperar información sobre los Pokémon y mostrarla en una interfaz de usuario amigable.

## Instalación

1. Clona este repositorio en tu máquina local
2. Instala un entorno virtual *(opcional)*
*Puedes saltarte este paso sin problemas*
Instala la librería de Python con el comando: `pip install virtualenv`
Crea el entorno virtual en la raíz de tu proyecto con el comando: `virtualenv venv`
Activa el entorno virtual creado anteriormente con el comando: `.\venv\Scripts\activate`
3. Instala los requerimientos con el comando: `pip install -r requirements.txt`
4. Ejecuta el comando: `python manage.py runserver`
5. Ahora puedes abrir el **localhost** o hacer clic aquí -> [Inicio](http://127.0.0.1:8000/ "Inicio")

## Uso

1. En la página de inicio, haz clic en el botón **registrarme**
2. Ingresa tus datos y haz clic en el botón **registrarme** *(serás redirigido al login)*
3. Haz clic en **iniciar sesión** *(serás redirigido a la página de inicio)*
4. Haz clic en **ver Pokémones**
5. Busca el Pokémon que quieras ver y haz clic en **ver detalles**
6. La aplicación mostrará información sobre el Pokémon seleccionado, como su imagen, tipo, habilidades, estadísticas y más.

## Contribución

Si deseas contribuir a este proyecto, eres bienvenido a hacerlo. Simplemente haz un fork de este repositorio, crea una nueva rama con tus cambios y envía una solicitud de extracción.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Para obtener más información, consulta el archivo LICENSE en este repositorio.

### Lista de tareas

- [ ] Agregar un buscador
- [ ] Crear una paginación de los Pokémones
- [ ] Mejorar el frontend
    - [ ] Página de inicio
    - [ ] Lista de Pokémones
    - [ ] Inicio de sesión y registro

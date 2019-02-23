import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() # Renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() # Almacena los datos del formulario
        numero = formulario['numero'] # Almacena el numero escrito en el input
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        pais = formulario['pais'] # Almacena el pais escrito en el input
        caracteristicas = formulario['caracteristicas'] # Almacena el equipo escrito en el input
        config.model_perro.insert_perro(numero, nombre, pais, caracteristicas) 
        raise web.seeother('/') # Redirecciona al index.html

import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, numero):
        perro = config.model_perro.select_numero(numero) 
        return config.render.update(perro) 

    def POST(self, nombre, pais,caracteristicas):
        formulario = web.input() # Almacena los datos del formulario Web
        numero = formulario['numero'] # Almacena el numero escrito en el input
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        pais = formulario['pais'] # Almacena el pais escrito en el input
        caracteristicas = formulario['caracteristicas'] # Almacena el equipo escrito en el input
        config.model_perro.update_perro(numero, nombre, pais,caracteristicas) # Actualiza los valores
        raise web.seeother('/') # Redirecciona al index.html

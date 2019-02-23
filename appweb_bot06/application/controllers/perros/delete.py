import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, numero):
        perro = config.model_perro.select_numero(numero) 
        return config.render.delete(perro) 
    def POST(self, numero):
        formulario = web.input() # Crea un objeto formulario con los datos enviados con el formulario
        numero = formulario['numero'] # Obtiene el numero almacenado en el formulario
        config.model_perro.delete_perro(numero) # Borra el registro del numero seleccionado
        raise web.seeother('/') # Renderiza a raiz

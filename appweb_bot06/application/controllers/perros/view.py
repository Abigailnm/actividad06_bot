import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, numero):
        perro = config.model_perro.select_numero(numero) # Selecciona el registro que coincida con el numero
        return config.render.view(perro) # Envia el registro y renderiza view.html

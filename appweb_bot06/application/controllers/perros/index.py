import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):
        perro = config.model_perro.select_perro().list() 
        return config.render.index(perro) 

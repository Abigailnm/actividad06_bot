import web
        
urls = ('/', 'application.controllers.perro.index.Index',
    '/insert', 'application.controllers.perro.insert.Insert',
    '/update/(.*)', 'application.controllers.perro.update.Update',
    '/delete/(.*)', 'application.controllers.perro.delete.Delete',
    '/view/(.*)', 'application.controllers.perro.view.View',)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()


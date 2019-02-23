import config as config # Importa el archivo config

db = config.db # Crea un objeto DB del objeto DB creado en config


def select_perro():
    try:
        return db.select('perro')
    except Exception as e:
        print "Model select_perro Error {}".format(e.args)
        print "Model select_perro Message {}".format(e.message)
        return None



def select_numero(numero):
    try:
        return db.select('perro', where='numero=$numero', vars=locals())[0] 
    except Exception as e:
        print "Model select_numero Error {}".format(e.args)
        print "Model select_numero Message {}".format(e.message)
        return None


def insert_perro(numero, nombre, pais,caracteristicas):
    try:
        return db.insert('perro', numero=numero, nombre=nombre, pais=pais, caracteristicas=caracteristicas) 
    except Exception as e:
        print "Model insert_perro Error {}".format(e.args)
        print "Model insert_perro Message {}".format(e.message)
        return None


def delete_perro(numero):
    try:
        return db.delete('perro', where='numero=$numero', vars=locals()) 
    except Exception as e:
        print "Model delete_perro Error {}".format(e.args)
        print "Model delete_perro Message {}".format(e.message)
        return None

def update_perro(numero, nombre, pais, caracteristicas): 
    try:
        return db.update('perro',
            nombre=nombre,
            pais=pais,
            caracteristicas=caracteristicas,
            where='numero=$numero',
            vars=locals())
    except Exception as e:
        print "Model update_perro Error {}".format(e.args)
        print "Model update_perro Message {}".format(e.message)
        return None

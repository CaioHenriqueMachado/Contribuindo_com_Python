from flask_restful import Resource

habilidades = ["Python", "Java", "Css", "HTML", "JavaScript"]

class Habilidades(Resource):
    def get(self):
        return habilidades
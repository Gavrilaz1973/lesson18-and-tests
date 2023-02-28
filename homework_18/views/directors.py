from flask_restx import Resource, Namespace
from models import Director, DirectorSchema


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = Director.query.all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        return DirectorSchema().dump(director), 200
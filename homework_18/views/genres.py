from flask_restx import Resource, Namespace
from models import Genre, GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = Genre.query.all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        return GenreSchema().dump(genre), 200
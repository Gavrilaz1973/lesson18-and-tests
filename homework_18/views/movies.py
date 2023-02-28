from flask_restx import Resource, Namespace
from flask import request
from models import Movie, MovieSchema

from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)
        elif year:
            movies = Movie.query.filter(Movie.year == year)
        else:
            movies = Movie.query.all()

        result = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        mov_json = request.json
        movie = Movie(**mov_json)
        db.session.add(movie)
        db.session.commit()
        return "", 201


@movie_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid):
        movie = Movie.query.get(uid)
        return MovieSchema().dump(movie), 200

    def put(self, uid):
        mov_jsn = request.json #data.pop('id')
        movie = Movie.query.get(uid)
        for field_name, field_value in mov_jsn.items():
            setattr(movie, field_name, field_value)
        db.session.add(movie)
        db.session.commit()
        return '', 204

    def delete(self, uid):
        movie = Movie.query.get(uid)
        db.session.delete(movie)
        db.session.commit()
        return '', 204



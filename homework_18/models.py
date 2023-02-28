from setup_db import db
from marshmallow import Schema, fields

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    genre_id = db.Column(db.String, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.String, db.ForeignKey('director.id'))
    director = db.relationship('Director')

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    rating = fields.Float()
    year = fields.Int()
    genre_id = fields.Str()
    director_id = fields.Str()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
from flask_restx import Namespace, Resource
from flask import request
from models import Book
from setup_db import db

book_ns = Namespace('books')

@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books = Book.query.all()
        res = []
        for book in books:
            res.append(book)
        return res, 200

    def post(self):
        data = request.json
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        book = Book.query.get(bid)
        result = book.__dict__
        del result['_sa_instance_state']
        return result, 200

    def put(self, bid):
        book = Book.query.get(bid)
        book_put = request.json
        book.name = book_put.get('name')
        book.author = book_put.get('author')
        book.year = book_put.get('year')
        book.pages = book_put.get('pages')
        db.session.add(book)
        db.session.commit()
        return "", 201

    def delete(self, bid):
        book_del = Movie.query.get(bid)
        db.session.delete(book_del)
        db.session.commit()
        return "", 204

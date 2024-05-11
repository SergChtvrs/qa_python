import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def bookscollector():
    bookscollector = BooksCollector()
    bookscollector.books_genre['Падение Дома Ашеров'] = 'Ужасы'
    bookscollector.books_genre['Молчание ягнят'] = 'Ужасы'
    bookscollector.books_genre['Приключения Шерлока Холмса'] = 'Детективы'
    bookscollector.books_genre['Незнайка на Луне'] = 'Фантастика'
    bookscollector.books_genre['Волшебник Изумрудного города'] = 'Мультфильмы'
    bookscollector.books_genre['Гензель и Гретель'] = 'Фантастика'

    return bookscollector

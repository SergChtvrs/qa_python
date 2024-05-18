import pytest


class TestBooksCollector:

    # проверяем, что книга добавлена, если ее название длиной 1, 10, 40 символов
    @pytest.mark.parametrize('book_name',
                             ['А',
                              'Американский психопатАмериканский психоп'],
                             ids=['длина 1 символ', 'длина 40 символов'])
    def test_add_new_book_with_param_length_successfully_added(self, book_name, bookscollector):
        bookscollector.add_new_book(book_name)
        assert book_name in bookscollector.get_books_genre()

    # проверяем, что книга не добавлена, если ее название длиной 0, 41, 50 символов
    @pytest.mark.parametrize('book_name',
                             ['',
                              'Американский психопатАмериканский психопа',
                              'Американский психопатАмериканский психопатАмерикаа'],
                             ids=['пустое значение', 'длина 41 символ', 'длина 50 символов'])
    def test_add_new_book_with_param_length_not_added(self, book_name, bookscollector):
        bookscollector.add_new_book(book_name)
        assert not book_name in bookscollector.get_books_genre()

    # проверяем что книга не добавляется, если она уже есть в коллекторе
    def test_add_new_book_add_book_already_in_list_not_added(self, bookscollector):
        dist_len = len(bookscollector.get_books_genre())
        new_book = 'Приключения Шерлока Холмса'
        bookscollector.add_new_book(new_book)
        assert (len(bookscollector.get_books_genre()) == dist_len and
                bookscollector.get_book_genre(new_book) == 'Детективы')

    # проверяем установку жанра ужасы
    def test_set_book_genre_set_horror_genre(self, bookscollector):
        new_book = 'Зов Ктулху'
        genre = 'Ужасы'
        bookscollector.add_new_book(new_book)
        bookscollector.set_book_genre(new_book, genre)
        assert bookscollector.get_book_genre(new_book) == genre

    # проверяем получение 2-x книг в жанре ужасы
    def test_get_books_with_specific_genre_get_two_horror_books(self, bookscollector):
        genre = 'Ужасы'
        assert len(bookscollector.get_books_with_specific_genre(genre)) == 2

    # проверяем получение подходящих для детей книг в разных жанрах
    def test_get_books_for_children_get_three_books_cartoon_and_fantasy_genre(self, bookscollector):
        assert len(bookscollector.get_books_for_children()) == 3

    # проверяем добавление 2-х книг в Избранное и удаление 1-й
    def test_delete_book_from_favorites_delete_one_of_two_books(self, bookscollector):
        book_1 = list(bookscollector.get_books_genre())[0]
        book_2 = list(bookscollector.get_books_genre())[1]
        bookscollector.add_book_in_favorites(book_1)
        bookscollector.add_book_in_favorites(book_2)
        bookscollector.delete_book_from_favorites(book_1)
        assert bookscollector.get_list_of_favorites_books() == [book_2]
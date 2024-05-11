import pytest


class TestBooksCollector:

    # проверяем, что книга добавлена, если ее название длиной 1, 10, 40 символов
    @pytest.mark.parametrize('book_name',
                             ['А',
                              'Американск',
                              'Американский психопатАмериканский психоп'],
                             ids=['длина 1 символ', 'длина 10 символов', 'длина 40 символов'])
    def test_add_new_book_with_param_length_successfully_added(self, book_name, bookscollector):
        bookscollector.add_new_book(book_name)
        assert book_name in bookscollector.books_genre

    # проверяем, что книга не добавлена, если ее название длиной 0, 41, 50 символов
    @pytest.mark.parametrize('book_name',
                             ['',
                              'Американский психопатАмериканский психопа',
                              'Американский психопатАмериканский психопатАмерикаа'],
                             ids=['пустое значение', 'длина 41 символ', 'длина 50 символов'])
    def test_add_new_book_with_param_length_not_added(self, book_name, bookscollector):
        bookscollector.add_new_book(book_name)
        assert not book_name in bookscollector.books_genre

    # проверяем что книга не добавляется, если она уже есть в коллекторе
    def test_add_new_book_add_book_already_in_list_not_added(self, bookscollector):
        bookscollector.add_new_book('Приключения Шерлока Холмса')
        key_lst = []
        for key in bookscollector.books_genre.keys():
            if key == 'Приключения Шерлока Холмса':
                key_lst.append(key)
        assert len(key_lst) == 1 and bookscollector.books_genre['Приключения Шерлока Холмса'] == 'Детективы'

    # проверяем установку жанра ужасы
    def test_set_book_genre_set_horror_genre(self, bookscollector):
        bookscollector.add_new_book('Зов Ктулху')
        bookscollector.set_book_genre('Зов Ктулху', 'Ужасы')
        assert bookscollector.get_book_genre('Зов Ктулху') == 'Ужасы'

    # проверяем получение 2-x книг в жанре ужасы
    def test_get_books_with_specific_genre_get_two_horror_books(self, bookscollector):
        assert bookscollector.get_books_with_specific_genre('Ужасы') == ['Падение Дома Ашеров', 'Молчание ягнят']

    # проверяем получение 3-x подходящие для детей книг в жанрах Мультфильм, Фантастика
    def test_get_books_for_children_get_three_books_cartoon_and_fantasy_genre(self, bookscollector):
        children_books_lst = []
        for book in bookscollector.get_books_for_children():
            if book in bookscollector.get_books_genre():
                children_books_lst.append(book)
        assert len(children_books_lst) == 3

    # проверяем добавление 2-х книг в Избранное
    def test_add_book_in_favorites_add_two_books(self, bookscollector):
        bookscollector.add_book_in_favorites('Приключения Шерлока Холмса')
        bookscollector.add_book_in_favorites('Падение Дома Ашеров')
        assert bookscollector.get_list_of_favorites_books() == ['Приключения Шерлока Холмса', 'Падение Дома Ашеров']

    # проверяем удаление книги из Избранного
    def test_delete_book_from_favorites_delete_one_of_two_books(self, bookscollector):
        bookscollector.add_book_in_favorites('Приключения Шерлока Холмса')
        bookscollector.add_book_in_favorites('Падение Дома Ашеров')
        bookscollector.delete_book_from_favorites('Приключения Шерлока Холмса')
        assert bookscollector.get_list_of_favorites_books() == ['Падение Дома Ашеров']

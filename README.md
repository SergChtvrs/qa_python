# qa_python_sprint_4
___

Реализованные тесты в классе ```TestBooksCollector``` :

+ ```test_add_new_book_with_param_length_successfully_added``` - проверяем, что книга добавлена, если ее название длиной 1, 10, 40 символов
+ ```test_add_new_book_with_param_length_not_added``` - проверяем, что книга не добавлена, если ее название длиной 0, 41, 50 символов
+ ```test_add_new_book_add_book_already_in_list_not_added``` - проверяем что книга не добавляется, если она уже есть в коллекторе
+ ```test_set_book_genre_set_horror_genre``` - проверяем установку жанра ужасы
+ ```test_get_books_with_specific_genre_get_two_horror_books``` - проверяем получение 2-x книг в жанре ужасы
+ ```test_get_books_for_children_get_three_books_cartoon_and_fantasy_genre``` - проверяем получение 3-x подходящие для детей книг в нескольких жанрах: мультфильм, фантастика
+ ```test_add_book_in_favorites_add_two_books``` - проверяем добавление 2-х книг в Избранное
+ ```test_delete_book_from_favorites_delete_one_of_two_books``` - проверяем удаление книги из Избранного
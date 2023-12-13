from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # №1 Проверка, что жанр установлен
    @pytest.mark.parametrize("name, genre, expected_genre", [
        ('Первому игроку приготовиться', 'Фантастика', 'Фантастика')
    ])
    def test_set_book_genre_positive_result(self,name, genre, expected_genre):
        collector1 = BooksCollector()
        collector1.add_new_book(name)
        collector1.set_book_genre(name, genre)
        assert collector1.get_book_genre(name) == expected_genre

    # №2 Проверка вывода с определённым жанром
    def test_get_books_with_specific_genre_with_add_two_books_positive_result(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Зов Ктулху')
        collector2.set_book_genre('Зов Ктулху', 'Ужасы')

        collector2.add_new_book('Черновик')
        collector2.set_book_genre('Черновик', 'Фантастика')
        assert collector2.get_books_with_specific_genre('Ужасы') == ['Зов Ктулху']

    # №3 Проверка книг подходящим детям
    def test_get_books_for_children_positive_result(self):

        collector3 = BooksCollector()
        collector3.add_new_book('Золушка')
        collector3.set_book_genre('Золушка', 'Мультфильмы')

        collector3.add_new_book('Башня')
        collector3.set_book_genre('Башня', 'Ужасы')
        assert 'Золушка' in collector3.get_books_for_children()

    # №4 Проверка, что оба жанра не добавлены в список книг для детей и получен пустой список
    def test_get_books_for_children_empty_result(self):

        collector4 = BooksCollector()
        collector4.add_new_book('Кристина')
        collector4.set_book_genre('Кристина', 'Ужасы')

        collector4.add_new_book('Убийство на улице Морг')
        collector4.set_book_genre('Убийство на улице Морг', 'Детективы')
        assert collector4.get_books_for_children() ==  []

    # №5 Проверка добавления книги в избранное
    def test_add_book_in_favorites_positive_result_one_book(self):

        collector5 = BooksCollector()
        collector5.add_new_book('Властелин колец')
        collector5.set_book_genre('Властелин колец', 'Фантастика')
        collector5.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector5.favorites

    # №6 Проверка удаления книги из избранного
    def test_delete_book_from_favorites_positive_result(self):

        collector6 = BooksCollector()
        collector6.add_new_book('Гарри Поттер')
        collector6.set_book_genre('Гарри Поттер', 'Фантастика')
        collector6.add_book_in_favorites('Гарри Поттер')
        collector6.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector6.get_list_of_favorites_books()

    # №7 Проверка получения словаря books_genre
    def test_get_books_genre_get_list_positive_result(self):

        collector7 = BooksCollector()
        collector7.add_new_book('Гарри Поттер')
        collector7.set_book_genre('Гарри Поттер', 'Фантастика')
        collector7.add_new_book('Убийство на улице Морг')
        collector7.set_book_genre('Убийство на улице Морг', 'Детективы')
        expected_result = {'Гарри Поттер': 'Фантастика','Убийство на улице Морг': 'Детективы'}
        assert collector7.get_books_genre() == expected_result

    # №8 Проверка, что у добавленной книги отсутствует жанр
    def test_get_book_genre_no_genre(self):

        collector8 = BooksCollector()
        collector8.add_new_book('Нет жанра')
        assert collector8.get_book_genre('Нет жанра') == ''

    # №9 Проверка, что книга с длинной 42 символа не добавилась
    def test_add_new_book_name_have_42_characters(self):

        collector9 = BooksCollector()
        collector9.add_new_book('Сказка о ТройкеИстория непримиримой борьбы')
        collector9.set_book_genre('Сказка о ТройкеИстория непримиримой борьбы', 'Фантастика')
        assert 'Сказка о ТройкеИстория непримиримой борьбы' not in collector9.books_genre

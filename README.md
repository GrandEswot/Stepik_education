main_project_stepic_autotests
Финальный тестовый проэкт по курсу Stepik "Автоматизация тестирования с помощью Selenium и Python"

Это базовый курс для начинающих тестировщиков, который научит вас писать автоматизированные UI-тесты на языке программирования Python с помощью библиотеки Selenium. А еще мы рассмотрим популярные фреймворки и хорошие практики написания автотестов.

В репозитории есть все нужные файлы. Все файлы, где хранятся страницы, лежат в отдельной папке pages.

есть следующие тесты:

test_user_can_add_product_to_basket

test_guest_can_add_product_to_basket

test_guest_cant_see_product_in_basket_opened_from_product_page

test_guest_can_go_to_login_page_from_product_page

Запуск с помощью следующей команды:

pytest -v --tb=line --language=en -m need_review

Все тесты написаны в стиле PageObject: нет assert в теле тестов, все методы действия и проверки выделены в отдельные методы в классах PageObject, все селекторы лежат в locators.py.
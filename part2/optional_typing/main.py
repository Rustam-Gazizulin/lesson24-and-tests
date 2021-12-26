# У вас есть функция get_user_by_id,
# которая получает пользователя из словаря с пользователями
# (users) по его идентификатору. Функция на вход принимает
# словарь users, в котором ключ - строка,
# значение - объект класса User, и число user_id.
# На выходе функция должна вернуть объект User,
# если в словаре есть пользователь с таким id или вернуть None.
# Подсказка: для решения можно использовать Option.


class User:
    pass


def get_user_by_id(users, user_id):
    return users.get(user_id)

# У вас есть функция get_postcode,
# которая получает из адреса (словарь address) почтовый индекс.
# Функция на вход принимает словарь, в котором ключ - строка,
# значение - или число или строка, на выходе должна вернуть почтовый индекс (число).
# Для успешного прохождения тестов
# при написании аннотаций используйте, пожалуйста, библиотеку typing

# Подсказка: для решения можно использовать Any или Union из typing.

from typing import Union, Dict


def get_postcode(address: Dict[str, Union[int, str]]) -> int:
    return int(address.get('postcode'))

import hashlib
from typing import Union

CURRENT_SALT: str = 'test_1'


# Вычисление остатка от деления по модулю хеш-функции
def get_hash_modulo(value: Union[str, int], modulo: int, salt: str) -> int:
    if not isinstance(modulo, int):
        raise TypeError('Неверно указан тип делителя')
    if modulo == 1:
        raise ValueError('Делитель должен быть больше единицы')
    else:
        hash_value = int(hashlib.md5(str.encode(str(value) + str(salt))).hexdigest(), 16)
        return hash_value % modulo


for i in range(10):
    hash = get_hash_modulo(value=i, modulo=10, salt=CURRENT_SALT)
    print(f'i={i} hash={hash}')

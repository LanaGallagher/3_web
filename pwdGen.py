import hashlib as h

def pwdGenerator(pwd_str: str, salt_str: str, num_char: str) -> str:
    # конкатенация строк
    pwd_str = pwd_str + salt_str
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_obj = h.sha256(byte_str)
    # преобразование хеш-объекта в обычную строку
    if not num_char.isnumeric():
        hex_str = hash_obj.hexdigest()
    else:
        hex_str = hash_obj.hexdigest()[:int(num_char)]
    # возврат результата
    # print(hex_str)
    return hex_str
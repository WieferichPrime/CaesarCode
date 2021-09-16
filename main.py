from encode import encode
from war import war


def main():
    # message = input('Введите слово для шифрования\n').split(' ')[0].lower()
    # key = int(input('Введите ключ (целое число)\n').split(' ')[0])
    # keyword = input('Введите ключевое слово\n').split(' ')[0].lower()
    # print(encode(message, keyword, key))
    print('Идёт зашифровка и расшифровка главы Войны и Мир...')
    war()
    print('Глава зашифрована и расшифрована, расшифрованный текст хранится в файле war_decoded.txt')


main()
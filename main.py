from frequency import frequency
def encode(word = 'сообщение', keyword = 'ключ', key = 3):
    if not (len(keyword) <= 32 - key and len(set(keyword)) == len(keyword)):
        return 'Некорректные входные значения'
    encoded = ''
    i = 0
    subst = ''
    ru = ''.join(frequency().keys())
    while len(subst) < key:
        if (ru[len(ru) - i - 1]) not in keyword:
            subst += ru[len(ru) - i - 1]
        i += 1

    encoded += subst[::-1]
    for char in keyword:
        encoded += char
    for char in ru:
        if char not in encoded:
            encoded += char
    return ''.join(list(map(lambda char: encoded[ru.find(char)], word)))

def main():
    message = input('Введите слово для шифрования\n').split(' ')[0].lower()
    key = int(input('Введите ключ (целое число)\n').split(' ')[0])
    keyword = input('Введите ключевое слово\n').split(' ')[0].lower()
    print(encode(message, keyword,key))

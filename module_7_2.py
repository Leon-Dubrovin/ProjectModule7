def custom_write(file_name, strings):
    strings_positions = {}
    if len(strings) > 0:   #в случае пустого списка возвращается пустой словарь
        with open(file_name, 'w', encoding='utf-8') as file:
            strings_positions[(1, 0)] = strings[0]
            file.write(strings[0])
            if len(strings) > 1:
                for i in range(1, len(strings)):
                    strings_positions[(i + 1, file.tell() + 2)] = strings[i]
                    file.write('\n' + strings[i])
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
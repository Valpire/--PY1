def get_count_char(str_):
    letter_dict = {

}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict
    print(letter_dict)


def letter_percentage(letter_dict):
    letters_dict = {

    }
    for letter, count in letter_dict.items():
        letters_dict[letter] = round(count / sum(letter_dict.values())*100,2)

    return letters_dict



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

#Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими). 
# Преобразовать каждое слово в строке, заменив в нем все последующие вхождения
# его первой буквы на символ «.»(точка). слово «МИНИМУМ» надо преобразовать в «МИНИ.У». 
# Количество пробелов между словами не изменять.
def transform_text(input_string):
    # Разделим строку на слова, сохраняя пробелы
    words = input_string.split(" ")
    transformed_words = []

    for word in words:
        if word:  # Проверяем, что слово не пустое
            first_letter = word[0]
            transformed_word = first_letter  #с первой буквы
            for char in word[1:]:
                #заменяем все вхождения первой буквы на '.'
                if char == first_letter:
                    transformed_word += '.'
                else:
                    transformed_word += char
            transformed_words.append(transformed_word)
        else:
            transformed_words.append("")  #сохраняем пустые места
    
    #объединяем слова обратно с пробелами
    result = " ".join(transformed_words)
    return result

#пример
input_string = "МИНИМУМ"
output_string = transform_text(input_string)
print(output_string)

def check_rhythm(poem):
    lines = poem.split()  # Разделение стихотворения на фразы по пробелам

    for line in lines:
        words = line.split('-')  # Разделение фразы на слова по дефисам
        # Подсчет гласных в каждом слове
        syllables = [count_vowels(word) for word in words]
        # Проверка, что все элементы равны первому
        if not all(s == syllables[0] for s in syllables):
            return "Пам парам"

    return "Парам пам-пам"


def count_vowels(word):
    vowels = 'aeiouаеёиоуыэюя'  # список гласных букв
    return sum(1 for letter in word.lower() if letter in vowels)


# Пример использования
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)

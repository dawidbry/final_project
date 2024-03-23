"""
Do zrobienia będzie funkcja `flatten_list` która przyjmować będzie listę która jako element może mieć albo kolejną listę,
albo liczbę całkowitą i w wyniku ma zwrócić wszystkie liczby całkowite bez zagnieżdżonych list, musimy założyć, że nie wiemy ile
będzie stopni zagnieżdżenia.
Przykładowa lista: [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]
Oczekiwany wynik: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

def flatten_list(list_of_lists):
    result = []
    for element in list_of_lists:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result

list_example = [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]
list_of_numbers = flatten_list(list_example)

print(list_of_numbers)


# dodano nowa tresc
a = [1234]




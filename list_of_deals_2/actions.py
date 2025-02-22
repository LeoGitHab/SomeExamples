from storage import LIST_WORKS_DICTS


def delete_act(index: int) -> list:
    for num, mem in enumerate(LIST_WORKS_DICTS, 1):
        for _, (key, val) in enumerate(mem.items()):
            print(num, key)
    index = input(f'Будет удалён элемент под номером {index} \n'
          f'Если желаете, введите № эл-та от 1 до {len(LIST_WORKS_DICTS)} ')
    index = int(index) - 1
    LIST_WORKS_DICTS.pop(index)
    return LIST_WORKS_DICTS


def filter_act(substring: str) -> list:
    substring = input(f'Будет выполнена фильтрация списка дел по строке "{substring}" \n'
          f'Если желаете, введите свою строку для фильтрации ')
    list_with_substring_in_key = []
    for num, mem in enumerate(LIST_WORKS_DICTS, 1):
        for _, (key, val) in enumerate(mem.items()):
            if substring.lower() in key.lower():
                list_with_substring_in_key.append(key)
    print(list_with_substring_in_key)
    return list_with_substring_in_key


def add_act():
    new_deal_dict = {}
    key = input('Введите новое дело ')
    new_deal_dict[key] = 'не выполнено'
    LIST_WORKS_DICTS.append(new_deal_dict)
    print('Новое дело успешно добавлено в список дел !')
    look_through_acts('не выполнено')


def look_through_acts(cond: str) -> list:
    list_acts_with_some_conditions = []
    for num, mem in enumerate(LIST_WORKS_DICTS, 1):
        for _, (key, val) in enumerate(mem.items()):
            if val == cond:
                list_acts_with_some_conditions.append((num, key))
    return list_acts_with_some_conditions

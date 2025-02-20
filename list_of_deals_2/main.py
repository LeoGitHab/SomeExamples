from actions import *


if __name__ == '__main__':
    actions = (
        {'action_name': 'Вывести выполненные дела', 'func': look_through_acts('выполнено')},
        {'action_name': 'Вывести невыполненные дела', 'func': look_through_acts('не выполнено')},
        {'action_name': 'Удалить дело', 'func': delete_act(1)},
        {'action_name': 'Добавить дело', 'func': add_act()},
        {'action_name': 'Отфильтровать дела по строке', 'func': filter_act('ремонт')}
    )

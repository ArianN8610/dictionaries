def operation(dict_result, value: dict) -> bool:
    internal_operations = ('==', '!=', '<', '>', '>=', '<=', 'in', 'not in', 'is', 'is not')
    opera = list(value.keys())[0]
    new_value = list(value.values())[0]

    if opera in internal_operations:
        return eval(f'dict_result {opera} new_value')
    else:
        ...


def check(dictionary: dict, condition: dict, parent_key: str = '') -> bool:
    parent_key = parent_key if parent_key else list(condition.keys())[0]
    bool_set = set()

    for key, value in condition.items():
        if key in ('and', 'or'):
            bool_set.add(check(dictionary, value, key))
        else:
            dict_result = dictionary

            for i in key.split('.'):
                dict_result = dict_result[i]

            bool_set.add(operation(dict_result, value))

    if parent_key:
        if parent_key == 'and':
            return False not in bool_set
        else:
            return True in bool_set


if __name__ == '__main__':
    a = {
        'origin': {
            'city': 'THR',
            'airport': 'IKA',
            'time': '02:00'
        },
        'destination': {
            'city': 'MHD',
            'airport': 'MHD',
            'time': '03:00'
        },
        'a': {'b': {1: 2}},
        'c': [1, 2]
    }
    b = {
        'or': {
            'a': {'==': {'b': {1: 2}}},
            'and': {
                'and': {
                    'origin.city': {'==': 'THR'},
                    'origin.time': {'==': '02:00'},
                    'or': {
                        'destination.city': {'!=': 'MHD'},
                        'destination.time': {'==': '04:00'}
                    }
                },
                'origin.airport': {'==': 'IKA'}
            },
            'c': {'==': [0, 1]}
        }
    }

    print(check(a, b))

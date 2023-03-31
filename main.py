from flatten import flatten_dict


def check(dictionary: dict, condition: dict) -> bool:
    operations = ('==', '!=', 'and', 'or')
    dictionary = flatten_dict(dictionary)
    bools = set()

    for key, value in flatten_dict(condition).items():
        result = []

        for i in key.split('.'):
            if i in operations:
                if result:
                    if i == "==":
                        if dictionary['.'.join(result)] == value:
                            bools.add(True)
                        else:
                            bools.add(False)

                    if i == "!=":
                        if dictionary['.'.join(result)] != value:
                            bools.add(True)
                        else:
                            bools.add(False)
            else:
                result.append(i)

    for i in condition:
        if i == "and":
            if False in bools:
                return False
            else:
                return True
        else:
            if bools != {False}:
                return True
            else:
                return False


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
        }
    }
    b = {
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
        }
    }

    print(check(a, b))

from typing import Any


def flatten_dict(data: Any, parent_key: str = "") -> dict:
    result = {}

    for key, value in data.items():
        try:
            if key.isdigit():
                key = f'"{key}"'
        except AttributeError:
            pass

        new_key = f"{parent_key}.{key}" if parent_key else str(key)

        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key))
        elif isinstance(value, (list, tuple, set)):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    result.update(flatten_dict(item, f'{new_key}.{index}'))
                else:
                    result.update({f'{new_key}.{index}': item})
        else:
            result.update({new_key: value})

    return result

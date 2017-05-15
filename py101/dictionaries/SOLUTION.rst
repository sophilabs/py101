.. sourcecode:: python

def print_only_even_keys(some_dict):
    for key in some_dict:
        if some_dict[key] % 2 == 0:
            print(key)

print_only_even_keys({ 'Alfred': 28, 'Mary': 29 })
print_only_even_keys({ 'Alfred': 31, 'Mary': 29 })

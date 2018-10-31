my_dict = {
    "key1": 1,
    "key2": {
        "key3": 5,
        "key4": {
            "key5": 10
        }
    }
}

def print_path(my_dict, depth = 1):
    for key in my_dict:
        if isinstance(my_dict[key], dict):
            print('Key: %s | Depth: %s' %(key, depth))
            print_path(my_dict[key], depth + 1)
        else:
            print('Key: %s | Depth: %s ' %(key, depth))

print_path(my_dict)
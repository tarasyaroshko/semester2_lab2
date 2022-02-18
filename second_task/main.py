"""
JSON Navigation Module
"""

import json

def parser():
    """
    JSON parser that helps to navigate
    through the JSON file.
    """
    user_input = '-'
    with (open('twitter2.json', 'r', encoding='utf-8')) as file:
        data = json.load(file)
        history = [data]
    
    print()
    print('If current level type is dictionary, ')
    print('enter the name of the key to navigate one step further.')
    print()
    print('If current level type is list, ')
    print('enter the index of an element to navigate one step further.')
    print()
    print('Use ".." to go up one level')
    print('Use enter to finish the program.')
    print()
    
    while user_input != '':
        if isinstance(data, dict):
            print('Available keys:')
            for index, key in enumerate(data.keys()): 
                print(f'{index+1}. {key}')
            print()
            user_input = input('>>> ')
            if user_input != '..' and user_input != '':
                history.append(data)
                data = data[user_input]

        elif isinstance(data, list):
            print(f'Length of the list: {len(data)}')
            print()
            user_input = input('>>> ')
            if user_input != '..' and user_input != '':
                history.append(data)
                data = data[int(user_input)]

        else:
            print(data)
            print("This is the last level, use '..' to navigate back")
            print("or use enter to finish the program.")
            user_input = input('>>> ')

        if user_input == '..':
            data = history.pop()

if __name__ == "__main__":
    parser()

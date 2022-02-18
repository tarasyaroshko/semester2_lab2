import json
def parser():
    key = '-'
    with (open('kved.json', 'r', encoding='utf-8')) as file:
        data = json.load(file)
        history = [data]
    
    while key != '':
        if isinstance(data, dict):
            print(f'Type of the current level: dictionary')
            print('Available keys:')
            for index, key in enumerate(data.keys()): 
                print(f'{index + 1}. {key}')
            print()
            key = input('Enter key or ".." to go up: ')
            while key not in data.keys():
                key = input('Please enter a valid key: ')
            if key != '..' and key != '':
                history.append(data)
                data = data[key]

        elif isinstance(data, list):
            print('Type of the current level: list')
            print(f'Available length: {len(data)}')
            print()
            key = input('Enter index of the list element or ".." to go up: ')
            if key != '..' and key != '':
                history.append(data)
                data = data[int(key)]

        else:
            print(data)
            print("There are no more levels.")
            key = input("Enter '..' to go up or press enter to exit: ")

    if key == '..':
            data = history.pop()

    print()
    print('End of the program', sep='\n')

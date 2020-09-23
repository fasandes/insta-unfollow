# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import escape


def print_hi(request):
    request_json = request.get_json(silent=True)
    if request_json and 'name' in request_json:
        name = request_json['name']
    return 'Hello {}!'.format(escape(name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('On g cloud function!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

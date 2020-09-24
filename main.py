from flask import escape
from google.cloud import datastore


def print_hi(request):
    request_json = request.get_json(silent=True)
    if request_json and 'name' in request_json:
        name = request_json['name']
    return 'Hello {}!'.format(escape(name))


def insert_user(request):
    request_json = request.get_json(silent=True)
    name = request_json['name']
    username = request_json['username']
    datastore_client = datastore.Client()
    kind = 'user'
    # The name/ID for the new entity

    task_key = datastore_client.key(kind)
    task = datastore.Entity(key=task_key)
    task['name'] = name
    task['username'] = username

    # Saves the entity
    datastore_client.put({
        'name': name,
        'username': username
    })

    result = datastore_client.get(task_key)
    print(result)

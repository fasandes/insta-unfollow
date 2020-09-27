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

    task_key = datastore_client.key(kind)
    task = datastore.Entity(key=task_key)
    task['name'] = name
    task['username'] = username

    datastore_client.put({
        'name': name,
        'username': username
    })

    result = datastore_client.get(task_key)
    return result


def revoke_permissions(request):
    request_json = request.get_json(silent=True)
    datastore_client = datastore.Client()
    kind = 'permission'

    user_key = datastore_client.key(kind)
    user = datastore.Entity(key=user_key)
    user.update(request_json)

    datastore_client.put(user)

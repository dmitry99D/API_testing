import requests
import json

def all_posts():
    responce = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(responce) == 100, 'not all posts returned'


def one_post():
    post_id = new_post()
    responce = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert responce['id'] == post_id


def post_a_post():
    body = json.dumps({
        "title": "fddfkghdf",
        "body": "gdfgdfgdfgdfgdfgdfgdfg",
        "userId": 1
    })
    headers = {"Content-Type": "application/json"}
    responce = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data=body,
        headers=headers
    )
    assert responce.status_code == 201, 'Status code is incorrect'
    assert responce.json()['id'] == 101, 'Id is incorrect'


def new_post():
    body = json.dumps({
        "title": "fddfkghdf",
        "body": "gdfgdfgdfgdfgdfgdfgdfg",
        "userId": 1
    })
    headers = {"Content-Type": "application/json"}
    responce = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data=body,
        headers=headers
    )
    return responce.json()['id']


def put_a_post():
    post_id = new_post()
    body = {
        "title": "fddfkghdf_DDDFDFFDFD",
        "body": "gdfgdfgdfgdfgdfgdfgdfg=%$%45456",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    responce = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert responce['title'] == 'fddfkghdf_DDDFDFFDFD'
    clearM(post_id)


def clearM(post_id):
    responce = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def patch_a_post():
    post_id = new_post()
    body = {  
        "body": "gdfgdfgdfgdfgdfgdfgdfg=%$%45456",
        "userId": 8
    }
    headers = {"Content-Type": "application/json"}
    responce = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(responce)  
    clearM(post_id)

def delete_post():
    post_id = new_post()
    responce = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(responce.json())  
    print(responce.status_code)

post_a_post()
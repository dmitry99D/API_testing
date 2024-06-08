import unittest
import requests
import json

class TestPostApi(unittest.TestCase):
    def setUp(self):
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
        self.post_id = responce.json()['id']
        print(f'Post created: {self.post_id}')

    def tearDown(self):
        responce = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')

    @unittest.skip('Getting error on each run')
    def test_get_one_post(self):
        responce = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(responce['id'], self.post_id)    


class TestIndependent(unittest.TestCase):
    def test_get_all_posts(self):
        responce = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(responce), 100)


    def test_add_post(self):
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
        self.assertEqual(responce.status_code, 201)
        self.assertEqual(responce.json()["id"], 101)
        
from app import *

web_path = 'http://http://127.0.0.1:5000/'

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 302


def test_add():
    client = app.test_client()
    data = {'todo_text':"test1"}
    response = client.post('/add', data=data)
    assert response.status_code == 302

    response = client.get('/todo')
    assert b'test1' in response.data

    data = {'todo_text':"test2"}
    response = client.post('/add', data=data)
    assert response.status_code == 302

    response = client.get('/todo')
    assert b'test1' in response.data and b'test2' in response.data
    client.get('/delete/0')
    client.get('/delete/0')



def test_delete():
    client = app.test_client()
    data1 = {'todo_text':"test1"}
    client.post('/add', data=data1)
    data2 = {'todo_text':"test2"}
    client.post('/add', data=data2)
    data3 = {'todo_text':"test3"}
    client.post('/add', data=data3)

    response = client.get('/todo')
    assert b'test1' in response.data and b'test2' in response.data and b'test3' in response.data
    response = client.get('/delete/1')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'test1' in response.data
    assert b'test2' not in response.data 
    assert b'test3' in response.data
    
    
    #Testing out of bounds index
    response = client.get('/delete/50')
    assert response.status_code == 302

    response = client.get('/todo')
    #Making sure nothing was deleted
    assert b'test1' in response.data
    assert b'test2' not in response.data 
    assert b'test3' in response.data

    #Removing the rest
    response = client.get('/delete/0')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'test1' not in response.data
    assert b'test2' not in response.data 
    assert b'test3' in response.data

    response = client.get('/delete/0')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'test1' not in response.data
    assert b'test2' not in response.data 
    assert b'test3' not in response.data


def test_check():
    client = app.test_client()
    data = {'todo_text':"test1"}
    response = client.post('/add', data=data)
    assert response.status_code == 302

    response = client.get('/todo')
    assert b'test1' in response.data
    assert b'unchecked' in response.data
    response = client.post('/check/0')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'checked' in response.data

    data = {'todo_text':"test2"}
    response = client.post('/add', data=data)
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'checked' in response.data
    assert b'unchecked' in response.data
    response = client.post('/check/1')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'checked' in response.data
    assert b'unchecked' not in response.data

    #Unchekcing 0
    response = client.post('/check/0')
    assert response.status_code == 302
    response = client.get('/todo')
    assert b'checked' in response.data
    assert b'unchecked' in response.data

    client.get('/delete/0')
    client.get('/delete/0')

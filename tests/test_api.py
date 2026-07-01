import requests

headers = {
    "x-api-key": "pub_dfc7d0e839a03ff8a894f20631dc4df12b170219281599c4badf237020bb6aa0"
   }

def test_login_valido():
    body = { 
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code == 200

def test_login_sin_password():
    body = { 
        "email": "eve.holt@reqres.in",
        
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code == 400

def test_create_user():
    body = { 
        "name": "morpheus",
        "email": "morpheus@mail.com",
        "password": "leader",
        "job": "leader"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json() #para que guarde la respuesta en formato json y poder imprimirla
    print(data) #imprimir la respuesta en formato json
    assert response.status_code == 201
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]
    assert response.elapsed.total_seconds() < 1
    
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

   
    assert response.status_code == 200
    print(response.elapsed.total_seconds()) #imprimir la respuesta en formato json
    assert response.elapsed.total_seconds() < 1
    
import requests
from faker import Faker
from user import User

fake = Faker()

def generate_experiment(user1: User, user2: User):
    # get aleatory user
    user = fake.random_element((user1, user2))
    


def login(user: User):
    username=user.username
    password=user.password
    try:
        r = requests.post("http://login/", json={"username": username, "password": password})
        return r.json().get("token", "")
    except:
        print("Error al conectarse con el servicio de login")
        return None

def update_user(user: User):
    user.update_country(fake.country())
    user.update_genra(fake.random_element(("M", "F")))
    user.update_age(fake.random_int(18, 100))

    edad = user.age
    genero = user.genra
    pais = user.country

    try:
        r = requests.post("http://usuario/", json={
                "username": user.username,
                "token": user.token,
                "edad": edad,
                "genero": genero,
                "pais": pais
            })
        return r.json().get("msg", "")
    except:
        print("Error al conectarse con el servicio de usuarios")
        return None



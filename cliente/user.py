class User:
    def __init__(self, username, password, idioma, token, country, genra, age, peso, estatura):
        self.username = username
        self.password = password
        self.token = token
        self.country = country
        self.genra = genra
        self.age = age
        self.peso = peso
        self.estatura = estatura
        self.idioma = idioma

    
    def update_token(self, token):
        self.token = token
    
    def update_genra(self, genra):
        self.genra = genra

    def update_country(self, country):
        self.country = country
    
    def update_age(self, age):
        self.age = age
    
    def update_peso(self, peso):
        self.peso = peso

    def update_estatura(self, estatura):
        self.estatura = estatura

    def update_idioma(self, idioma):
        self.idioma = idioma
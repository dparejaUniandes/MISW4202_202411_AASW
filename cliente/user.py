class User:
    def __init__(self, username, password, token, country, genra, age):
        self.username = username
        self.password = password
        self.token = token
        self.country = country
        self.genra = genra
    
    def update_token(self, token):
        self.token = token
    
    def update_genra(self, genra):
        self.genra = genra

    def update_country(self, country):
        self.country = country
    
    def update_age(self, age):
        self.age = age
    

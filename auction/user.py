class User:
    username: str
    password: str
    email: str
    phone: int
    address: str

    def __init__(self):
        self.user_type='guest'

    def register(self, name, password, email, phone, address):
        self.username=name
        self.password=password
        self.email=email
        self.phone=phone
        self.address=address

    def __repr__(self):
        s = 'Name: {0}, Email: {1}, Phone: {2}, Address: {3}, Type: {4}\n'
        s = s.format(self.username, self.email, self.phone, self.address, self.user_type)
        return s

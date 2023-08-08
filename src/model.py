class PersonalData:
    def __init__(self, name="", address="", phone_number=""):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'phone_number': self.phone_number
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['address'], d['phone_number'])
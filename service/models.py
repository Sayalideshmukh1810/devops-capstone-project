import logging
class DataValidationError(Exception):
    pass
class Account:
    logger = logging.getLogger("flask.app")
    data = {}
    index = 0
    def __init__(self, id=0, name="", email="", address="", phone=""):
        self.id, self.name, self.email, self.address, self.phone = id, name, email, address, phone
    def create(self):
        Account.index += 1
        self.id = Account.index
        Account.data[self.id] = self
        return self
    def update(self):
        if not self.id or self.id not in Account.data:
            raise DataValidationError("Non-existent account")
        Account.data[self.id] = self
        return self
    def delete(self):
        if self.id in Account.data:
            del Account.data[self.id]
    def serialize(self):
        return {"id": self.id, "name": self.name, "email": self.email, "address": self.address, "phone": self.phone}
    def deserialize(self, data):
        try:
            self.name, self.email, self.address, self.phone = data["name"], data["email"], data["address"], data["phone"]
        except KeyError as error:
            raise DataValidationError(f"Missing {error.args[0]}")
        return self
    @classmethod
    def all(cls):
        return [a for a in cls.data.values()]
    @classmethod
    def find(cls, account_id):
        return cls.data.get(account_id)

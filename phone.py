class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))
        # print(f"Calling {other_number} from {self.number}")

    def text(self, other_number, msg):
        print("Sending text top {} from {}".format(other_number, self.number))
        print(msg)

    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))

class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == None and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")

        if (fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else:
            print("Phone locked. Fingerprint does not match")

martin_iphone = IPhone(8887654535)
print("Martin's number is {}".format(martin_iphone.number))

martin_iphone.set_fingerprint("password")

print(martin_iphone.fingerprint)

martin_iphone.unlock("password123")
martin_iphone.call(7652435436)
martin_iphone.open_app("Tik Tok")

class Andriod(Phone):
    def __init__(self, phone_number):
       super().__init__(phone_number)
       self.keyboard = "Default"

    def set_keyboard(self, new_keyboard):
        self.keyboard = new_keyboard 

# josh_phone = Andriod(7898977765)

# josh_phone.set_keyboard("Dvorak")
# josh_phone.call(7893452435)

# josh_phone.open_app("Google Play Store")





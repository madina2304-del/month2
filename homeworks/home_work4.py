class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class Contactlist:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueErrror("Номер телофона должен содержать 10 цифр")

Contactlist.add_contact("Мадина", "0500996226")
for contact in Contactlist.all_contacts:
    print(contact.name, contact.phone_number)
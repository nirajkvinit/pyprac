
class PhoneBook:
    def __init__(self):
        self.phoneBook = {}

    def addContact(self, name, phoneNumber):
        self.phoneBook[name.strip()] = phoneNumber.strip()

    def getContact(self, name):
        phoneNumber = self.phoneBook.get(name.strip(), '')
        if phoneNumber:
            return "{}={}".format(name, phoneNumber)
        else:
            return "Not found"

if __name__ == "__main__":
    entries = 0
    phoneBook = PhoneBook()
    while True:
        inputVal = input()
        if inputVal.isdigit():
            entries = int(inputVal)
        elif inputVal == "":
            break
        else:
            if entries > 0:
                inputValArr = inputVal.split(" ")
                phoneBook.addContact(inputValArr[0], inputValArr[1])
                entries -= 1
            else:
                print(phoneBook.getContact(inputVal))

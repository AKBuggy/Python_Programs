class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
        print("😁😎😍")


class AkEditor:
    def execute(self):
        print("Ankit's editor")
        print("Can add emojis to the code 😊😋🤗🥱😂🤣")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = AkEditor()
# ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)

a, b = 3, 5
print(int.__add__(a, b))

class Human:
    # __init__ is like constructor in other lang like java, c++ etc
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            # print(self.name, "plays tennis")
            print(f"{self.name} plays tennis")  # different ways to print
        elif self.occupation == "actor":
            print(f"{self.name} shoots films")
        elif self.occupation == "coder":
            print(self.name, "is coding right now")

    def speaks(self):
        print(self.name, "says how are you?")


ankit = Human("AkBuggy", "coder")
ankit.do_work()
ankit.speaks()

jalaja = Human("Jalaja Prakash", "tennis player")
jalaja.do_work()
jalaja.speaks()

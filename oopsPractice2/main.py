class Parent:
    @staticmethod
    def print_parent_name():
        print("I am a parent inside print_parent_name method")


class Child(Parent):
    @staticmethod
    def print_child_name():
        print("I am a child inside print_child_name method")


def main():
    child = Child()
    child.print_child_name()


if __name__ == '__main__':
    main()

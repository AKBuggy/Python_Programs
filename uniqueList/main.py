# Take Five Inputs from user and if the number inputted is already in the list then ask user to type unique number


class Logic:
    def __init__(self, ele, inp_list):
        self.ele = ele
        self.inp_list = inp_list

    def is_unique(self):
        return self.ele not in self.inp_list


def main():
    inp_list = []

    while len(inp_list) != 5:
        ele = int(input("Enter no.:"))
        obj = Logic(ele, inp_list)
        if obj.is_unique():
            inp_list.append(ele)
        else:
            print("Enter No. which is unique")

    print(inp_list)


if __name__ == '__main__':
    main()

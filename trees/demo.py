class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        if self.children:    # len(self.children) > 0
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("HP"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Oneplus"))
    cellphone.add_child(TreeNode("MI"))
    cellphone.add_child(TreeNode("IPhone"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Impex"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    # root.print_tree()
    root.get_level()
    pass

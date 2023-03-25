class ParentClass:
    def parent_method(self):
        print("This is the parent method")


class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        return super().parent_method()

    def child_method(self):
        print("This is the child method")
        # super keyword is used to call the methods of parent class inside a child class
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

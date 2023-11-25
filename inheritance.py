class A:

    def __init__(self):
        print('in init a')
        
    def feature1(self):
        print("feature1 working")

    def feature2(self):
        print("feature2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print('in init b')
    
    def feature3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")

class C(B):
    def __init__(self):
        super().__init__()
        print('in init c')

a1=C()
a2=B()



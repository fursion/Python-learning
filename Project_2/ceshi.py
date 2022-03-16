def im():
    print("im test")


class C_a:
    def __init__(self) -> None:
        print("C_a")


class C_b(C_a):
    def __init__(self) -> None:
        print("C_b")
    def fun01():
        print("C_b_fun01")
c=C_b()
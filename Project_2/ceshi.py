def im():
    print("im test")


class Ca:
    def __init__(self) -> None:
        print("C_a")


class Cb(Ca):
    def __init__(self) -> None:
        print("C_b")

    @staticmethod
    def fun01(self):
        print("C_b_fun01")


c = Cb()

class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except (ZeroDivisionError, NameError) as e:
            print(e)

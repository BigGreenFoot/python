class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except (ZeroDivisionError, TypeError) as e:
            print(e)

class Percent1:
    def execute(self, x, y):
        return x + y


class Percent2:
    def execute(self, x, y):
        return x + y * .1


class Percent3:
    def execute(self, x, y):
        return x - y


class Percent4:
    def execute(self, x, y):
        return y


class Context:
    strategy = None

    def set_stretegy(self, strategy):
        self.strategy = strategy

    def execute(self, x, y):
        return self.strategy.execute(x, y)


def get_strategy():
    strategy_number = int(input("Введите номер стратегии "))

    strategy = None

    if strategy_number == 1:
        strategy = Percent1()

    if strategy_number == 2:
        strategy = Percent2()

    if strategy_number == 3:
        strategy = Percent3()

    if strategy_number == 4:
        strategy = Percent4()

    return strategy


def run_strategy(strategy):
    if strategy is None:
        print("Стратеги не выбрана")
    else:
        context = Context()
        context.set_stretegy(strategy)
        result = context.execute(3, 4)
        print("Результат", result)


if __name__ == '__main__':
    strategy = get_strategy()
    run_strategy(strategy)

class Monkey:
    def __init__(self, monkey_do):
        monkey_stats = monkey_do.splitlines()
        self.items = eval('[' + monkey_stats[1][18:] + ']')
        self.operation = eval('lambda old: ' + monkey_stats[2][19:])
        self.test = int(monkey_stats[3][21:])
        self.iftrue = int(monkey_stats[4][29:])
        self.iffalse = int(monkey_stats[5][30:])
        self.inspect_count = 0
    
    def play(self, worry_divider):
        while self.items:
            self.inspect_count += 1
            worry = self.operation(self.items.pop(0))
            worry = worry % 9699690 if worry_divider == 1 else worry // worry_divider
            yield self.iffalse if worry % self.test else self.iftrue, worry

def play_a_game(rounds, worry_divider):
    with open(r'file.txt') as f:
        monkeys = [Monkey(monkey_do) for monkey_do in f.read().split('\n\n')]

    for _ in range(rounds):
        for monkey in monkeys:
            for catcher, worry in monkey.play(worry_divider):
                monkeys[catcher].items.append(worry)

    for i in monkeys:
      print(i.inspect_count)

    return (lambda x, y: x.inspect_count * y.inspect_count) \
        (*sorted(monkeys, key=lambda monkey: monkey.inspect_count)[-2:])

part1 = play_a_game(20, 3)
print("Part 1:", part1)

part2 = play_a_game(10000, 1)
print("Part 2:", part2)
from functools import reduce
from operator import mul



class Ticket:
    def __init__(self, ticket_txt):
        self.rows = [self.parse_line(line) for line in ticket_txt.split("\n")]
        self.coords = {}
        self.row_score = [0] * 5
        self.col_score = [0] * 5
        self.numbers = set()
        for row_num, row in enumerate(self.rows):
            for col_num, number in enumerate(row):
                self.coords[number] = (row_num, col_num)
                self.numbers.add(number)

    @staticmethod
    def parse_line(line):
        return list(map(int, line.split()))

    def process(self, n):
        if n not in self.coords:
            return False
        row, col = self.coords[n]
        self.row_score[row] += 1
        self.col_score[col] += 1
        self.numbers.discard(n)
        if self.row_score[row] == 5 or self.col_score[col] == 5:
            return True
        return False


def part1(numbers, tickets):
    for n in numbers:
        for t in tickets:
            bingo = t.process(n)
            if bingo:
                return sum(t.numbers) * n


def part2(numbers, tickets):
    for n in numbers:
        new_tickets = []
        for t in tickets:
            if t.process(n):
                if len(tickets) == 1:
                    return sum(t.numbers) * n
            else:
                new_tickets.append(t)
        tickets = new_tickets


def main():
    numbers_txt, *tickets_txt = open("input.txt").read().split("\n\n")
    numbers = list(map(int, numbers_txt.split(',')))
    tickets = [Ticket(tickets_txt) for tickets_txt in tickets_txt]
    # print(part1(numbers, tickets))
    # print(part2(numbers, tickets))

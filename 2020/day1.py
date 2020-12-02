"--- Day 1: Report Repair ---"
from operator import xor

__author__ = "Shyamal Akruvala"

def test():
    lines = ['1721\n','979\n','366\n','299\n','675\n','1456\n']
    part1(lines) # expected answer is 514579
    part2(lines) # expected answer is 241861950

def part1(lines):
    for x in lines:
        for y in lines:
                if (int(x) + int(y) == 2020):
                    print("Part 1 - The numbers are {} and {} and product is {}".format(int(x), int(y), int(x)*int(y)))

def part2(lines):
    for x in lines:
        for y in lines:
            for z in lines:
                if (int(x) + int(y) + int(z) == 2020):
                    print("Part2 - The numbers are {} and {} and {} and product is {}".format(int(x), int(y), int(z), int(x)*int(y)*int(z)))

if __name__ == "__main__":
    # test()
    print("--- Day 1: Report Repair ---")
    with open("./2020/input/inputDay1.txt","r") as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
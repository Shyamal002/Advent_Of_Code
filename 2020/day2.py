"--- Day 2: Password Philosophy ---"
from operator import xor

@author = "Shyamal Akruvala"

def test():
    lines = ['1-3 a: abcde\n', '1-3 b: cdefg\n', '2-9 c: ccccccccc\n']
    part1(lines) # expected answer is 2
    part2(lines) # expected answer is 1

def part1(lines):
    counterForGoodPasswords = 0
    for line in lines:
        pwdPolicy, passwordString = line.split(":")
        pwdNumbers, pwdCharacter = pwdPolicy.split(" ")
        minNumber, maxNumber = pwdNumbers.split("-")
        minNumber = int(minNumber)
        maxNumber = int(maxNumber)
        if passwordString.count(pwdCharacter) >= minNumber and passwordString.count(pwdCharacter) <= maxNumber:
            counterForGoodPasswords = counterForGoodPasswords + 1
    print("Part 1 - good password count is {}".format(counterForGoodPasswords))

def part2(lines):
    counterForGoodPasswords = 0
    for line in lines:
        pwdPolicy, passwordString = line.split(":")
        passwordString = passwordString.strip()
        pwdNumbers, pwdCharacter = pwdPolicy.split(" ")
        minNumber, maxNumber = pwdNumbers.split("-")
        minNumber = int(minNumber) - 1
        maxNumber = int(maxNumber) - 1
        if xor(bool(passwordString[minNumber] == pwdCharacter), bool(passwordString[maxNumber] == pwdCharacter)):
            counterForGoodPasswords = counterForGoodPasswords + 1
    print("Part 2 - good password count is {}".format(counterForGoodPasswords))

if __name__ == "__main__":
    # test()
    print("--- Day 2: Password Philosophy ---")
    with open("./2020/input/inputDay2.txt","r") as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
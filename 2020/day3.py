"--- Day 3: Toboggan Trajectory ---"

__author__ = "Shyamal Akruvala"

def test():
    lines = ['..##.......\n',
             '#...#...#..\n',
             '.#....#..#.\n',
             '..#.#...#.#\n',
             '.#...##..#.\n',
             '..#.##.....\n',
             '.#.#.#....#\n',
             '.#........#\n',
             '#.##...#...\n',
             '#...##....#\n',
             '.#..#...#.#\n']
    print(part1([line.strip() for line in lines], (3,1)))

def part1(lines, slope):
    pos_x, pos_y, treesCounter = 0, 0, 0
    width = len(lines[0])
    while pos_y < len(lines):
        if lines[pos_y][pos_x] == '#':
            treesCounter += 1
        pos_x += slope[0]
        pos_y += slope[1]
        pos_x %= width
    return treesCounter

if __name__ == "__main__":
    print("--- Day 3: Toboggan Trajectory ---")
    # test()
    with open("./2020/input/inputDay3.txt","r") as f:
        lines = [line.strip() for line in f]
        print("Part1 - Number of trees are {}".format(part1(lines, (3,1))))
        print("Part2 - Number of trees are {}".format(part1(lines, (1,1)) * 
                                                        part1(lines, (3,1)) * 
                                                        part1(lines, (5,1)) * 
                                                        part1(lines, (7,1)) * 
                                                        part1(lines, (1,2))))

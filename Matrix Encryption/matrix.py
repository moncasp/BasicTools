matrix = [
    ["V", "r", "L", "e", "G", "z"],
    ["E", "b", "C", "B", "Q", "o"],
    ["q", "_", "t", "y", "Z", "H"],
    ["K", "8", "J", "6", "j", "X"],
    ["N", "F", "s", "D", "a", "3"],
    ["Y", "T", "O", "{", "c", "1"],
    ["m", "W", "h", "U", "w", "5"],
    ["n", "+", "S", "}", "4", "p"],
    ["i", "f", "l", "9", "x", "k"],
    ["A", "0", "7", "g", "M", "v"],
    ["u", "2", "P", "I", "d", "R"]
]

up = "U"
down = "D"
left = "L"
right = "R"
encoded_file = "encoded.txt"

line = 1
with open(encoded_file, "r") as file:
    while True:
        readed = file.readline()
        if len(readed) == 0:
            break
        sr = 0
        sl = 0
        su = 0
        sd = 0
        for i in readed:
            if i == right:
                sr += 1
            elif i == left:
                sl += 1
            elif i == up:
                su += 1
            elif i == down:
                sd += 1
        x = (sr - sl) % 11
        y = (sd - su) % 6
        print(matrix[x][y], end="")
        line += 1

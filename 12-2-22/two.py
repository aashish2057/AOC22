import fileinput


rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6
total = 0
with fileinput.input(files=("input.txt")) as file:
    for line in file:
        line = line.strip()
        answers = line.split(" ")
        if answers[1] == "X":
            total += lose
            if answers[0] == "A":
                total += scissors
            elif answers[0] == "B":
                total += rock
            elif answers[0] == "C":
                total += paper
        elif answers[1] == "Y":
            total += draw
            if answers[0] == "A":
                total += rock
            elif answers[0] == "B":
                total += paper
            elif answers[0] == "C":
                total += scissors
        else:
            total += win
            if answers[0] == "A":
                total += paper
            elif answers[0] == "B":
                total += scissors
            elif answers[0] == "C":
                total += rock

        
print(total)
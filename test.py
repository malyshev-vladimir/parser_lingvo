with open('words.csv','r') as file:
    lines = file.readlines()
    lines = lines[amount:]
    print(lines)
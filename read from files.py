dict = {}
with open("names.txt", "r") as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line in dict:
            dict[line] += 1
        else:
            dict[line] = 1
        line = open_file.readline()

print(dict)

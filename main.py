import subprocess

number_of_ok = 0

linesf1 = []  # readed from file opisanie
linesf2 = []  # readed from file input

lists = []  # edited list of inputs
f1 = open("opisanie.txt")
f2 = open("input.txt")

a = "name: "
b = "i: "
c = "o: "
linesf1 = f1.readlines()
linesf2 = f2.readlines()

# read files
linesf2 = [line.rstrip() for line in linesf2]  # deletes '\n'
linesf2 = [line.split(' ') for line in linesf2]
for x in linesf2:
    if x[0] != '':  # to avoid RE caused by '' lines
        xf = [int(i) for i in x]
        lists.append(xf)

# parsing executable file name, number of inputs, number of outputs
name_exe = linesf1[-3].strip().split(" ")[-1]
number_of_inputs = len(linesf1[-2].strip().split(" ")[1:])
number_of_outputs = len(linesf1[-1].strip().split(" ")[1:])

inputs = []
outputs = []

for i in lists:
    inputs.append(i[0:len(i) - number_of_outputs])
    outputs.append(i[number_of_inputs:])

path_to_exe = 'C:/2pythonproj/dsaAssignment/build/exe.win-amd64-3.6/' + name_exe
for i in range(len(lists)):
    outputs_runtime = []

    process = subprocess.Popen([path_to_exe, '-i'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    for j in range(number_of_inputs):
        process.stdin.write((str(inputs[i][j]) + "\n").encode())
        process.stdin.flush()

    for j in range(number_of_outputs):
        outputs_runtime.append((process.stdout.readline().strip().decode()))

    process.stdin.close()
    process.stdout.close()
    process.terminate()
    process.wait(timeout=0.2)

    for j in range(number_of_outputs):
        if outputs[i][j] == int(outputs_runtime[j]): #neponyatno kak sravnivat esli ne int
            number_of_ok += 1

print(" tested file:", name_exe + "\n",
      "number_of_inputs:", number_of_inputs, "\n",
      "number_of_outputs:", number_of_outputs, "\n",
      "tests passed ok:", number_of_ok / len(lists) * 100, "%")

print("done")


# s = s.replace('\\', ' ') nado dobavit ko vsem inputam i outputam

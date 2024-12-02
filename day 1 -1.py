numbersfile = open("numbers.txt", "r")

line1 = []

line2 = []

difference = 0

i = 0

for line in numbersfile:
    number = line.split()
    line1.append(int(number[0]))
    line2.append(int(number[1]))
    
line1 = sorted(line1)
line2 = sorted(line2)

while i < len(line1):
    if line1[i] > line2[i]:
        difference += line1[i] - line2[i]
    else:
        difference += line2[i]-line1[i]
    i +=1

print(difference)


numbersfile = open("numbers.txt", "r")

line1 = []

line2 = []

similarity = 0

i = 0
howmany = 0

for line in numbersfile:
    number = line.split()
    line1.append(int(number[0]))
    line2.append(int(number[1]))
    
line1 = sorted(line1)
line2 = sorted(line2)

while i < len(line1):
    howmany = line2.count(line1[i])
    howmany = howmany * line1[i]
    similarity = similarity + howmany
    i += 1

print(similarity)

#this one took me 7 minutes letss gooooooooooooo

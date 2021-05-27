
input = open('passwords.txt', 'r').read().split()


#Split the range of given letter in a list at index 0 and 1 (MUST INCREMENT BY 3s for ranges


#Remove colon from 2nd entry
# print(input[1].replace(':' , ''))

#password does not need to be formatted
#print(input[2])


# print(len(input))

validPasswords = []

ranges = []
letter = []
currentPassword = []
totalValidPasswords = 0
for i in range(0, 9, 3):
    ranges.append((input[i].split('-')))
    letter.append((input[i+1].replace(':', '')))
    currentPassword.append((input[i+2]))

#get individual password
# print(len(currentPassword))

for x in range(len(ranges)):
    # print('Current Password ', currentPassword[x])
    hit = 0

    #gets the individual letters
    for y in range(0,len(currentPassword[x])):
        # print(currentPassword[x][y])

        if (letter[x] == currentPassword[x][y]):
            # print('IN HERE _______')
            hit +=1
            # print('Hit Recorded')

    if (hit <=  int(ranges[x][1] )) and hit >= int(ranges[x][0] ):
        totalValidPasswords +=1

print('Total Valid Passwords: ', totalValidPasswords)

updatedValidPassword = []
for x in range(len(ranges)):
    range1 = int(ranges[x][0])
    range2 = int(ranges[x][1])
    range1 =-1
    range2 =-1
    if(letter[x] == currentPassword[x][range1] is not letter[x] == currentPassword[x][range2] ):
        print('Target: ', letter[x])
        print('Range 1', currentPassword[x][range1])
        print('Range 2', currentPassword[x][range2])
        updatedValidPassword.append(currentPassword)
    print('-----------------------------')
print(len(updatedValidPassword))
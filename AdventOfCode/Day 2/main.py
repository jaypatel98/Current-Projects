
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
for i in range(0, 3000, 3):
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

updatedValidPassword = 0
for x in range(len(ranges)):
    range1 = int(ranges[x][0])
    range2 = int(ranges[x][1])
    print('Range 1', currentPassword[x][range1])
    print('Range 2', currentPassword[x][range2])
    # if(letter[x] == currentPassword[x][range1] or letter[x] == currentPassword[x][range2] ):
    #     print(updatedValidPassword)

print(updatedValidPassword)
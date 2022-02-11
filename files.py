# filevar = open("filename.txt", "r")

# outfile = ""

# for line in range(1,10):
#     if line % 2 == 0:
#         outfile += filevar.readline()
#     else:
#         filevar.readline()


# filevar = open("filename.txt", "w")
# filevar.write(outfile)
# filevar.close()
        

file = open("teams.txt", "r")

line = file.readlines()
print(line[0] + line[3])

file.close()



# for line in range(number_of_lines):
#     line = file.readline()
#     print(line)
        


# filecontents =filevar.read()
# filevar.close()
# print(filecontents)

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
        
file = open("Teams.txt")
filecontent = file.read()
print(filecontent)

# for line in range(1,6):
#     if line == 1:
#         print(filecontent)
#     elif line == 4:
#         print(filecontent)     




# filecontents =filevar.read()
# filevar.close()
# print(filecontents)

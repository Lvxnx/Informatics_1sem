inp = input()

palindrome_flag = 0
mirror_string_flag = 1

mirror_inp = ""
rever_inp = ""

for i in range(len(inp)):
    rever_inp = inp[i] + rever_inp

    if inp[i] not in "AHIMOTUVWXY18EJSZ3L25":
        mirror_string_flag = 0
    elif inp[i]=="E":
        mirror_inp = "3" + mirror_inp
    elif inp[i]=="J":
        mirror_inp = "L" + mirror_inp
    elif inp[i]=="S":
        mirror_inp = "2" + mirror_inp
    elif inp[i]=="Z":
        mirror_inp = "5" + mirror_inp
    elif inp[i]=="5":
        mirror_inp = "Z" + mirror_inp
    elif inp[i]=="2":
        mirror_inp = "S" + mirror_inp
    elif inp[i]=="L":
        mirror_inp = "J" + mirror_inp
    elif inp[i]=="3":
        mirror_inp = "E" + mirror_inp
    else: mirror_inp = inp[i] + mirror_inp

if rever_inp==inp:
    palindrome_flag = 1

if mirror_inp==inp:
    mirror_string_flag = 1

if palindrome_flag == 1 and mirror_string_flag == 1:
    print(inp + " is a mirrored palindrome.")
elif palindrome_flag == 0 and mirror_string_flag == 1: 
    print(inp + " is a mirrored string.")
elif palindrome_flag == 1 and mirror_string_flag == 0: 
    print(inp + " is a regular palindrome.")
else:
    print(inp + " is not a palindrome.")
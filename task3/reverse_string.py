def reverse_string(text):
    file = open("task2.txt","w")
    str= text # initial string
    stringlength=len(str) # calculate length of the list
    reverse_string=str[stringlength::-1] # reverse
    print(str)
    print(reverse_string) # print the reversed string
    file.write(str)
    file.write(reverse_string)
    file.close
a_list = ["abc", "def", "ghi"]
textfile = open("devices.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()
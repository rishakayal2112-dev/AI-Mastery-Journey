#creating file
file = open("sample_FH.txt","w")
file.write("File handling code creating and testing")
file.close()

#display
file = open("sample_FH.txt","r")
print(file.read())
file.close()

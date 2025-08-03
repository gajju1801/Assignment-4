try:
    file1=open("sample.txt","r")
    print("reading file content: ")
    print(file1.read())
    file1.close()
except FileNotFoundError:
   print("Error: The file 'sample.txt' was not found.")


#Open a file in read mode
with  open("example.txt", "r") as file:
    content = file.read()
    print(content)

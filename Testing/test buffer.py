msg = "hello, I am Robert"
# msg += "\n"

buffer = ""
buffer += msg

pos = buffer.find("\n")
print(pos)
while pos > -1:
    message = buffer[:pos]
    print(message)
    buffer = buffer[pos+1:]
    print(buffer)
    break

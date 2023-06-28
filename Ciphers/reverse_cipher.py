message = "My name is esty"
i = len(message)-1
transalated = ""

while i >= 0:
    transalated = transalated + message[i]
    i -=1

print(transalated)

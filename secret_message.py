##MESSAGE ENCODING

##input message here
message1 = input("Type your message here: ")


##message in being encoded in ASCII value
##and stored in variable   ""encoded""

encoded = ""
for i in message1:
    encoded = encoded + str(ord(i)).zfill(3)

##encoded message is being printed
print ("The encoded message: ",encoded)


##MESSAGE DECODING

message2 = input("Copy and Paste the encoded message here: ")       ##the encoded message
v = len(message2)        ##length of the encoded message
decoded = ""              ##"decoded" is the variable where decoded message is stored
x = 0
y = 3
## encoded message is being decoded
while (x < v):
    split = int(message2[x:y])
    decoded = decoded + chr(split)
    x = x + 3
    y = y + 3

print ("The decoded message: ",decoded)

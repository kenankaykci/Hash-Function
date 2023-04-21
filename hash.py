import hashlib
import base64

message = input('Please enter string data:\n')
selection = int(input('Please select wanted process:\n For Encode = 1 For Decode = 2\n'))

if (selection == 1):

    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
elif (selection == 2):
    base64_bytes = message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(message)
else :
    print('Please type your selection correctly')
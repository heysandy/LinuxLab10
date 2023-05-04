import sys

#This function encrypts the message with a ceaser key.
def encode(message: str, key: int)-> str:
    message = message.upper()
    fin_message = ""
    num = 0
    for i in message:
        ordd = ord(i)
        if ordd < 65 or ordd > 90:
            continue
        if num%50 == 0 and len(fin_message) != 0:
            fin_message += "\n"
        elif num%5 == 0 and len(fin_message) != 0:
            fin_message += " "
        fin_message += chr(65 + (ord(i)-65+key) % 26)
        num += 1
    return fin_message


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print("invalid input")
        sys.exit(1)
    
    key = int(sys.argv[1])
    
    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        message = sys.stdin.read()

    print(encode(message, key))
    sys.exit(0)
import sys
import binascii

def main():
    print("[*] This script is used to solve challenges for cryptopals")
    if (len(sys.argv) <= 1):
        print("[*] Arguments are required to run this script")
        printUsage()
        exit(0)
    elif sys.argv[1] == "challenge1":
        challenge1()
    elif sys.argv[1] == "challenge2":
        #challenge2()
        print("Currently working on it still... Come back later!")
    else:
        printUsage()
        exit(0)

def printUsage():
    print("[*] Usage: ")
    print("\t[*] To solve challenge 1 for Set 1 use:")
    print("\t\t[*] python " + sys.argv[0] + " challenge1")
    print("\t[*] To solve challenge 2 for Set 1 use:")
    print("\t\t[*] python " + sys.argv[0] + " challenge2")

def challenge1():
    user_in = input("Enter hex string to solve: ")
    if user_in != "":
        print("[*] User input: {}".format(user_in))
        user_raw = binascii.unhexlify(user_in)
        print("[*] Actual value: {}".format(user_raw))
        user_base64 = binascii.b2a_base64(user_raw)
        print("[*] Base64 encoded: {}".format(user_base64))
    else:
        print("[*] Nothing was provided. Ending program.")
        exit(0)

def challenge2():
    user_in1 = input("Please enter the hex string to decode: ")
    user_in2 = input("Please enter the string to XOR against: ")
    if user_in1 != "" and user_in2 != "":
        user_raw = binascii.unhexlify(user_in1)
        print("[*] decrypted hex value for input 1: {}".format(user_raw))
        user_in2_hex = binascii.a2b_hex(user_in2)
        user_in1 = binascii.a2b_hex(user_raw)
        xor_result = user_in1 ^ user_in2_hex
        print("[*] XOR results: {}".format(xor_result))
    else:
        print("[*] One of the fields was left blank. Ending the program.")
        exit(0)

if __name__ == "__main__":
    main()

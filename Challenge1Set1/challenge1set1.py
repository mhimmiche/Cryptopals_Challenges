import sys
import binascii


if len(sys.argv) <= 1:
    print("[*] Error, there must be an argument provided")
    print("[*] This script takes in a hex string, decodes it, and converts it to base64")
    print("[*] Usage: python " +  sys.argv[0] + " <hexToDecode>")
else:
    user_in = sys.argv[1]
    print("User input: {}".format(user_in))
    user_raw = binascii.unhexlify(user_in)
    print("Actual value: {}".format(user_raw))
    user_base64 = binascii.b2a_base64(user_raw)
    print("Base64 encoded: {}".format(user_base64))

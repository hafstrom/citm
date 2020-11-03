import os
from os import system, name

print("If you didn't wish to exit, then something went wrong!")
def main():
    a = input(" > Type 'ok' to close this window: ")
    a = a.lower()

    if a == 'ok':
        exit(0)

    else:
        main()
main()
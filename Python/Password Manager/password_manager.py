from cryptography.fernet import Fernet


def main():
    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (View, Add)? Q to Quit :").lower()
        if mode == "q":
            break
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid Mode")
            continue


def view(fer):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add(fer):
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


main()

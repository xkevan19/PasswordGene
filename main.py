import secrets
import string as str


class PasswordGenerator:

    @staticmethod
    def gen_sequence(
            conditions):  # must have  conditions (in a list format), for each member of the list possible_characters
        possible_characters = [str.ascii_lowercase, str.ascii_uppercase, str.digits, str.punctuation]
        sequence = ""
        for x in range(len(conditions)):
            if conditions[x]:
                sequence += possible_characters[x]
            else:
                pass
        return sequence


def gen_password(sequence, passlength=8):
    password = ''.join((secrets.choice(sequence) for _ in range(passlength)))
    return password


class Interface:
    has_characters = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True
    }

    @classmethod
    def change_has_characters(cls, change):
        # noinspection PyBroadException
        try:
            cls.has_characters[change]
            # to check if the specified key exists in the dictionary
        except:
            print("Invalid")
        else:
            cls.has_characters[change] = not cls.has_characters[
                change]  # automatically changes to the opposite value already there
            print(f"{change} is now set to {cls.has_characters[change]}")

    @classmethod
    def show_has_characters(cls):
        print(cls.has_characters)  # print the output

    def generate_password(self, length):
        sequence = PasswordGenerator.gen_sequence(list(self.has_characters.values()))
        print(gen_password(sequence, length))


def list_to_vertical_string(list):
    to_return = ""
    for member in list:
        to_return += f"{member}\n"
    return to_return


class Run:

    # noinspection PyBroadException
    def decide_operation(self):
        user_input = input("Enter the amount of characters for your desired passwords: ")
        try:
            int(user_input)
        except:
            Interface.change_has_characters(user_input)
        else:
            print("This is your new password: \n")
            Interface().generate_password(int(user_input))
            print("\nEnjoy!")
        finally:
            print("\n\n")

    def run(self):
        menu = \
            f"""\nWelcome to GetPassEasy App!
\nThe following commands can be used to modify the outcome of your generated password, good luck!
COMMANDS to modify output:\n
{list_to_vertical_string(Interface.has_characters.keys())}
            """
        print(menu)
        while True:
            self.decide_operation()


Run().run()

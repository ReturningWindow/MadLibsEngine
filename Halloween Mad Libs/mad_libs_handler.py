class MadLibsHandler:

    COMMANDS = ["NOUN", "VERB", "ADJECTIVE", "DONE"]

    def __init__(self, name, script, commands=[]):
        self.name = name
        self.script = script
        self.command = None
        self.missing_word_count = self.script.count("{}")
        self.registered_commands = commands
        self.words = {}

    def set_commands(self, commands):
        self.registered_commands = commands

    def create_mad_libs(self):
        print(
            "The valid commands here are NOUN, VERB, ADJECTIVE, and DONE. You can get plurals by adding s to the commands that aren't DONE"
        )
        while self.command != (len(self.commands) - 1):
            self.command = input("Enter a command: ")
            if len(self.command) > 0:
                sef.registered_commands.append(self.command.lower())
            else:
                print("Invalid command! Please ACTUALLY enter a command or enter DONE")

        print("Commands registered!")

    def play_mad_libs(self):
        for index, command in enumerate(self.registered_commands):
            match command:
                case "noun":
                    word = input("Enter a noun: ")
                case "verb":
                    word = input("Enter a verb: ")
                case "adjective":
                    word = input("Enter an adjective: ")
                case "adverb":
                    word = input("Enter an adverb: ")
                case "nouns":
                    word = input("Enter a plural noun: ")
                case "done":
                    raise Exception(f"Invalid {command} registered in commands.")
                case "":
                    raise Exception(f"No command received for commands.")
                case _:
                    word = input(f"Enter a {command}: ")

            if word == "":
                print("Please enter something into the things listed before!")
                index = index - 1 if index != 0 else 0
            else:
                self.words[index + 1] = word

    def get_mad_libs(self):
        return self.script.format(*self.words.values())

class MadLibsHandler:

    COMMANDS = ["NOUN", "VERB", "ADJECTIVE", "DONE"]

    def __init__(self, name, script, commands=[]):
        """Creates a MadLibsHandler object

        Parameters:
        name: str
            The name of the mad libs.

        script: str
            The text of the mad libs game.

        commands: list of str, optional
            The commands registered for the game to play.
        """
        self.name = name
        self.script = script
        self.command = None
        self.missing_word_count = self.script.count("{}")
        self.registered_commands = commands
        self.words = {}

    def set_commands(self, commands):
        """Overrides the preivous commands with new commands.


        Parameters:
            commands: list of str
            A list of commands for the writers of the game.

        Returns:
            None
        """
        self.registered_commands = commands

    def create_mad_libs(self):
        """Allows a creator to input a list of commands manually until DONE is typed.

        Parameters:
            None

        Returns:
            None
        """
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
        """Allows the player to play a game of madlibs

        Parameters:
            None

        Raises:
            Exception #1
                If command "DONE" is read into the commands it will break the program.

            Exception #2
                If there is no command to give, then it will break the program and not proceed.
        Returns:
            None
        """

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
                    raise Exception(f"No command received for this entry.")
                case _:
                    word = input(f"Enter a {command}: ")

            if word == "":
                print("Please enter something into the things listed before!")
                index = index - 1 if index != 0 else 0
            else:
                self.words[index + 1] = word

    def get_mad_libs(self):
        """Gets the end result of the game for the user.

        Parameters:
            None

        Returns
            str
                A script full of what the user inputted into your game of mad libs.
        """

        return self.script.format(*self.words.values())

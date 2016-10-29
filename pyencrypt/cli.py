import os.path
from textwrap import dedent

class PyencryptCLI:
    def __init__(self, arguments):
        self.arguments = arguments

    def parse(self):
        if self.correct_usage() == False:
            self.print_usage()
            exit(0)

        self.encrypt = self.arguments[1] == '-e'
        self.in_file = self.arguments[2]
    
    def correct_usage(self):
       return self.enough_arguments() and self.correct_option() and self.input_file_exists() 

    def enough_arguments(self):
       return len(self.arguments) == 3

    def correct_option(self):
        return self.arguments[1] == '-e' or self.arguments[1] == '-d'

    def input_file_exists(self):
        return os.path.isfile(self.arguments[2])

    def print_usage(self):
        usage = """
        Usage:
            pyencryt OPTION IN_FILE

            Options:
                -d      Decrypt the IN_FILE
                -e      Encrypt the IN_FILE 
        """
        
        print(dedent(usage))

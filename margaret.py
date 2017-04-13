import pickle
import sys

global file_name
# global action

class Margaret():
    """ """

    def __init__(self, name):
        """ """
        self.name = name

    def log(message):
        """Log a message to the log file
        """
        with open('messages.txt', a) as file:
            file.write(str(message))


    if __name__ == "__main__":
        try:
            file_name = sys.argv[1]
            action = sys.argv[2]

        if action == r:
            read_log()
        elif action == w or action == a:
            log( .join(sys.argv[3:]), action)
        except IndexError:
            pass

#####################3
def __init__(self):
    self.all_notes = []
    try:
        self.all_notes = self.deserialize()
    except FileNotFoundError:
        pass

def list_notes(self):
    for key,note in enumerate(self.all_notes):
        print(str(key) + ": " + note)

def serialize(self):
    with open(notes.txt, wb) as file:
        pickle.dump(self.all_notes, file)

def deserialize(self):
    try:
        with open(notes.txt, rb) as file:
            self.all_notes = pickle.load(file)
    except EOFError:
        pass

return self.all_notes
#NOUNS: Mary class, mary list, message = command line message, dict_name[name] = message, messages.txt, 
#   FileNotFoundError, EOFError, KeyError
#VERBS: create 3 files, READ command line message; STORE that message as a value in a dict, STORE that dict 
#   in messages.txt; RETRIEVE that value from messages.txt; PRINT message in the terminal,

import pickle
import sys

class Mary():
    """
    The Class for Mary that allows the user to save and retrieve her messages 

    Methods:
    log
    serialize
    deserialize

    """

    def __init__(self):
        """
        Creates the dict and list for Mary's storage.
        Also, it tries to deserialize

        """

        self.info = {}
        self.mary_list = []

        try:
            self.info = self.deserialize()         #TRY to SAVE the dict
        except FileNotFoundError:
            pass


    def log(self):
        """Stores the message into the value in a dict"""

        self.mary_list.append(sys.argv[1:])
        self.info['Mary'] = self.mary_list
        self.serialize()

    def serialize(self):
        """ Writes/serializes message to file"""

        with open('messages.txt', 'wb') as file:
            pickle.dump(self.info, file)

    def deserialize(self):
        """ Reads/deserializes message from file"""

        try:
            with open('messages.txt', 'rb') as file:
                self.info = pickle.load(file)
        except (EOFError, KeyError):
            pass

        print(self.info)
        #print(self.mary_list)

        return self.info
        return self.mary_list['Mary']


if __name__ == '__main__':
    mary = Mary()
    mary.log()
    mary.serialize()
    mary.deserialize()
#NOUNS: Margaret class, margaret list, message = command line message, dict_name[name] = message, messages.txt, 
#   FileNotFoundError, EOFError, KeyError
#VERBS: create 3 files, READ command line message; STORE that message as a value in a dict, STORE that dict 
#   in messages.txt; RETRIEVE that value from messages.txt; PRINT message in the terminal,
#I don't know where to put the Key error

import pickle
import sys

class Margaret():
    """
    The Class for Margaret that allows the user to save and retrieve her messages 

    Methods:
    log
    serialize
    deserialize

    """

    def __init__(self):
        """
        Creates the dict and list for Margaret's storage.
        Also, it tries to deserialize

        """

        self.info = {}
        self.marg_list = []

        try:
            self.info = self.deserialize()         #TRY to SAVE the dict
        except FileNotFoundError:
            pass


    def log(self):
        """Stores the message into the value in a dict"""

        self.marg_list.append(sys.argv[1:])
        self.info['Margaret'] = self.marg_list
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
        #print(self.marg_list)

        return self.info
        return self.marg_list['Margaret']

if __name__ == '__main__':
    margaret = Margaret()
    margaret.log()
    margaret.serialize()
    margaret.deserialize()
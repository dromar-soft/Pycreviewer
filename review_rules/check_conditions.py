import json

class CheckConditions():
    """
    CheckConditions class provide functions to decode JSON file 
    and refer to the setting conditions of various check rules.
    """
    def __init__(self, file_path:str):
        io = open(file_path, 'r')
        self.json = json.load(io)

    def isInvalid(self)->bool:
            return True

import json

class CheckConditions():
    """
    CheckConditions class provide functions to decode JSON file 
    and refer to the setting conditions of various check rules.
    """
    def __load__(self, file_path:str):
        io = open(file_path, 'r')
        self.json_dict= json.load(io)
        io.close()

    def __init__(self, file_path:str):
        self.__load__(file_path)

    def Version(self):
        if 'version' in self.json_dict:
            return self.json_dict["version"]
        else:
            return ''

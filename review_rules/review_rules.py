class ReviewResult(object):
    def __init__(self, id, level, msg, coord):
        self.id = id
        self.level = level
        self.msg = msg
        self.coord = coord

    def output_str(self):
        return vars(self)

class ReviewRules(object):
    """
    ReviewRules class provide code check function by using ast_analyser object.
    The condition parameters of each code check item are set by reading the JSON file. 
    """
    def __init__(self, ast_analyser):
        self.ast_anaylser = ast_analyser

    def check(self):
        results = []
        results.append(ReviewResult("dummy", "WARN", "testtest", "./examples/c_files/xxxx.c::7::12"))
        return results

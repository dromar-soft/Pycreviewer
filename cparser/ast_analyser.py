from pycparser import c_ast

class AstAnalyser(object):

    def __init__(self, ast):
        print("AstAnalyser Obj Created.")
        self.ast = ast

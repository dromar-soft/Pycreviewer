from pycparser import c_ast

class SourceCode(object):
    """
    SourceCodeクラスは、ソースコード情報を抽象化し、各要素にアクセスする機能を提供する。
    SouceCodeクラスは、pycparser.parse()によって生成されたc_astオブジェクトを利用する。
    """

    def __init__(self, ast):
        print("AstAnalyser Obj Created.")
        self.ast = ast

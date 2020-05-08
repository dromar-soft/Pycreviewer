# coding: UTF-8
from cparser import c_parser_wrapper,ast_analyser

if __name__ == "__main__":

    print("pycreviewer start")
    
    ast = c_parser_wrapper.parse("./examples/c_files/memmgr.c")
    analyser = ast_analyser.AstAnalyser(ast)
    
    print("pycreviewer end")

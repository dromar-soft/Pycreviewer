# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# pycreviewer: source_file_parser.py
# Dromar [https://github.com/dromar-soft]
# License: MIT
#------------------------------------------------------------------------------
from pycparser import parse_file, c_generator, c_ast
import os

def parse(filepath:str, cpp_args:list):
    """
    Parse c source file by pycparser, and return AST object.
    """
    ast = parse_file(filepath, use_cpp=True,
                        cpp_path='gcc',
                        cpp_args=cpp_args)
    return ast
    
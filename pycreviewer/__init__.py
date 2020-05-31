# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# pycreviewer: __init__.py
# Dromar [https://github.com/dromar-soft]
# License: MIT
#------------------------------------------------------------------------------
#print("pycreviewer imported")
from .source_file_parser import parse
from .source_code import SourceCode
from .check_conditions import CheckConditions
from .coding_rules import CodinfgRules

def review_file(sourcefile: str, cpp_args=['-E', r'-Ipycreviewer/utils/fake_libc_include'], jsonfile='./default.json') ->list:
    """
    Perform code review on a single source file.
    The result of the code review is returned in the form of List<CheckResult>.
    sourcefile:
        the target source file path.
    cppargs:
        a list of command line arguments for the preprocessor execution of C compiler.
        Normally, specifies the preprocessor execution option '-E' and the include option '-Ixxxxx'.
    jsonfile:
        JSON file path describing the checking conditions for coding rules.
    """
    #print("Executing: "+filepath)
    ast = parse(filepath=sourcefile,cpp_args=cpp_args)
    code = SourceCode(ast)
    rules = CodinfgRules(code, CheckConditions(jsonfile))
    results = rules.check_all()
    return results
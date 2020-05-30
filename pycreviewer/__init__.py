#print("pycreviewer imported")

from .source_file_parser import parse
from .source_code import SourceCode
from .check_conditions import CheckConditions
from .coding_rules import CodinfgRules

def review_file(filepath: str, cpp_args=['-E', r'-Ipycreviewer/utils/fake_libc_include']) ->list:
    """
    Perform code review on a single source file.
    The result of the code review is returned in the form of List<CheckResult>.
    Enter the target source file path in the 'filepath' field.
    The 'cppargs' is a list of command line arguments for the preprocessor execution of C compiler.
    Normally, 'cppargs' specifies the preprocessor execution option '-E' and the include option '-Ixxxxx'.
    """
    #print("Executing: "+filepath)
    ast = parse(filepath=filepath,cpp_args=cpp_args)
    code = SourceCode(ast)
    rules = CodinfgRules(code, CheckConditions('./default.json'))
    results = rules.check_all()
    return results
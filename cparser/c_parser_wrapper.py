from pycparser import parse_file, c_generator, c_ast

def parse(filepath):
    ast = parse_file(filepath, use_cpp=True,
                        cpp_path='gcc',
                        cpp_args=['-E', r'-Iutils/fake_libc_include'])
    return ast
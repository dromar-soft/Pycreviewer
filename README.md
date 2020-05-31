# Pycreviewer
 
pycreviewer is a coderewview tool of C source code in Python.
pycreivewer can do simple and mechanical code reviews on your behalf that people don't have to do.
This way, developers don't have to deal with reviewers pointing out simple mistakes, and
The reviewer can focus on the essential review.

# Design

![](https://raw.githubusercontent.com/dromar-soft/Pycreviewer/images/architecture.png)
 
# Features

## Coding rules

### Static variable name prefix
### Global variable name prefix
### Too short variable name
### Recursive call
### Function blacklist
### No break statement in the switch-case statement
### No default statement in switch statement

## Check conditions of coding rules(JSON file)

```
{
    "version": "0.1.0",
    "conditions":{
        "static_variable_prefix":{
            "id":"R001",
            "param":"m_",
            "level":"SHOULD"
        },
        "global_variable_prefix":{
            "id":"R002",
            "param":"g_",
            "level":"SHOULD"
        },
        "variable_short_name":{
            "id":"R003",
            "param":2,
            "level":"MUST"
        },
        "recursive_call":{
            "id":"R004",
            "param":true,
            "level":"MUST"
        },
        "function_blacklist":{
            "id":"R005",
            "param":[
                "malloc",
                "free"
            ],
            "level":"WANT"
        },
        "no_break_in_switch":{
            "id":"R006",
            "param":true,
            "level":"SHOULD"
        },
        "no_default_in_switch":{
            "id":"R007",
            "param":true,
            "level":"SHOULD"
        }
    }
}

```

# Requirement
 
* pycreviewer was tested on Python 3.8.2. 
* pycparser 2.2.0(https://github.com/eliben/pycparser)
 
# Installation

```bash 
git clone https://github.com/dromar-soft/Pycreviewer.git
```

# Usage
 
## Using simple cui application.

1. Run the pycreviewer module.    
2. Enter your source code directory.
3. The review result is output to the console.
4. The application is terminated by entering Esc.

    ```bash
    python -m pycreviewer
    input source folder >> 'your sourcecode directory'
    {'id': 'R006', 'level': 'SHOULD', 'msg': 'No break statement in switch-case statement.', 'file': '/xxx/xxx/xxx.c', 'line': X, 'column': X}
    {'id': 'R007', 'level': 'SHOULD', 'msg': 'No default statement in switch-case statement.', 'file': '/xxx/xxx/xxx.c', 'line': X, 'column': Y}
    ...
    ...
    ...
    X files codereview completed. Please enter esc key.
    ```
 
 ## Using as a library

You can perform a code review on a single source file by calling pycreviewer.review_file().

```python
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
```    
# Note
 
* For parsing of C source code, this library runs the C compiler's preprocessor (gcc -E) .
Therefore, you need to remove compile errors in the target source code in advance.

 
# License
 
pycreviewer is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
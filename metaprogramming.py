"""
Assignment 4: Metaprogramming

The idea of this assignment is to get you used to some of the dynamic
and functional features of Python and how they can be used to perform
useful metaprogramming tasks to make other development tasks easier.
"""

import functools
import sys
import string

def logcalls(prefix):
    """A function decorator that logs the arguments and return value
    of the function whenever it is called.

    The output should be to sys.stderr in the format:
    "{prefix}: {function name}({positional args}..., {keyword=args}...)" 
    and 
    "{prefix}: {function name} -> {return value}"
    respectively for call and return. The call line should
    be printed before the call and the return line after.
    This is important for recursive functions (it will make 
    the call and return lines show the actual nested 
    structure of the recursion).

    Look up functools.wraps and use it to make the function you return
    have the same documentation and name as the function passed in.

    This will be used like:
    @logcalls("test")
    def f(arg):
        return arg

    NOTE: Do not generate and then modify strings. Instead generate
    the string you wanted directly. Look at str.join and keep
    generator comprehensions in mind. Also look at str.format.
    """
    def log(prefix):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                arg_list = []

                output = "{prefix}: {func_name}(".format(prefix=prefix, func_name=func.__name__)

                # get positional args
                arg1 = ', '.join(repr(p) for p in args)
                arg_list.append(arg1)

                # get key word args
                arg2 = ', '.join(key + '=' + repr(value) for key, value in kwargs.items())
                arg_list.append(arg2)

                # print out calls and args
                output += ', '.join(filter(None, arg_list)) + ')\n'
                sys.stderr.write(output)

                ret_value = func(*args, **kwargs)

                # print out return values
                output = "{prefix}: {func_name} ".format(prefix=prefix, func_name=func.__name__)
                output += '-> ' + (repr(ret_value))
                sys.stderr.write(output + '\n')

                return ret_value
            return wrapper
        return decorator
    return log(prefix)





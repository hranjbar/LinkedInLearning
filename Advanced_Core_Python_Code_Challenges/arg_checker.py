from functools import wraps

def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
        - The number of variables that you use for a function
        - The type of each variable.
       Raises a TypeError if either of these fail''' 
    def decorator(f):
        @wraps(f)
        def wrapper(*args):
            assert len(args) == len(arg_types)
            if len(args) != len(arg_types):
                raise(TypeError(f"Wrong number of input arguments!"))
            for arg, arg_type in zip(args, arg_types):
                if isinstance(arg, arg_type):
                    raise(TypeError(f"Wrong type of input!"))
            return wrapper
        return decorator
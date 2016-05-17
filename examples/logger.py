"""A decorator which logs"""
def logthis(log_msg="", severity="INFO"):  # Decorators with two positional parameters
    def real_decorator(func):
        def wrapper(*args, **kwargs):  # Wrapper-closure wraps the function
            data = func(*args, **kwargs)  # Execute decorated function and get returned values
            print("Hello from inside your decorator, i can see: {}".format(locals()))
            print("{}: {}".format(severity, log_msg))
            return data
        return wrapper
    return real_decorator

@logthis("Main function called", "WARN")
def main():
    return "Did some fancy stuff"


if __name__ == '__main__':
    main()

import re


email_re = re.compile(r'''
    (^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*  # dot-atom
    |^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"  # quoted string
    )@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$  # domain.tld
''', re.IGNORECASE | re.VERBOSE)

def save(obj):
    return "i saved your stuff"

"""A decorator which validates email addresses"""
def validate_email(func):  # Decorator receives function as param
    def wrapper(*args, **kwargs):  # Wrapper-closure wraps the function
        print("Hello from inside your decorator, i can see: {}".format(locals()))
        if not email_re.match(kwargs['addr']):
            raise ValueError("Not a valid email address")
        data = func(*args, **kwargs)  # Execute decorated function and get returned values (if any)
        return data  # Maybe empty
    return wrapper

@validate_email
def save_email(addr):
    r = save(addr)
    print(dir(r))

if __name__ == '__main__':
    # save_email(addr="decorate<at>yourhome.net")
    save_email(addr="decorate@yourhome.org")

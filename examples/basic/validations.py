import re


email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

def save(obj):
    pass

"""A decorator which validates email addresses"""
def validate_email(func):  # Decorator receives function as param
    def wrapper(*args, **kwargs):  # Wrapper-closure wraps the function
        data = func(*args, **kwargs)  # Take positional and keyword params from original function
        print("Hello from inside your decorator, i can see: {}".format(locals()))
        if not email_re.match(kwargs['addr']):
            raise ValueError("Not a valid email address")
        return data
    return wrapper

@validate_email
def save_email(addr):
    save(addr)


if __name__ == '__main__':
    save_email(addr="decorate<at>yourhome.net")
    #save_email(addr="decorate@yourhome.net")

# Understanding Python decorators

A little demo repository helping me to learn writing decorators. [PEP 318][PEP0318]
describes decorators and their design. This repository is a hands on approach to
decorators.

## Need to know

In order to "wrap a function" inside the decorator code, we use closures like this:

    def make_printer(msg):
        def printer():
            print msg  # Closure: accessing the outer scope's variable!
        return printer  # return the printer function

    printer = make_printer('Foo!')  # bind a new printer function
    printer()  # finally call the function

It is also helpful to understand unpacking lists and tuples into positional
arguments:

        """
        Remember: You can unpack a tuple or a list into positional arguments
        using a star.

        def add(a, b, c):
            print(a, b, c)
            x = (1, 2, 3)
            add(*x)

        # Similarly, you can use double star to unpack
        # a dict into keyword arguments
        x = { 'a': 3, 'b': 1, 'c': 2 }
        add(**x)
        """


[PEP0318]: https://www.python.org/dev/peps/pep-0318/

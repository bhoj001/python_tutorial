'''
hashable

    An object is hashable if it has a hash value which never changes during its 
    lifetime (it needs a __hash__() method), and can be compared to other 
    objects (it needs an __eq__() method). Hashable objects which compare equal 
    must have the same hash value.

    Hashability makes an object usable as a dictionary key and a set member, because these 
    data structures use the hash value internally.

    Most of Python’s immutable built-in objects are hashable; mutable containers 
    (such as lists or dictionaries) are not; immutable containers (such as tuples and 
    frozensets) are only hashable if their elements are hashable. Objects which are 
    instances of user-defined classes are hashable by default. They all compare 
    unequal (except with themselves), and their hash value is derived from their id().

immutable

    An object with a fixed value. Immutable objects include numbers, strings and tuples. 
    Such an object cannot be altered. A new object has to be created if a different 
    value has to be stored. They play an important role in places where a constant hash 
    value is needed, for example as a key in a dictionary.

interpreted

    Python is an interpreted language, as opposed to a compiled one, though the distinction 
    can be blurry because of the presence of the bytecode compiler. This means that source 
    files can be run directly without explicitly creating an executable which is then run. 
    Interpreted languages typically have a shorter development/debug cycle than compiled ones, 
    though their programs generally also run more slowly. See also interactive.

iterable

    An object capable of returning its members one at a time. Examples of iterables include all 
    sequence types (such as list, str, and tuple) and some non-sequence types like dict, file 
    objects, and objects of any classes you define with an __iter__() method or with a __getitem__() 
    method that implements Sequence semantics.

lambda

    An anonymous inline function consisting of a single expression which is evaluated when the function 
    is called. The syntax to create a lambda function is lambda [parameters]: expression

list comprehension

    A compact way to process all or part of the elements in a sequence and return a list with the 
    results. result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] generates a list 
    of strings containing even hex numbers (0x..) in the range from 0 to 255. The if clause is 
    optional. If omitted, all elements in range(256) are processed.

mapping

    A container object that supports arbitrary key lookups and implements the methods specified 
    in the Mapping or MutableMapping abstract base classes. Examples include dict, 
    collections.defaultdict, collections.OrderedDict and collections.Counter.

metaclass

    The class of a class. Class definitions create a class name, a class dictionary, and a list of 
    base classes. The metaclass is responsible for taking those three arguments and creating the 
    class. Most object oriented programming languages provide a default implementation. 
    What makes Python special is that it is possible to create custom metaclasses. Most users 
    never need this tool, but when the need arises, metaclasses can provide powerful, elegant 
    solutions. They have been used for logging attribute access, adding thread-safety, tracking 
    object creation, implementing singletons, and many other tasks.

method

    A function which is defined inside a class body. If called as an attribute of an instance of 
    that class, the method will get the instance object as its first argument (which is usually 
    called self). See function and nested scope.

mutable

    Mutable objects can change their value but keep their id(). See also immutable.

object

    Any data with state (attributes or value) and defined behavior (methods). Also the 
    ultimate base class of any new-style class.

bytecode

    Python source code is compiled into bytecode, the internal representation of a Python 
    program in the CPython interpreter. The bytecode is also cached in .pyc files so that 
    executing the same file is faster the second time (recompilation from source to bytecode 
    can be avoided). This “intermediate language” is said to run on a virtual machine that 
    executes the machine code corresponding to each bytecode. Do note that bytecodes are not 
    expected to work between different Python virtual machines, nor to be stable between Python 
    releases.

class

    A template for creating user-defined objects. Class definitions normally contain method 
    definitions which operate on instances of the class.

context manager

    An object which controls the environment seen in a with statement by 
    defining __enter__() and __exit__() methods. See PEP 343.

coroutine

    Coroutines are a more generalized form of subroutines. Subroutines are entered at one 
    point and exited at another point. Coroutines can be entered, exited, and resumed at 
    many different points. They can be implemented with the async def statement. See also PEP 492.

decorator

    A function returning another function, usually applied as a function transformation 
    using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

    The decorator syntax is merely syntactic sugar, the following two function definitions 
    are semantically equivalent:

    def f(...):
        ...
    f = staticmethod(f)

    @staticmethod
    def f(...):
        ...


'''
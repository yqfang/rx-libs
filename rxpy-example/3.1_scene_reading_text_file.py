from __future__ import print_function
from rx import Observable

def read_lines(file_name):
    file = open(file_name)

    return Observable.from_(file) \
        .map(lambda l: l.strip()) \
        .filter(lambda l: l != "")

read_lines("2.25_operator_group_into_lists.py").subscribe(lambda s: print(s))


# 7.2. Reading and Writing Files
# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
#
# >>>
# >>> f = open('workfile', 'w')
# >>> print f
# <open file 'workfile', mode 'w' at 80a0960>
# The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.
#
# On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'. Python on Windows makes a distinction between text and binary files; the end-of-line characters in text files are automatically altered slightly when data is read or written. This behind-the-scenes modification to file data is fine for ASCII text files, but it’ll corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files. On Unix, it doesn’t hurt to append a 'b' to the mode, so you can use it platform-independently for all binary files.
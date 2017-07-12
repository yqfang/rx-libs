from __future__ import print_function
from rx import Observable
import os

def recursive_files_in_directory(folder):

    def emit_files_recursively(observer):
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                observer.on_next(os.path.join(root, directory))
            for filename in filenames:
                observer.on_next(os.path.join(root, filename))

        observer.on_completed()

    return Observable.create(emit_files_recursively)


recursive_files_in_directory('/Users/yqfang/develop/github/open/rx') \
    .filter(lambda f: f.endswith('.js')) \
    .subscribe(on_next=lambda l: print(l), on_error=lambda e: print(e))


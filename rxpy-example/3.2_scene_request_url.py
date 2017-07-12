from __future__ import print_function
from rx import Observable
from urllib2 import urlopen

def read_request(link):
    f = urlopen(link)

    return Observable.from_(f) \
        .map(lambda b: b.decode("utf-8".strip()))
read_request("https://gist.githubusercontent.com/thomasnield/d50c61aee74aebdacf917a918eaeb71a/raw/aca53e1f458a354fa5a1bf44458c279432b8973a/year_over_year_growth.sql") \
    .subscribe(lambda line: print(line))
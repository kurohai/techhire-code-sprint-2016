#!/bin/python

def parse_next_string():
    return raw_input().strip()


def parse_next_int():
    return int(parse_next_string())


def parse_query_set():
    return [parse_next_string() for i in xrange(parse_next_int())]


def do_the_other_thing(query_set):
    stop = len(max(query_set, key=len))
    for i in xrange(stop):
        new = [c for c in query_set if len(c) > i]
        pre = [c[:i+1] for c in new]
        if len(pre) == len(set(pre)):
            return i

def filter_no_match(queryset, prefixlen):
    holder = list()
    for q in queryset:
        # remove any that dont match on prefixlen
        pass

def main():
    set_count = parse_next_int()
    for c in xrange(set_count):
        query_set = parse_query_set()
        print do_the_other_thing(query_set)


if __name__ == '__main__':
    main()

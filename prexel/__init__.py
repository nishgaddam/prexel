import re

REGEX = {
    "class_name": re.compile(r'^[A-Z]\w*$'),
    "method_signature": re.compile(r'^([^(){}]+)\((.*)\)$'),
    "aggregation": re.compile('^<>([\d*]?)-+(\w*)-*([\d*]?)>$'), # A <>-wings-> B
    "inheritance": re.compile('^<<$') # <<
}

#re.compile(r'^    $')

"""
A REGEX or regular expression is a special text string for describing a search pattern.
For example, you could use the regular expression \b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b to search for an email address.
"""

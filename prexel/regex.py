import re

REGEX = {
    "class_name": re.compile(r'^[A-Z]\w*$'),
    "class_method": re.compile(r'^[a-z]\w()*$'),
    "class_attribute": re.compile(r'^[a-z]\w*$'),
    "method_signature": re.compile(r'^([^(){}]+)\((.*)\)$'),
    "aggregation": re.compile('^<>([\d*]?)-+(\w*)-*([\d*]?)>$'),  # A <>-wings-> B 
    "inheritance": re.compile('^>>$'),  # <<
    "valid_multiplicity": re.compile('([0-9]+|\*)'),  # <>1-employees---*>
    "ignored_characters": ("<<>", "<>>", "<>", "<<>>"),
    "reserved_characters": (",", "|", "#"),
}

'''      *Aggregation Regex explanation*
^           Beginning of a String
([\d*]?)    means 0 or more digits
-+          1 or More -'s
(\w*)       means 0 or more word characters
-*          0 or More -'s
([\d*]?)    means 0 or more digits
$           End of a String
'''

def is_class_name(value):
    return REGEX["class_name"].match(value)

def is_method_signature(value):
    return REGEX["method_signature"].match(value)
 
def is_inheritance(value):
    return REGEX["inheritance"].match(value)


def is_aggregation(value):
    return REGEX["aggregation"].match(value)


def is_ignored_token(value):
    return value in REGEX["ignored_characters"]


def is_reserved_character(value):
    return value in REGEX["reserved_characters"]

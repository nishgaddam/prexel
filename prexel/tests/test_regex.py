import os
path="/Users/gaddamnitish/Library/Application Support/Sublime Text 3/Packages"
os.chdir(path)

import unittest
from prexel.regex import REGEX


class TestRegex(unittest.TestCase):
    def test_class_name_regex(self):
        class_name_regex = REGEX["class_name"]

        # These should match
        self.assertTrue(class_name_regex.match("Kitchen"))
        self.assertTrue(class_name_regex.match("Wing"))
        self.assertTrue(class_name_regex.match("Style"))
        self.assertTrue(class_name_regex.match("A"))

        # These shouldn't match
        self.assertFalse(class_name_regex.match("$Class"))
        self.assertFalse(class_name_regex.match("kitchen"))
        self.assertFalse(class_name_regex.match("Kitchen()"))
        self.assertFalse(class_name_regex.match("method()"))
        print('Test2')

    def test_class_method_regex(self):
        class_method_regex = REGEX["class_method"]

        # These should match
        self.assertTrue(class_method_regex.match("wing()"))
        self.assertTrue(class_method_regex.match("style()"))
        self.assertTrue(class_method_regex.match("a()"))

        # These shouldn't match
        self.assertFalse(class_method_regex.match("Class()"))
        self.assertFalse(class_method_regex.match("Kitchen"))
        self.assertFalse(class_method_regex.match("Kitchen()"))
        self.assertFalse(class_method_regex.match("method"))
        print('Test2')
 
    def test_class_attribute_regex(self):
        class_attribute_regex = REGEX["class_attribute"]

        # These should match
        self.assertTrue(class_attribute_regex.match("kitchen"))
        self.assertTrue(class_attribute_regex.match("wing"))
        self.assertTrue(class_attribute_regex.match("style"))
        self.assertTrue(class_attribute_regex.match("a"))

        # These shouldn't match
        self.assertFalse(class_attribute_regex.match("$Class"))
        self.assertFalse(class_attribute_regex.match("kitchen()"))
        self.assertFalse(class_attribute_regex.match("Kitchen()"))
        self.assertFalse(class_attribute_regex.match("method()"))
        print('Test2')



    def test_method_signature_regex(self):
        method_signature_regex = REGEX["method_signature"]

        # These should match
        self.assertTrue(method_signature_regex.match("sample_method()"))
        self.assertTrue(method_signature_regex.match("sample_method(param1,[])"))

        # These shouldn't match
        self.assertFalse(method_signature_regex.match("sample_method"))
        self.assertFalse(method_signature_regex.match("Sample_method"))
        self.assertFalse(method_signature_regex.match("()"))
        print('Test4')

    def test_aggregation_regex(self):
        aggregation_regex = REGEX["aggregation"]
        # weight <>-wings-> Wing
        # These should match
        self.assertTrue(aggregation_regex.match("<>-->"))
        self.assertTrue(aggregation_regex.match("<>-------->"))
        self.assertTrue(aggregation_regex.match("<>1-->"))
        self.assertTrue(aggregation_regex.match("<>*-->"))
        self.assertTrue(aggregation_regex.match("<>1--*>"))
        self.assertTrue(aggregation_regex.match("<>1--1>"))
        self.assertTrue(aggregation_regex.match("<>*--1>"))
        self.assertTrue(aggregation_regex.match("<>*--*>"))
        self.assertTrue(aggregation_regex.match("<>*-name-*>"))
        self.assertTrue(aggregation_regex.match("<>--name--->"))

        # These shouldn't match
        self.assertFalse(aggregation_regex.match("<>--"))
        self.assertFalse(aggregation_regex.match("-->"))
        self.assertFalse(aggregation_regex.match("<>&-->"))
        self.assertFalse(aggregation_regex.match("<>--&>"))
        self.assertFalse(aggregation_regex.match("<>1a--1b>"))

        # Test groupings
        matcher = aggregation_regex.match("<>1--name----*>")
        groups = matcher.groups()
        self.assertEqual(groups[0], "1")
        self.assertEqual(groups[1], "name")
        self.assertEqual(groups[2], "*")

        matcher = aggregation_regex.match("<>1--name---->")
        groups = matcher.groups()
        self.assertEqual(groups[0], "1")
        self.assertEqual(groups[1], "name")
        self.assertEqual(groups[2], "")
        print('Test1')

    def test_inheritance_regex(self):
        inheritance_regex = REGEX["inheritance"]

        self.assertTrue(inheritance_regex.match(">>"))
        self.assertFalse(inheritance_regex.match("> >"))
        print('Test3')


if __name__ == '__main__':
    unittest.main()


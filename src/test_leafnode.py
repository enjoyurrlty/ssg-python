import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\" target=\"_blank\">Hello, world!</a>")


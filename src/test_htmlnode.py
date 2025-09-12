import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test", None, {"class": "light"})
        res = " class=\"light\""
        self.assertEqual(node.props_to_html(), res)

    def test_only_val(self):
        node = HTMLNode(None, "test")
        self.assertEqual(node.value, "test")

    def test_href_props(self):
        node = HTMLNode("p", "test", None, {"href": "https://google.com", "target": "_blank"})
        res = " href=\"https://google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), res)


if __name__ == "__main__":
    unittest.main()
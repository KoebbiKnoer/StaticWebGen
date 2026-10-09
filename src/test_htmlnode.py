import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode



class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        test_dict = {}
        test_dict["href"] = "https://www.google.com"
        test_dict["target"] = "_blank"
        node = HTMLNode("a", "somestuff",None,test_dict)
        node2 = HTMLNode("a", "somestuff",None,test_dict)
        self.assertEqual(node, node2)

    def test_propsHTML(self):
        test_dict = {}
        test_dict["href"] = "https://www.google.com"
        test_dict["target"] = "_blank"
        node = HTMLNode("a", "somestuff",None,test_dict)
        test_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), test_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Hello, world!</a>')

if __name__ == "__main__":
    unittest.main()
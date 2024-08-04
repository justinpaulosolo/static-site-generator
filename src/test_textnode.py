import unittest

from textnode import (
    TextNode,
    text_type_bold
)   

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")
        self.assertIsNone(node.url)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node2", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold)
        self.assertEqual(repr(node),"TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
    unittest.main()
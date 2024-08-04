import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("p","This is a test node")
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "This is a test node"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            None
        )

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode("p","This is a test node",props=props)
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a test node")
        self.assertEqual(node.to_html(),"<p>This is a test node</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a test node")
        self.assertEqual(node.to_html(),"This is a test node")


    def test_repr(self):
        node = HTMLNode("p","This is a test node")
        self.assertEqual(repr(node),"HTMLNode(p, This is a test node, None, None)")
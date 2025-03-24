import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_different_text(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Other text", TextType.BOLD)
        self.assertNotEqual(node1, node2)  # Different texts.
    
    def test_not_eq_different_texttype(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)  # Different text types.
    
    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_different_url_and_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
    
    def test_eq_url_none_default(self):
        node1 = TextNode("This is a text node", TextType.BOLD, None)  # Explicitly None
        node2 = TextNode("This is a text node", TextType.BOLD)       # Uses default None
        self.assertEqual(node1, node2)  # Should be equal


if __name__ == "__main__":
    unittest.main()
    
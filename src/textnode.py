from enum import Enum
from leafnode import LeafNode


class TextType (Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    
    def __init__ (self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__ (self, other) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode)-> LeafNode:
    if text_node.text_type not in TextType:
        raise ValueError ("not a valid TextType")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text,props=None)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text,props=None)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text,props=None)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text,props=None)
        case TextType.LINK:
            link = {
                "href": text_node.url
            }
            return LeafNode(tag="a", value=text_node.text,props=link)
        case TextType.IMAGE:
            file = {
                "src": text_node.url,
                "alt": text_node.text 
            }
            return LeafNode(tag="img", value="",props=file)

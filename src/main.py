from textnode import TextNode
from textnode import TextType


def main ():
    Node1 = TextNode("This is some anchor text", TextType.LINK,"https://www.boot.dev")
    print(Node1)
main()
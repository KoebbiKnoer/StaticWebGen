from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("no tag")

        if self.children is None:
            raise ValueError ("no childe")

        html = ""

        for child in self.children:
            html += child.to_html()

        return f'<{self.tag}>{html}</{self.tag}>'
        
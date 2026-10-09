


class HTMLNode():
    def __init__(self, tag:str, value:str, children: list, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        html = ""
        for k in self.props:
            v = self.props[k]
            html += f' {k}="{v}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return (self.tag, self.value, self.children, self.props) == (other.tag, other.value, other.children, other.props)



    
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value can not be empty")
        if self.tag is None:
            return f"{self.value}"
        else:
            attrs = ""
            if self.props:
                attrs = self.props_to_html()

            return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
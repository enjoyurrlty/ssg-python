from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag should not be empty")
        if self.children is None:
            raise ValueError("children should not be empty")
        else:
            attr = ""
            if self.props is not None:
                attr = self.props_to_html()
            children = ""
            for child in self.children:
                children += child.to_html()

            return f"<{self.tag}{attr}>{children}</{self.tag}>"
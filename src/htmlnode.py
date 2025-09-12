class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_attrs = ""
        for prop in self.props:
            html_attrs += f" {prop}=\"{self.props[prop]}\""
        return html_attrs
    
    def __repr__(self):
        print(f"HTNLNode({self.tag}, {self.value}, {self.children}, {self.props})")
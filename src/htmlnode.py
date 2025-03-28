class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_href = self.props["href"]
        prop_target = self.props["target"]
        prop_string = f" href={prop_href} target={prop_target}"
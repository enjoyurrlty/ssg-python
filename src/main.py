import re
from leafnode import LeafNode
from textnode import TextNode, TextType

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        splitted = node.text.split(delimiter)
        
        new_nodes.append(TextNode(splitted[0], TextType.TEXT))
        new_nodes.append(TextNode(splitted[1], text_type))
        new_nodes.append(TextNode(splitted[2], TextType.TEXT))
    return new_nodes

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMG:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    if not isinstance(text_node.text_type, TextType):
        raise Exception("node should be of type TextType")
    return


def main():
    print("hello world")
    text = TextNode("this _is anchor_ tag", TextType.LINK, "https://google.com")
    print(text)
    print(split_nodes_delimiter([text], "_", TextType.ITALIC))

main()
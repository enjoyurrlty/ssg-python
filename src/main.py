from textnode import TextNode, TextType

def main():
    print("hello world")
    text = TextNode("this is anchor tag", TextType.LINK, "https://google.com")
    print(text)

main()
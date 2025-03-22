from textnode import TextNode, TextType

def main():
    new_object = TextNode("anchor text", TextType.LINK, "www.boot.dev")
    print(new_object)
    print("Hello World")

if __name__ == "__main__":
    main()
from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain_text"  # Represents normal text
    BOLD = "bold_text" 
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link_text"
    IMAGE = "image_text"
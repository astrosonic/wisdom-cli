import os

def get_terminal_width():
    """Get current terminal width"""
    return os.get_terminal_size()[0]

def wrap_text(message):
    """Wrap the whole content of a page"""
    wrapped_message = str()
    max_width = get_terminal_width()

    for m in message.split('\n'):
        if len(m) <= max_width:
            wrapped_message += m + '\n'
        else:
            wrapped_message += wrap_paragraph(m, max_width)

    return wrapped_message

def wrap_paragraph(paragraph, max_width, indent=9):
    """Wrap a long paragraph"""
    wrapped_paragraph = str()
    indent_text = ' ' * indent
    paragraph_width = len(paragraph)
    width = max_width - indent

    wrapped_paragraph += paragraph[0 : max_width]
    for i in range(max_width, paragraph_width, width):
        wrapped_paragraph += indent_text
        wrapped_paragraph += paragraph[i : i + width]
        #if i < paragraph_width - width:
        wrapped_paragraph += '\n'

    return wrapped_paragraph

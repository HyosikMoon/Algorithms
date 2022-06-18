def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if begin in text and end in text:
        return text[text.index(begin)+len(begin):text.index(end)]
    elif begin in text and end not in text:
        return text[text.index(begin)+len(begin):]
    elif begin not in text and end in text:
        return text[:text.index(end)]
    else:
        return text
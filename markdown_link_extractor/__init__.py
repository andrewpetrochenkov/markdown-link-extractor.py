__all__ = ['getlinks']


import markdown
import re


def getlinks(string):
    """return a list with markdown links"""
    html = markdown.markdown(string, output_format='html')
    links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', html)))
    links = list(filter(lambda l: l[0] != "{", links))
    return links

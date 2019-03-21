#!/usr/bin/env python
import markdown
import public
import re


@public.add
def getlinks(string):
    """return a list with markdown links"""
    html = markdown.markdown(string, output_format='html')
    r = re.compile('(?<=href=").*?(?=")')
    result = []
    for link in r.findall(html):
        if link not in result:
            result.append(link)
    return result

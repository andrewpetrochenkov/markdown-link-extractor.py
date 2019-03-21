#!/usr/bin/env python
import markdown
import public
import re


@public.add
def getlinks(string):
    """return a list with markdown links"""
    html = markdown.markdown(string, output_format='html')
    return list(set(re.findall(r'href=[\'"]?([^\'" >]+)', html)))

#!/usr/bin/env python
"""extract links from markdown files"""
# -*- coding: utf-8 -*-
import click
import markdown_link_extractor


MODULE_NAME = "readme_links"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    links = []
    for path in paths:
        string = open(path).read()
        links += markdown_link_extractor.getlinks(string)
    if links:
        print("\n".join(sorted(list(set(links)))))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)

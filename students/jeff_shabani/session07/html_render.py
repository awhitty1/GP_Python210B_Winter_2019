#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        if content:
            self.content = content
        else:
            self.content = ''

    def append(self, new_content):
        result = list()
        result.append(new_content)
        for i in result:
            self.content +=i
        return self.content


    def render(self, out_file):
        out_file.write("just something as a place holder...")

e=Element()
e.append('Wulliam\nB')
print(e.content)


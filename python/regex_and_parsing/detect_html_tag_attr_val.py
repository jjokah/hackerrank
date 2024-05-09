"""
HackerRank Chanllenge: Detect HTML Tags, Attributes and Attribute Values (Python)
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

Parse HTML tags, attributes and attribute values in this challenge.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

    def print_attrs(self, attrs):
        for attr, value in attrs:
            print(f"-> {attr} > {value}")


html = ""
for _ in range(int(input())):
    html += input()
    html += "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()

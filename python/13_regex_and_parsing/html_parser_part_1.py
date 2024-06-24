"""
HackerRank Challenge: HTML Parser - Part 1 (Python)
https://www.hackerrank.com/challenges/html-parser-part-1/problem

Parse HTML tags, attributes and attribute values using HTML Parser.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        self.print_attrs(attrs)

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        self.print_attrs(attrs)

    def print_attrs(self, attrs):
        for name, value in attrs:
            print(f"-> {name} > {value}")


parser = MyHTMLParser()
parser.feed("".join(input() for _ in range(int(input()))))

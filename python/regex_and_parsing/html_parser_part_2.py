"""
HackerRank Chanllenge: HTML Parser - Part 2 (Python)
https://www.hackerrank.com/challenges/html-parser-part-2/problem

Parse HTML comments and data using HTML Parser.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if '\n' not in data:
            print('>>> Data')
            print(data)


html = ''
for _ in range(int(input())):
    html += input()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

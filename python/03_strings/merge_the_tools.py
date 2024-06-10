"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # get the substring
        sub_list = string[i:i + k]

        new_sub_list = []
        for character in sub_list:
            # print non-duplicate characters from each substring
            if character not in new_sub_list:
                new_sub_list.append(character)
        print("".join(new_sub_list))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

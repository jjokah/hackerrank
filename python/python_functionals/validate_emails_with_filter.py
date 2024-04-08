"""
HackerRank Chanllenge: Validating Email Addresses With a Filter (Python)
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

This question covers the concept of filters.
"""

def fun(s):
    try:
        username, site_and_ext = s.split('@', 1)
        site, ext = site_and_ext.split('.', 1)

        username = username.replace('-', '')
        username = username.replace('_', '')
        if username.isalnum():
            if site.isalnum():
                if ext.isalpha():
                    if len(ext) <= 3:
                        return True
        return False
    except ValueError:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
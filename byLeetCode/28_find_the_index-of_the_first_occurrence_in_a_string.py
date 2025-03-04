"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=string
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

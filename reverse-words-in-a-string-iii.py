class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_words = [word[::-1] for word in words]
        return ' '.join(reverse_words)

'''
Given a word and a text, return the count of occurrences of the anagrams of the word in the text.
An anagram of a word is a word that’s formed by rearranging the letters of the original word.
eg.
Input : text = aabaabaa, word = aaba
Output : 4
Explanation : Anagrams of the word aaba - aaba, abaa each appear twice in the text and hence the
count is 4.
'''


def anagram_occurrence(text: str, word: str) -> int:
    # two words are anagrams of each other if the count of every character in both the words are same.
    def is_anagram(word1: str, word2: str) -> bool:
        word1_count = {}
        word2_count = {}

        for i in word1:
            if word1_count.get(i):
                word1_count.update({i: word1_count.get(i) + 1})
            else:
                word1_count[i] = 1

        for i in word2:
            if word2_count.get(i):
                word2_count.update({i: word2_count.get(i) + 1})
            else:
                word2_count[i] = 1

        for c in word1_count.keys():
            if word1_count.get(c) != word2_count.get(c):
                return False

        return True

    count = 0
    window_start, window_end = 0, len(word)

    while window_end <= len(text):

        if is_anagram(word, text[window_start:window_end]):
            count += 1
        window_start += 1
        window_end += 1

    return count


if __name__ == '__main__':
    print(anagram_occurrence("aabaabaa", "aaba"))  # 4
    print(anagram_occurrence("forxxorfxdofr", "for")) # 3


class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        
        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))
        
        return max_words
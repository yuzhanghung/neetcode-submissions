class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ["a", "e", "i", "o", "u"]
        res = []
        cnt = []


        for word in words:
            l, r = 0, len(word) - 1
            if word[l] in vowel and word[r] in vowel:
                cnt.append(True)
            else:
                cnt.append(False)

        for query in queries:
            l, r = query[0], query[-1]
            count = 0
            for i in range(l, r + 1):
                if cnt[i]:
                    count += 1
            res.append(count)

        return res


        
            


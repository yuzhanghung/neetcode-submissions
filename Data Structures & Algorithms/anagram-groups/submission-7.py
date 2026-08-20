class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash table: sorted str: orginal strs
        # log n

        anagrams = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in anagrams:
                anagrams[sortedS].append(s)
            else:
                anagrams[sortedS] = [s]

        return list(anagrams.values())

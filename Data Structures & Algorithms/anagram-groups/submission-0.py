class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used = set()
        result = []
        for i in range(len(strs)):
            if i in used:
                continue
            used.add(i)
            cur_anagrams = [strs[i]]
            cur_word_len = len(strs[i])
            cur_word = Counter(strs[i])
            for j in range(i + 1, len(strs)):
                ana_can = strs[j]
                if len(ana_can) == cur_word_len and cur_word == Counter(ana_can):
                    cur_anagrams.append(ana_can)
                    used.add(j)
            result.append(cur_anagrams)
        return result

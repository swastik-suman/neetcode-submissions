class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            sorted_S=''.join(sorted(s))
            result[sorted_S].append(s)
        return list(result.values())
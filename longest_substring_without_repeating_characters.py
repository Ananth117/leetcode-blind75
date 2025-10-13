class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len, start, index_dict=0, 0, {}
        for end in range(len(s)):
            char = s[end]
            if char in index_dict and index_dict[char]>=start:
                start = index_dict[char]+1
            index_dict[char] = end
            max_len = max(max_len, end-start+1)
        return max_len
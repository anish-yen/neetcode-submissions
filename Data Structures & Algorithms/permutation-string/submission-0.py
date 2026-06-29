class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, it can't be a substring.
        if len(s1) > len(s2):
            return False

        # Initialize frequency arrays for 26 lowercase English letters
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Populate the initial window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Calculate initial matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add the new character entering the window from the right
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the old character leaving the window from the left
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # Shrink the window
            l += 1

        # Check the final window
        return matches == 26
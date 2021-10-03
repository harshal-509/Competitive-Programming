#Author : koder_786
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        def findLongestSequence(A, k):
            left = 0
            count = 0 
            window = 0
            leftIndex = 0
            for right in range(len(A)):
                if A[right] == "T":
                    count = count + 1
                while count > k:
                    if A[left] == "T":
                        count = count - 1
                    left = left + 1
                if right - left + 1 > window:
                    window = right - left + 1
                    leftIndex = left
            if window == 0:
                return
            return window
        def findLongestSequenceF(A, k):
            left = 0
            count = 0 
            window = 0
            leftIndex = 0
            for right in range(len(A)):
                if A[right] == "F":
                    count = count + 1
                while count > k:
                    if A[left] == "F":
                        count = count - 1
                    left = left + 1
                if right - left + 1 > window:
                    window = right - left + 1
                    leftIndex = left
            if window == 0:
                return
            return window
        ans=findLongestSequence(answerKey, k)
        ans=max(ans,findLongestSequenceF(answerKey, k))
        return ans
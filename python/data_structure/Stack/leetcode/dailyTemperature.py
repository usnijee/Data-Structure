'''
739. Daily Temperature

정수 배열 temperatures가 매일의 온도를 나타낸다고 할 때, 배열 answer를 반환하세요. 
answer[i]는 i번째 날 이후 더 따뜻한 온도가 나올 때까지 기다려야 하는 날 수를 나타냅니다. 
만약 더 따뜻한 온도가 나오는 날이 없다면, answer[i]는 0이어야 합니다.

'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        
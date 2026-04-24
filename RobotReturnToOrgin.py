class Solution(object):
    def judgeCircle(self, moves):
        u=(moves.count('U'))
        d=(moves.count('D'))
        l=(moves.count('L'))
        r=(moves.count('R'))
        if abs(u-d)==0 and abs(l-r)==0:
            return True
        else:
            return False

'''
Problem Description

Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.



Problem Constraints
1 <= N <= 105

1 <= A[i][0] <= A[i][1] <= 109



Input Format
First and only argument is a 2D array A of size N x 2 denoting the N intervals.



Output Format
Return a integer denoting the length of maximal set of mutually disjoint intervals.



Example Input
Input 1:

 A = [
       [1, 4]
       [2, 3]
       [4, 6]
       [8, 9]
     ]
Input 2:

 A = [
       [1, 9]
       [2, 3]
       [5, 7]
     ]


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Intervals: [ [1, 4], [2, 3], [4, 6], [8, 9] ]
 Intervals [2, 3] and [1, 4] overlap.
 We must include [2, 3] because if [1, 4] is included thenwe cannot include [4, 6].
 We can include at max three disjoint intervals: [[2, 3], [4, 6], [8, 9]]
Explanation 2:

 Intervals: [ [1, 9], [2, 3], [5, 7] ]
 We can include at max two disjoint intervals: [[2, 3], [5, 7]]
'''


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        A.sort()
        stack = []
        for s, e in A:
            if stack and s <= stack[-1][1]:
                prev_s, prev_e = stack.pop()
                stack.append([min(s, prev_s), min(e, prev_e)])
            else:
                stack.append([s, e])
        
        return len(stack)





#Space Optimization
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        A.sort()
        prev_e = None
        res = 0
        for s, e in A:
            if prev_e and s <= prev_e:
                prev_e = min(e, prev_e)
            else:
                prev_e = e
                res += 1
        
        return res

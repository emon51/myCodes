
'''
Given a string containing of 0, 1 and ? - a wildcard character, generate all distinct binary strings that can be formed by replacing each wildcard character by either 0 or 1.

Example 1:

Input: 1??0?101
Output: 10000101 10001101 10100101 10101101 
11000101 11001101 11100101 11101101
Explanation:
There will be 8 such possible strings that 
can be formed, they are 10000101, 10001101, 
10100101, 10101101, 11000101, 11001101, 
11100101 and 11101101.
Example 2:

Input: 10?
Output: 100 101
Explanation: There are 2 such possible strings
and they are 100 and 101.
Your Task:
You don't need to read or print anything. Your task is to complete the function generate_binary_string() which takes the given string as input parameter and returns a vector of strings containing all the possible strings that can be formed.

Note : Strings should be printed in lexicographically increasing order.

Expected Time complexity: O(2n)
Expected Space complexity: O(n*2n)

Constraints:
1 ≤ length of string ≤ 30
Note: Number of '?' in any string does not exceed 15.
'''


class Solution:
    def generate_binary_string(self,s):
        
        res = []
        def fun(i, p):
            nonlocal res
            if i == len(s):
                res.append(p)
                return 
            if s[i] == '?:
                fun(i + 1, p + '0')
                fun(i + 1, p + '1')
            else:
                fun(i + 1, p + s[i])
        
        fun(0, '')
        return res
            

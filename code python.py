class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # Get the length of the input string
        string_length = len(s)
        # Initialize a DP array with zeros, one extra for the base case
        dp = [0] * (string_length + 1)
      
        # Loop over the characters of string starting from index 1 for convenience
        for index, char in enumerate(s, 1):
            # We look for closing parentheses, as they mark possible ends of valid substrings
            if char == ")":
                # If the previous char is '(', it's a pair "()"
                if index > 1 and s[index - 2] == "(":
                    # Add 2 to the result two positions ago in dp array
                    dp[index] = dp[index - 2] + 2
                else:
                    # Get the index of the potential matching '('
                    match_index = index - dp[index - 1] - 1
                    # Make sure match_index is within bounds and check for '('
                    if match_index > 0 and s[match_index - 1] == "(":
                        # Add the length of the valid substring ending right before the current one,
                        # plus two for the '()' just found, plus length of valid substring before the pair
                        dp[index] = dp[index - 1] + 2 + dp[match_index - 1]
      
        # Return the maximum length of valid parentheses found
        return max(dp)

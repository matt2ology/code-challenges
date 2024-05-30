class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []

        # Dictionary to keep mappings of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty,
                # otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the corresponding
                # opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets had a matching closing
        # bracket
        return not stack


if __name__ == "__main__":
    # Driver code
    s = Solution()
    print("() : " + str(s.isValid("()")))  # True
    print("()[]{} : " + str(s.isValid("()[]{}")))  # True
    print("(] : " + str(s.isValid("(]")))  # False
    print("([)] : " + str(s.isValid("([))]")))  # False
    print("{[]} : " + str(s.isValid("{[]}")))  # True
    print("} : " + str(s.isValid("}")))  # False
    print("[ : " + str(s.isValid("[")))  # False
    print("] : " + str(s.isValid("]")))  # False
    print("{{ : " + str(s.isValid("{{")))  # False
    print("}} : " + str(s.isValid("}}")))  # False
    print("{{}} : " + str(s.isValid("{{}}")))  # True
    print("{{}}{} : " + str(s.isValid("{{}}{}")))  # True

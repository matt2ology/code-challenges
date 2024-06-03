# Interview question: Given two strings check if they can be encoded
# JR0001747 - Development Tools Software Engineer - 2nd Interview
# with Daniel Keith - 2024-05-30 (Thursday) 2:00 PM - 3:00 PM


def foo(s1: str, s2: str) -> bool:
    """my attempt at solving the problem of checking if two strings are
    isomorphic during a coding interview. I was given the problem and had to
    solve it in 30 minutes.

    The code prompt: Given two strings check if they can be encoded
    (i.e are isomorphic) to each other.

    For example, "cat" and "dog" can be encoded to each other because
    the characters in "cat" can be replaced with the characters in "dog". "c"
    can be replaced with "d", "a" can be replaced with "o", and "t" can be
    replaced with "g". If the strings cannot be encoded to each other, return
    False.

    Args:
        s1 (str): First string to check if it can be encoded to s2
        s2 (str): Second string to check if it can be encoded to s1

    Returns:
        bool: True if the strings can be encoded to each other, False otherwise
    """
    result: bool = False
    dict = {}
    for index, value in enumerate(s1):
        if value in dict:
            if dict[value] != s2[index]:
                return result
        else:
            dict[value] = s2[index]

    result = True
    return result


def isIsomorphic(s1: str, s2: str) -> bool:
    """Check if two strings are isomorphic. Two strings are isomorphic if the
    characters in s1 can be replaced to get s2. All occurrences of a character
    and all occurrences of another character will be replaced with the
    corresponding characters.

    Args:
        s1 (str): First string to check if it can be encoded to s2
        s2 (str): Second string to check if it can be encoded to s1

    Returns:
        bool: True if the strings can be encoded to each other, False otherwise
    """
    result: bool = False
    if len(s1) == len(s2):  # Check if the strings are of equal length
        s1_dict = {}  # Dictionary to store the characters in s1
        s2_dict = {}  # Dictionary to store the characters in s2
        # Loop through the characters in s1
        for i in range(len(s1)):
            # If the character is not in the dictionary for s1 (s1_dict)
            if s1[i] not in s1_dict:
                s1_dict[s1[i]] = i  # Add the character to the dictionary
                print("s1: ", s1[i], " -> ", i)
            # If the character is not in the dictionary for s2 (s2_dict)
            if s2[i] not in s2_dict:
                s2_dict[s2[i]] = i  # Add the character to the dictionary
            # If the characters are not equal in the dictionary for s1 and s2
            if s1_dict[s1[i]] != s2_dict[s2[i]]:
                return False  # The strings are not isomorphic
        result = True  # The strings are isomorphic
    return result  # The strings are isomorphic if the loop completes


if __name__ == "__main__":
    print("===============================================")
    print("MY ATTEMPT")
    print("===============================================")
    print("cat ->", "dog: ", foo("cat", "dog"))      # True (123 -> 123)
    print("mom ->", "dad: ", foo("mom", "dad"))      # True (121 -> 121)
    print("talk ->", "look: ", foo("talk", "look"))  # False (1234 -> 1223)
    print("mmo ->", "dad: ", foo("mmo", "dad"))      # False (112 -> 121)
    print("mama ->", "moo: ", foo("mama", "moo"))    # False (1212 -> 122)
    print("===============================================")
    print("THE SOLUTION")
    print("===============================================")
    # True (123 -> 123) Because c -> d, a -> o, t -> g (cat -> dog)
    print("cat ->", "dog: ", isIsomorphic("cat", "dog"))
    # True (121 -> 121) Because m -> d, o -> a (mom -> dad)
    print("mom ->", "dad: ", isIsomorphic("mom", "dad"))
    # False (1234 -> 1223) Because 'o' is mapped to 'o' and 'k'
    print("talk ->", "look: ", isIsomorphic("talk", "look"))
    # False (112 -> 121) Because 'm' is mapped to 'd' and 'a'
    print("mmo ->", "dad: ", isIsomorphic("mmo", "dad"))
    # False (1212 -> 122) Because 'm' is mapped to both 'm' and 'o'
    print("mama ->", "moo: ", isIsomorphic("mama", "moo"))

    # Test cases for the isIsomorphic function prints True if the test passes
    # This is how I would test the function in a real-world scenario
    assert isIsomorphic("cat", "dog") is True      # True (123 -> 123)
    assert isIsomorphic("mom", "dad") is True      # True (121 -> 121)
    assert isIsomorphic("egg", "add") is True      # True (122 -> 122)
    assert isIsomorphic("paper", "title") is True  # True (12345 -> 12345)
    assert isIsomorphic("ab", "ca") is True        # True (12 -> 13)
    assert isIsomorphic("talk", "look") is False   # False (1234 -> 1223)
    assert isIsomorphic("mmo", "dad") is False     # False (112 -> 121)
    assert isIsomorphic("mama", "moo") is False    # False (1212 -> 122)
    assert isIsomorphic("foo", "bar") is False     # False (112 -> 121)
    assert isIsomorphic("ab", "aa") is False       # False (12 -> 11)

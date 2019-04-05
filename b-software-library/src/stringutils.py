def compare(str1, str2):
    """Returns whether one is greater than, equal, or less than the other.
    
    Args:
        str1 (str): The string which is to be compared with.
        str2 (str): The other string.

    Raises:
        ValueError: If str1 or str2 is equal to None.

    Returns:
        -1 if str1 is less than str2.
        0 if str1 is equal to str2.
        1 if str1 is greater than str2.

    """
    to_string = lambda inp : str(inp) if type(inp) != str else inp

    if str1 == None or str2 == None:
        raise ValueError("You should give me 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: '1.2' is greater than '1.1'")

    str1=to_string(str1)
    str2=to_string(str2)
    
    for char1, char2 in zip(str1, str2):
        ascii1 = ord(char1)
        ascii2 = ord(char2)
        if ascii1 != ascii2:
            return 1 if ascii1 > ascii2 else -1

    return 0 if len(str1) == len(str2) else (1 if len(str1) > len(str2) else -1)



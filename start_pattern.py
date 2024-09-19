
def default_way(n: int) -> None:
    """
    This function just holds the print pattern
    as default way of implementation.

    Param: n  (int)
    Usage: funcName(Param)
    Returns: None
    """
    for i in range(1, n+1):
        for _ in range(1, n-i+1):
            print('-', end=' ')
        for _ in range(i*2-1):
            print('*', end=' ')
        print()



def modified_way(n: int) -> str:
    """

    """
    pass




n = 5

#GENERATING THE PATTERN BY DEFAULT WAY!
default_way(n)

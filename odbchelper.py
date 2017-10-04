def buildConnectionString(params):
    """ Builds a connection string from a dictionary of params
    :param params: a dictionary
    :return: string
    """
    return ";".join(["%s=%s" % (k,v) for k, v in params.items()])
def factorial(n):
    """ Factorial, just as you know it
    :param n: integer
    :return: factorial
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    myParams={
        "server": "txbiomed",
        "database":"animal",
        "uid": "sa",
        "pwd":"secret"
    }

    print(buildConnectionString(myParams))
    print(factorial(5))
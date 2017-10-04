def info(object, spacing=10, collapse=1):
    """ prints methods and doc strings

    :param object: can be a module, a class, a list, a dictionary, a string, or any other object
    :param spacing:  defaults to 10
    :param collapse: defaults to 1
    :return:
    """
    methodsList=[method for method in dir(object) if callable(getattr(object,method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" %
                    (
                        method.ljust(spacing),
                        processFunc(str(getattr(object,method).__doc__))
                    )
                    for method in methodsList])

if __name__ =="__main__":
    print info.__doc__
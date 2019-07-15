def foo(hello: int, *, world: str='world', **kwargs):
    """
    :param **kwargs: 
    :type **kwargs: 
    :param world:  (Default: ""\"world""\")
    :type world: str
    :param hello: 
    :type hello: int
    """
    pass


class Bar:

    def fizz(self, buzz: bytes, *python: list, js: str='ew'):
        """
        Docstring!
        
        :param *python: 
        :type *python: list
        :param js:  (Default: ""\"ew""\")
        :type js: str
        :param buzz: 
        :type buzz: bytes
        """

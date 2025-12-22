class Account:
    '''
    Docstring for Account
    hides internal details for account 
    '''

    def __init__(self):

        self._balance = 0 # protected 
        self.__pin = 1234 # private 
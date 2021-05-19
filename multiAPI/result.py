class Result:
    def __init__(self, 
                 isSuccess: bool, 
                 message:   str, 
                 value:     str = None ):
        self.isSuccess = None 
        self.message   = message
        self.value     = value
        
    def is_ok(self):
        return self.isSuccess


class Error(Result):
    def __init__(self, 
                 message: str, 
                 value:   str = None ):
        super().__init__(message,value)
        self.isSuccess = False


class Ok(Result):
    def __init__(self, 
                 message: str, 
                 value:   str = None ):
        super().__init__(message,value)
        self.isSuccess = True
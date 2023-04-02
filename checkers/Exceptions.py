
class BadMoveExceptions(Exception):
    def __init__(self):
        self.message = f'bad move'



class OutsideBoardExceptions(Exception):
    def __init__(self):
        self.message = f'outside board exce'

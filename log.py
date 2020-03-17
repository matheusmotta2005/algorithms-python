class Log:
    def __init__(self, input):
        self.__input = input

    def before(self):
        self.__log(self.__input,-1)

    def log(self):
        self.__log(self.__input,0)

    def after(self):
        self.__log(self.__input,1)

    def __log(self, value, pos):
        position = ""
        if pos<0:
            position = "Before: "
        elif pos>0:
            position = "After: "
        else:
            position = "Output: "
        print(position+str(value))

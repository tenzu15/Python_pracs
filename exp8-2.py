from abc import ABC,abstractmethod
class Reverse(ABC):
    def __init__(self,st):
        (self.st)=str(st)
    @abstractmethod
    def reversal(self):
        pass
class Main(Reverse):
    def reversal(self):
        strev=""
        strev=reversed(self.st)
        print(strev)
        return strev
r=Main("prit")
print(r.reversal())

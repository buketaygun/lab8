from abc import ABC


class Address(ABC):
    address=""
    def __init__(self,ad):
            self.address=ad

    def calculateFreqs(self):
        pass


class ListCount(Address):
    def __init__(self, buket):

        super(ListCount, self).__init__(buket)

    def calculateFreqs(self ):
        with open(self.address)as f :
            lines=f.read()
        print(lines)



class DictCount(Address):

    def __init__(self):
        super(DictCount, self).__init__()

    def calculateFreqs(self):
        super().calculateFreqs()

myobj=ListCount("C:\\Users\\Hp\\Desktop\\yeni.txt")
myobj.calculateFreqs()



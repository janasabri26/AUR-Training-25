from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)

class BaseMsg:
    def __init__(self,data:str):
        self._data=data

    @property
    def style(self):
        return ''
    
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data
    
    def __len__(self):
        return len(str(self))
    
    def __eq__(self,other):
        if isinstance(other,BaseMsg):
            return str(self)==str(other)
        else:
            return False
    def __add__(self,other):
        if isinstance(other,BaseMsg):
            return type(self)(self.data+other.data)
        elif isinstance(other,str):
            return type(self)(self.data+other)
        else:
            raise TypeError(f"can't add {type(other)} to BaseMsg")

class LogMsg(BaseMsg):
    def __init__ (self,data):
        super().__init__(data)
        self._timestamp:int=int(time())

    @property
    def style(self):
        return 'black on yellow'
    def __str__(self):
        return (f"[{self._timestamp}] {self.data}")

        

class WarnMsg(LogMsg):
    class WarnMsg(LogMsg):
        @property
        def style(self):
            return 'white on red'  
        
        @property
        def __str__(self):
            return f"[!WARN][{self._timestamp}] {self.data}"   









if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
send_Msg(m1)
send_Msg(m2)
send_Msg(m3)  
        
    


from example1 import MyFunction1
from typing import List

def MyFunction3(b: int):
    print("hello world from example MyFunction3!")
    print("something more")
    a = "s"
    return 2+b, "sss"

def fc():
    pass

if __name__ == "__main__":
    MyFunction1()
    try:
        myint, mystr = MyFunction3(1)
        print(myint)
    except Exception as e:
        print(e) 


def func1():
    x = 1  #Here X is a enclosed variable
    
    def func2():
        x = 2 #Here the scope of x is local in func2
        print(x)

    func2()

func1()
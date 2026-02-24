def question12():

    # Input 
     num = int(input("Enter the number: "))
     limit = int(input("Enter range: "))
     
     print("\Multiplication table of", num)

     for i in range(1, limit+1):
        print(f"{num} x {i} = {num*i}")
     question12()
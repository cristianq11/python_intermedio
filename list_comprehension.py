def run():
    
    squares = [ i for i in range(1, 100000) if i % 36 == 0] # encontrar el minimo comun multiplo entre los numeros 4,5 y 9 
    print(squares)
    
if __name__ == '__main__':
    run()
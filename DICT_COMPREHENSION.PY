def run():
    squere = {i:i**3 for i in range(1,101) if i %3 != 0 }

    print(squere)

    raiz = {i:i**0.5 for i in range(1,101)}

    print(raiz)
    
if __name__=='__main__':
    run()
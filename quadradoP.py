import os

if __name__ == "__main__":
    numero=int(input("Digite um número: "))
    os.system("clear")
    for y in range(1,100):
        if(numero==y*y):
            print("O número {} é quadrado perfeito".format(numero))
            exit()
    print("O número {} não é quadrado perfeito".format(numero))       

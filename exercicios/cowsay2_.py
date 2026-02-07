import cowsay

def desenhar():
    mensagem = "muuuuu!"
    desenho = cowsay.draw(mensagem, cow=cowsay.cow)
    print(desenho)

if __name__ == "__main__":
    desenhar()

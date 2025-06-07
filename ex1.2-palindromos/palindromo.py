class Palindromo:
    def __init__(self, palavra):
        self.palavra = palavra

    def verificar_palindromo(self):
        palavra_sem_espacos = self.palavra.replace(" ", "").lower()
        return palavra_sem_espacos == palavra_sem_espacos[::-1]
    
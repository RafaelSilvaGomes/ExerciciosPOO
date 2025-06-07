class Palindromo:
    def eh_palindromo(self, palavra):
        palavra_sem_espacos = palavra.replace(" ", "").lower()
        return palavra_sem_espacos == palavra_sem_espacos[::-1]
    
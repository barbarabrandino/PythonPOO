class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.set_nota(nota)

    def set_nota(self, nota: float):
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:
            self._nota = nota
        else:
            raise ValueError("A nota deve ser um número entre 0 e 10.")

    def get_nota(self):
        return self._nota

    def __str__(self):
        return f"Aluno: {self.nome}, Nota: {self._nota}"

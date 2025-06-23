class Arquivo:
    def __init__(self, nome):
        self.nome = nome

    def abrir(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


class ArquivoTexto(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"Abrindo o arquivo de texto: {self.nome}")


class ArquivoImagem(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"Exibindo a imagem: {self.nome}")


class ArquivoVideo(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"Reproduzindo o vídeo: {self.nome}")



arquivos = [
    ArquivoTexto("documento.txt"),
    ArquivoImagem("foto.jpg"),
    ArquivoVideo("filme.mp4")
]

for arquivo in arquivos:
    arquivo.abrir()

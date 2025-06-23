# Modele um sistema de envio de mensagens com as classes Email, SMS e Whatsapp. Todas devem ter o método enviar_mensagem().

class EnvioMensagens:
    def __init__(self,destinatario,conteudo):
        self.destinatario = destinatario
        self.conteudo = conteudo 
    def enviar_mensagem(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    
class Email(EnvioMensagens):
    def enviar_mensagem(self):
        print(f"Enviando Email para {self.destinatario}: {self.conteudo}")

class SMS(EnvioMensagens):
    def enviar_mensagem(self):
        print(f" SMS enviado para {self.destinatario}: {self.conteudo}")

class Whatsapp(EnvioMensagens):
    def enviar_mensagem(self):
        print(f"Whatsapp enviado para {self.destinatario}: {self.conteudo}")

mensagens = [
    Email("joao@email.com", "Olá, João!"),
    SMS("+5591983000000", "Código: 1234"),
    Whatsapp("+5591988112233", "Oi! Chegarei às 18h.")
]

for mensagem in mensagens:
    mensagem.enviar_mensagem()  

# Modele um sistema de notificações com as classes NotificacaoEmail, NotificacaoSMS e NotificacaoPush.
# Superclasse
class Notificacao:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f"Enviando EMAIL para {self.destinatario}: {self.mensagem}")



class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f"Enviando SMS para {self.destinatario}: {self.mensagem}")



class NotificacaoPush(Notificacao):
    def enviar(self):
        print(f"Enviando PUSH para {self.destinatario}: {self.mensagem}")



notificacoes = [
    NotificacaoEmail("joao@email.com", "Você tem um novo e-mail."),
    NotificacaoSMS("+5591987654321", "Código de verificação: 123456"),
    NotificacaoPush("Usuário123", "Você recebeu uma nova curtida.")
]

for notificacao in notificacoes:
    notificacao.enviar()

    
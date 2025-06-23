
class Pagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError("Este método deve ser implementado na subclasse.")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento no cartão no valor de R$ {valor:.2f}")
        print("Pagamento autorizado.")

class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento via PIX no valor de R$ {valor:.2f}")
        print("Pagamento realizado com sucesso.")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Gerando boleto no valor de R$ {valor:.2f}")
        print("Boleto gerado. Aguarde compensação.")

pagamentos = [
    PagamentoCartao(),
    PagamentoPix(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.processar_pagamento(260.00)
    print("-" * 30)
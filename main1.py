class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class ContaBancaria:
    numero_conta = 1
    agencia = "0001"

    def __init__(self, usuario):
        self.numero = ContaBancaria.numero_conta
        ContaBancaria.numero_conta += 1
        self.agencia = ContaBancaria.agencia
        self.usuario = usuario
        self.saldo = 0
        self.limite_por_saque = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        valor_depositado = "Depósito de R$ " + str(valor)
        self.extrato.append(valor_depositado)
        print(f"O seu saldo atual é de R$ {self.saldo}")

    def sacar(self, valor):
        if self.numero_saques < self.LIMITE_SAQUES:
            if valor <= self.saldo:
                if valor > self.limite_por_saque:
                    print(f"Valor não permitido, o valor máximo permitido é de {self.limite_por_saque}")
                else:
                    print(f"Sacando o valor de R$ {valor} ...")
                    self.saldo -= valor
                    self.numero_saques += 1
                    valor_sacado = "Saque de - R$ " + str(valor)
                    self.extrato.append(valor_sacado)
                    print(f"O seu saldo atual é de R$ {self.saldo}")
            else:
                print("Saldo insuficiente!")
        else:
            print(f"O limite de saques diários foi excedido, o limite máximo permitido é de {self.LIMITE_SAQUES}")

    def mostrar_extrato(self):
        for item in self.extrato:
            print(item)
        print("")
        print(f"O seu saldo disponível é de R$ {self.saldo}")


def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = {
        "logradouro": input("Digite o logradouro do endereço: "),
        "numero": input("Digite o número do endereço: "),
        "bairro": input("Digite o bairro do endereço: "),
        "cidade": input("Digite a cidade do endereço: "),
        "estado": input("Digite a sigla do estado do endereço: ")
    }

    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Não é possível criar um usuário com o mesmo CPF.")
            return

    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def criar_conta():
    cpf = input("Digite o CPF do usuário para criar a conta: ")

    # Procura pelo usuário com o CPF informado
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print
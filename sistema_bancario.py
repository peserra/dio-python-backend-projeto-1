from abc import ABC, abstractmethod
from datetime import date


class Historico:
    def __init__(self) -> None:
        self._transacoes:list = []
    def adicionar_transacao(self, transacao:"Transacao"):
        self._transacoes.append(transacao)


class Cliente:
    def __init__(
        self,
        endereco:str,
        ):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta:"Conta"):
        self._contas.append(conta)

    def realizar_transacao(self, conta:"Conta", transacao:"Transacao"):
        transacao.registrar(conta)

class Conta:
    def __init__(
        self,
        numero:int,
        agencia:str,
        cliente:Cliente,
        ):
        self._saldo:float = 0
        self._historico:Historico = Historico()
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente

    @property
    def saldo(self)->float:
        return self._saldo

    @classmethod
    def nova_conta(
        cls,
        cliente:Cliente,
        numero:int
        ):
        return cls(cliente=cliente, numero = numero, agencia = "1000")

    def sacar(self, valor:float) -> bool:
        if valor > self._saldo:
            return False

        self._saldo -= valor
        return True;

    def depositar(self, valor:float) -> bool:
        if valor <= 0:
            return False
        self._saldo += valor
        return True;


# interface
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor:float) -> None:
        self._valor = valor

    def registrar(self, conta:Conta):
        if conta.depositar(self._valor):
            conta._historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        self._valor = valor

    def registrar(self, conta:Conta):
        if conta.sacar(self._valor):
                conta._historico.adicionar_transacao(self)

class ContaCorrente(Conta):
    def __init__(
            self,
            numero,
            agencia,
            cliente,
            limite,
            limite_saques):

        super().__init__( numero, agencia, cliente)
        self._limite:float = limite
        self._limite_saques:int = limite_saques
    pass

class PessoaFisica(Cliente):
    def __init__(
        self,
        cpf:str,
        nome:str,
        data_nascimento: date,
        endereco:str
        ):
            super().__init__(endereco)
            self._cpf = cpf
            self._nome = nome
            self._data_nascimento = data_nascimento
            pass
    pass


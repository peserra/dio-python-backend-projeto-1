from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def adicionar_transacao(self):
    pass

class Deposito:
    valor:float = 0
    pass

class Saque:
    valor:float = 0
    pass

class Cliente:
    def __init__(
        self,
        endereco:str,
        contas:list
         
        ):
        pass
    
    def adicionar_conta(conta:Conta):
        pass



class Conta:
    def __init__(
        self, 
        saldo:float, 
        numero:int, 
        agencia:str, 
        cliente:Cliente, 
        historico:Historico
        ):
        pass
    
    def saldo()->float:
        pass
    
    def nova_conta(
        cliente:Cliente, 
        numero:int
        ) -> Conta:
        pass
    
    def sacar(valor:float) -> bool:
        pass
    
    def depositar(valor:float) -> bool:
        pass

# interface
class Transacao(ABC):
    @abstractmethod
    def registrar(conta:Conta):
        pass


class ContaCorrente(Conta):
    limite:float = 0
    limite_saques:int = 0
    
    def __init__(self, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo, numero, agencia, cliente, historico)
    pass



class PessoaFisica:
    def __init__(
        self,
        cpf:str,
        nome:str,
        data_nascimento: date
        ):
        pass
    pass


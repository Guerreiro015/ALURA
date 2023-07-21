class ContaSalario: 
  def __init__(self, codigo):
      self._codigo = codigo
      self._saldo = 0

  def __eq__(self, outro):
      return self._codigo == outro._codigo

  defdeposita(self, valor):
      self._saldo += valor

    def__str__(self):
      return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
  
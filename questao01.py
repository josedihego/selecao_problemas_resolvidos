class Empresa:
    def __init__(self, CNPJ, razao_social):
        self.funcionarios = []
        self.veiculos  = []
        self.CNPJ = CNPJ
        self.razao_social = razao_social

    def cadastrar_funcionario(self, fun_novo):
        self.funcionarios.append(fun_novo)

    def cadastrar_veiculo(self, vei_novo):
        self.veiculos.append(vei_novo)

class Funcionario:
    def __init__(self, nome, CPF, salario_bruto):
        self.nome = nome
        self.CPF = CPF
        self.salario_bruto = salario_bruto
    def __repr__(self):
        return repr((self.nome, self.CPF, self.salario_bruto))

class Veiculo:
    def __init__(self, placa, n_km, modelo):
        self.placa = placa
        self.n_km = n_km
        self.modelo = modelo
    def __repr__(self):
        return repr((self.placa, self.n_km, self.modelo))



mat_const = Empresa('33.444.999/0001-88','ConstruForte')
mat_const.cadastrar_funcionario(Funcionario('Maria', '111.111.111-11', 3456))
fun_antonio = Funcionario('Antônio', '222.222.222-22', 2345)
mat_const.cadastrar_funcionario(fun_antonio)
fun_ana = Funcionario('Ana', '333.333.333-33', 3345)
mat_const.cadastrar_funcionario(fun_ana)
fun_mozart =  Funcionario('Mozart','444.444.444-44', 5678)
mat_const.cadastrar_funcionario(fun_mozart)
print(mat_const.funcionarios)

funcionarios_ordenados = sorted(mat_const.funcionarios, key= lambda f: f.salario_bruto)
print(funcionarios_ordenados)

mat_const.cadastrar_veiculo(Veiculo('KGH-3456', 8000,'Caminhão'))
mat_const.cadastrar_veiculo(Veiculo('JHG-4567', 15000, 'Caminhonete'))
mat_const.cadastrar_veiculo(Veiculo('OLJ-5678', 6000, 'Furgão'))

veiculos_ordenados = sorted(mat_const.veiculos, key= lambda v : v.n_km, reverse=True)
print(veiculos_ordenados)
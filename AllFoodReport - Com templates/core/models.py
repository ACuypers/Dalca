from django.db import models
from django.contrib.auth.models import UserManager

class UsuariosFuncoesAdm(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, unique='True')  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True, unique='True')
    login = models.CharField(max_length=255, blank=True, null=True,unique=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    acessobackupbd = models.CharField(db_column='acessoBackupBD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    acessodownloadnotas = models.CharField(db_column='acessoDownloadNotas', max_length=1, blank=True, null=True)  # Field name made lowercase.
    is_anonymous = False
    is_authenticated = True
    is_staff = True
    is_superuser = True

    REQUIRED_FIELDS = ('id','login','senha')
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'usuarios_funcoes_adm'

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    razaosocial = models.CharField(db_column='razaoSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    end_point = models.CharField(max_length=100, blank=True, null=True)
    dnscloudaws = models.CharField(max_length=255, blank=True, null=True)
    datapadrao = models.CharField(max_length=1, blank=True, null=True)
    ultimaatualizacao = models.DateTimeField(blank=True, null=True)
    idcontador_fk = models.IntegerField(db_column='idContador_FK', blank=True, null=True)  # Field name made lowercase.
    versaousada = models.CharField(db_column='versaoUsada', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nomebasedadoscloud = models.CharField(max_length=255, blank=True, null=True)
    licencaativa = models.CharField(db_column='licencaAtiva', max_length=1, blank=True, null=True)  # Field name made lowercase.
    versaofull = models.CharField(db_column='versaoFull', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtde_backoffice = models.IntegerField(db_column='Qtde_BackOffice', blank=True, null=True)  # Field name made lowercase.
    qtde_pc = models.IntegerField(db_column='Qtde_Pc', blank=True, null=True)  # Field name made lowercase.
    qtde_micro_terminais = models.IntegerField(db_column='Qtde_Micro_Terminais', blank=True, null=True)  # Field name made lowercase.
    qtde_mobile = models.IntegerField(db_column='Qtde_Mobile', blank=True, null=True)  # Field name made lowercase.
    qtde_caixa = models.IntegerField(db_column='Qtde_Caixa', blank=True, null=True)  # Field name made lowercase.
    qtde_administrativo = models.IntegerField(db_column='Qtde_Administrativo', blank=True, null=True)  # Field name made lowercase.
    qtde_touch = models.IntegerField(db_column='Qtde_Touch', blank=True, null=True)  # Field name made lowercase.
    qtde_recepcao = models.IntegerField(db_column='Qtde_Recepcao', blank=True, null=True)  # Field name made lowercase.
    qtde_forcadevendas = models.IntegerField(db_column='Qtde_ForcaDeVendas', blank=True, null=True)  # Field name made lowercase.
    qtde_terminaldesaida = models.IntegerField(db_column='Qtde_TerminalDeSaida', blank=True, null=True)  # Field name made lowercase.
    qtde_terminaldeproducao = models.IntegerField(db_column='Qtde_TerminalDeProducao', blank=True, null=True)  # Field name made lowercase.
    qtde_moduloremoto = models.IntegerField(db_column='Qtde_ModuloRemoto', blank=True, null=True)  # Field name made lowercase.
    datahoraultimobackup = models.DateTimeField(db_column='dataHoraUltimoBackup', blank=True, null=True)  # Field name made lowercase.
    valortotalliquidototal = models.FloatField(db_column='valorTotalLiquidoTOTAL', blank=True, null=True)  # Field name made lowercase.
    qtdecomandaspagastotal = models.IntegerField(db_column='qtdeComandasPagasTOTAL', blank=True, null=True)  # Field name made lowercase.
    ticketmedioglobalatual = models.FloatField(db_column='ticketMedioGlobalAtual', blank=True, null=True)  # Field name made lowercase.
    valorsf = models.FloatField(db_column='valorSF', blank=True, null=True)  # Field name made lowercase.
    percsf = models.FloatField(db_column='percSF', blank=True, null=True)  # Field name made lowercase.
    bloquearsf = models.CharField(db_column='bloquearSF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'

    def __int__(self):
        return self.cnpj

    REQUIRED_FIELDS = ('id', 'razaosocial', 'cnpj')

    objects = UserManager()


class Usuario(models.Model):
    #settings.AUTH_USER_MODE talveztera que usar aqui no usuario comum
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=255, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.usuario

    REQUIRED_FIELDS = ('id', 'usuario', 'senha','idempresa_fk')
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []

    objects = UserManager()

###########################################################################################

class Cancelamento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    qtdecomanda = models.IntegerField(blank=True, null=True)
    qtdeitens = models.IntegerField(blank=True, null=True)
    qtdeadicionais = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    idempresa_fk = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancelamento'


class Comanda(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    itensvenda = models.FloatField(blank=True, null=True)
    descitensvenda = models.FloatField(blank=True, null=True)
    servico = models.FloatField(blank=True, null=True)
    adicional = models.FloatField(blank=True, null=True)
    desconto = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    qtdepessoa = models.IntegerField(blank=True, null=True)
    totalestimado = models.FloatField(blank=True, null=True)
    totalqtdepessoa = models.IntegerField(blank=True, null=True)
    totalcomandas = models.IntegerField(blank=True, null=True)
    idempresa_fk = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comanda'


class Desconto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    qtdeitens = models.IntegerField(blank=True, null=True)
    qtdeadicionais = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    idempresa_fk = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desconto'


class Mesa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    livre = models.IntegerField(blank=True, null=True)
    aberta = models.IntegerField(blank=True, null=True)
    emconta = models.IntegerField(blank=True, null=True)
    ticketmedio = models.FloatField(blank=True, null=True)
    ativas = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa'


class Ocorrencia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    totalcancelamento = models.FloatField(blank=True, null=True)
    totaldesconto = models.FloatField(blank=True, null=True)
    totalsangria = models.FloatField(blank=True, null=True)
    totalreforco = models.FloatField(blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocorrencia'


class RecebimentoCaixa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    totalrecebido = models.FloatField(blank=True, null=True)
    totalreceber = models.FloatField(blank=True, null=True)
    caixasabertos = models.IntegerField(blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recebimento_caixa'


class Reforco(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    qtdetroco = models.IntegerField(blank=True, null=True)
    totaltroco = models.FloatField(blank=True, null=True)
    qtdependura = models.IntegerField(blank=True, null=True)
    totalpendura = models.FloatField(blank=True, null=True)
    qtdecreditocliente = models.IntegerField(blank=True, null=True)
    totalcreditocliente = models.FloatField(blank=True, null=True)
    qtdecreditoprepago = models.IntegerField(blank=True, null=True)
    totalcreditoprepago = models.FloatField(blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reforco'


class Sangria(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    qtde = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    idempresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangria'





#################################TALVEZ NAO USE
class Contadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=30, blank=True, null=True)
    crc = models.CharField(max_length=50, blank=True, null=True)
    cnpj = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contadores'


class Syncrealtime(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idempresa_fk = models.IntegerField(db_column='idEmpresa_Fk', blank=True, null=True)  # Field name made lowercase.
    datahoraultimaverificacao = models.DateTimeField(db_column='dataHoraUltimaVerificacao', blank=True, null=True)  # Field name made lowercase.
    quantidadenotasparadas = models.CharField(db_column='QuantidadeNotasParadas', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syncrealtime'

class Logbd(models.Model):
    idlog = models.AutoField(primary_key=True)
    datahora = models.DateTimeField(blank=True, null=True)
    bancodados = models.CharField(db_column='bancoDados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbd'
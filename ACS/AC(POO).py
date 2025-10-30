class PosGraduacao:
    def __init__(self,insituicao,curso):
        self.instituicao = insituicao
        self.curso = curso

    def get_curso(self):
        return 'Doutorado em '+ (self.curso)   
     
class Doutorado(PosGraduacao):
    def __init__(self, insituicao, curso,tese=None):
        super().__init__(insituicao, curso)
        self.__tese = tese
        

    def get_tese(self):
        return self.__tese

    def set_tese(self,tese):
        self.__tese = tese


pessoa = Doutorado('Impacta', 'ADS')
pessoa.get_tese()

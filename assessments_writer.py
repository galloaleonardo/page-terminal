from file_maker import MakeReportPatient
import datetime


class AssessmentsWriterFile:
    lines_header_file_gerontologian = []
    lines_header_file_patient = []

    @staticmethod
    def inicializate_write(gerontologian, patient):
        file = MakeReportPatient()
        file.open_file(patient)
        AssessmentsWriterFile.header_file_gerontologian(gerontologian)
        AssessmentsWriterFile.header_file_patient(patient)

        file.write_header(AssessmentsWriterFile.lines_header_file_gerontologian,
                          AssessmentsWriterFile.lines_header_file_patient)

    @staticmethod
    def header_file_gerontologian(gerontologian):
        AssessmentsWriterFile.\
            lines_header_file_gerontologian.append('1. INFORMAÇŌES SOBRE O ENTREVISTADOR(A)')
        AssessmentsWriterFile.\
            lines_header_file_gerontologian.append('Serviço/Instituição: XUSP')
        AssessmentsWriterFile.\
            lines_header_file_gerontologian.append('Entrada no serviço: %s' % str(datetime.datetime.now()))
        AssessmentsWriterFile.\
            lines_header_file_gerontologian.append('Entrevistado: Idoso')
        AssessmentsWriterFile.\
            lines_header_file_gerontologian.append('Entrevistador(a) gerontologo(a): %s' % gerontologian.p_name)

    @staticmethod
    def header_file_patient(patient):
        AssessmentsWriterFile.lines_header_file_patient.append('2. DADOS DE IDENTIFICAÇÃO DO PACIENTE')
        AssessmentsWriterFile.lines_header_file_patient.append('Nome: %s' % patient.p_name)

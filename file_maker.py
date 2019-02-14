import os


class MakeReportPatient:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.f = None
        self.lines_attitude = []
        self.lines_quality = []

    @staticmethod
    def open_file(patient):
        return open(MakeReportPatient.BASE_PATH + '/reports/' + patient.p_name, 'w+')

    def write_file_patient(self, lines_attitude, lines_quality):
        self.f = self.open_file()
        MakeReportPatient.write_attitude_issues(self, lines_attitude)
        MakeReportPatient.write_quality_issues(self, lines_quality)
        self.f.close()

    def write_attitude_issues(self, lines):
        self.lines_attitude = lines
        self.f.write(lines)

    def write_quality_issues(self, lines):
        self.lines_quality = lines
        self.f.write(lines)

    def write_header(self, lines_g, lines_p):
        self.f.write(lines_g)
        self.f.write(lines_p)

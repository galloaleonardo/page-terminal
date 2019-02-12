class Gerontologian:
    def __init__(self, name, num_abg):
        self.g_name = name
        self.g_num_abg = num_abg


class Patient:
    def __init__(self, name, birth, sex, marital_status, schooling, ocupation,
                 home_with, income, bpc, b_religion, religion_name):
        self.p_name = name
        self.p_birth = birth
        self.p_sex = sex
        self.p_marital_status = marital_status
        self.p_schooling = schooling
        self.p_ocupation = ocupation
        self.p_home_with = home_with
        self.p_income = income
        self.p_bpc = bpc
        self.p_religion = b_religion
        self.p_religion_name = religion_name
        self.p_score_attitudes_aging = None
        self.p_score_quality_life = []

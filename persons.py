class Person:
    def __init__(self, primary_name, last_name):
        self._primary_name = primary_name
        self._last_name = last_name

    @property
    def full_name(self):
        return '{} {}'.format(self._primary_name, self._last_name)


class Gerontologian(Person):
    def __init__(self, primary_name, las_name, num_membership_abg, service_institution,
                 is_elderly_interviewee, evaluation_date):
        super().__init__(primary_name, las_name)
        self._num_membership_abg = num_membership_abg
        self._service_institution = service_institution
        self._is_elderly_interviewee = is_elderly_interviewee
        self._evaluation_date = evaluation_date


class Patient(Person):
    def __init__(self, primary_name, last_name, adress, telephone, date_birth,
                 age, genre, marital_status, scholarity, years_scholarity,
                 retired, retired_pensioner, paid_work, individual_income,
                 family_income, live_with, have_relegion):
        super().__init__(primary_name, last_name)
        self._adress = adress
        self._telephone = telephone
        self._date_birth = date_birth
        self._age = age
        self._genre = genre
        self._marital_status = marital_status
        self._scholarity = scholarity
        self.years_scholarity = years_scholarity
        self.retired = retired
        self.retired_pensioner = retired_pensioner
        self.paid_work = paid_work
        self._individual_income = individual_income
        self._family_income = family_income
        self._live_with = live_with
        self._have_religion = have_relegion


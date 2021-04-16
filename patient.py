from patient_mockdb import PatientMockDB
from patient_utils import get_one_year_ago, calc_bmi, calc_blood_pressure


class Patient:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.patient_info = self.get_patient_info()
        if self.patient_info:
            self.physician_info = self.get_physician_info()
        else:
            raise ValueError

    def get_summary(self, today: str) -> str:
        start_date = get_one_year_ago(today)
        if not start_date:
            return {}

        numerical_diagnostic_data = self.get_numerical_diagnostics(start_date, today)
        visits = self.get_visits(start_date, today)
        bmi = calc_bmi(numerical_diagnostic_data)
        blood_pressure = calc_blood_pressure(numerical_diagnostic_data)

        return {
            'personal info': self.patient_info,
            'physician info': self.physician_info,
            'visits': visits,
            'bmi': bmi,
            'blood pressure': blood_pressure,
        }

    def get_visits(self, start_date: str, end_date: str) -> list:
        return PatientMockDB.get_visits(self.patient_id, start_date, end_date)

    def get_patient_info(self) -> dict:
        return PatientMockDB.get_patient_info(self.patient_id)

    def get_physician_info(self) -> dict:
        return PatientMockDB.get_physician_info(self.patient_info['physician_id'])

    def get_numerical_diagnostics(self, start_date: str, end_date: str) -> list:
        return PatientMockDB.get_numerical_diagnostics(self.patient_id, start_date, end_date)


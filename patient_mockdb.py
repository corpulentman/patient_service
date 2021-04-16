class PatientMockDB:
    def __init__(self):
        pass

    @staticmethod
    def get_patient_info(_patient_id: int) -> dict:
        result = [
            {'first_name': 'Jane',
             'last_name': 'Doe',
             'phone_number': '1234567890',
             'gender': 'F',
             'participate_in_study': True,
             'physician_id': 7252},
        ]
        return result[0] if result else {}

    @staticmethod
    def get_visits(_patient_id: int, _start_date: str, _end_date: str) -> list:
        return ['20200301', '20200401', '20200501']

    @staticmethod
    def get_physician_info(_physician_id: int) -> dict:
        result = [
            {'first_name': 'Enaj',
             'last_name': 'Eod',
             'phone_number': '0987654321'}
        ]
        return result[0] if result else {}

    @staticmethod
    def get_numerical_diagnostics(_patient_id: int, _start_date: str, _end_date: str) -> list:
        result = [
            {'date': '20200301',
             'type': 'weight',
             'value': 171},
            {'date': '20200301',
             'type': 'height',
             'value': 80},
            {'date': '20200301',
             'type': 'blood pressure',
             'value': 120},
            {'date': '20200401',
             'type': 'weight',
             'value': 181},
            {'date': '20200401',
             'type': 'height',
             'value': 80},
            {'date': '20200401',
             'type': 'blood pressure',
             'value': 130},
            {'date': '20200501',
             'type': 'weight',
             'value': 185},
            {'date': '20200501',
             'type': 'height',
             'value': 80},
            {'date': '20200501',
             'type': 'blood pressure',
             'value': 135},
        ]
        return result

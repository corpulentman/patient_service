from patient import Patient
from patient_utils import calc_bmi


def test_good_patient_id():
    p = Patient(123)
    r = p.get_summary('20121108')
    assert r['personal info']['first_name'] == 'Jane'
    assert r['physician info']['first_name'] == 'Enaj'
    assert r['blood pressure'] != []
    assert r['bmi'] != []
    assert r['visits'] != []


def test_bad_patient_id():
    # with pytest we can do something like
    # with pytest.raises(ValueError):
    #     p = Patient(0)
    pass


def test_patient_with_missing_weights():
    diagnostics = [
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
    ]
    r = calc_bmi(diagnostics)
    assert len(r) == 1
    assert r[0]['date'] == '20200401'


def test_patient_with_missing_height():
    diagnostics = [
        {'date': '20200301',
         'type': 'weight',
         'value': 171},
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
    ]
    r = calc_bmi(diagnostics)
    assert len(r) == 1
    assert r[0]['date'] == '20200401'


def test_patient_with_zero_height():
    diagnostics = [
        {'date': '20200301',
         'type': 'weight',
         'value': 171},
        {'date': '20200301',
         'type': 'blood pressure',
         'value': 120},
        {'date': '20200401',
         'type': 'weight',
         'value': 181},
        {'date': '20200401',
         'type': 'height',
         'value': 0},
        {'date': '20200401',
         'type': 'blood pressure',
         'value': 130},
    ]
    r = calc_bmi(diagnostics)
    assert len(r) == 0


if __name__ == '__main__':
    test_good_patient_id()
    test_patient_with_missing_height()
    test_patient_with_missing_weights()
    test_patient_with_zero_height()

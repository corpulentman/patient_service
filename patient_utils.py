from datetime import datetime, timedelta


def get_one_year_ago(today: str):
    end_date_obj = datetime.strptime(today, '%Y%m%d')
    start_date_obj = end_date_obj + timedelta(days=-365)
    return start_date_obj.strftime('%Y%m%d')


def calc_bmi(diagnostics):
    heights = _get_numerical_entry_by_type(diagnostics, 'height')
    weights = _get_numerical_entry_by_type(diagnostics, 'weight')

    bmi = []
    for dt, height in heights.items():
        if dt in weights:
            if height and height != 0.0:
                bmi.append({'date': dt, 'bmi': 703 * weights[dt] / (height**2)})
    return bmi


def calc_blood_pressure(diagnostics: list):
    bp = _get_numerical_entry_by_type(diagnostics, 'blood pressure')
    return [{'date': k, 'blood pressure': v} for k, v in bp.items()]


def _get_numerical_entry_by_type(diagnostics: list, measurement_type: str):
    return {entry['date']: entry['value'] for entry in diagnostics if entry['type'] == measurement_type}
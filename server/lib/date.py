import datetime as dt

def convert_date(d: str) -> dt.date:
    return dt.datetime.strptime(d, '%Y-%m-%d').date()

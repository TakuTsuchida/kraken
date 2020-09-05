import datetime as dt

def str2date(d: str) -> dt.date:
    return dt.datetime.strptime(d, '%Y-%m-%d').date()

def date2str(d) -> str:
    return d.strftime('%Y-%m-%d')

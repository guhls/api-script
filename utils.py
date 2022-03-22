from credentials.creds import get_creds
from googleapiclient.discovery import build
import pandas as pd
import datetime as dt
import unidecode

service_admin = build('admin', 'directory_v1', credentials=get_creds())
service_sheets = build('sheets', 'v4', credentials=get_creds())

with open('asset/nomes.csv', 'r') as file:
    df = pd.read_csv(file)

names = df['first_name'].squeeze()
extra_names = pd.Series(['TACCIANE'])
names_ibge = names.append(extra_names).to_list()


def is_user(name):
    firstname = unidecode.unidecode(name)
    firstname = firstname.split()
    if firstname[0].upper().strip() in names_ibge:
        return True
    else:
        return False


def in_zarpo(last_login):
    format_time = '%Y-%m-%dT%H:%M:%S.%fZ'

    last_login = dt.datetime.strptime(last_login, format_time)
    today = dt.date.today()

    if last_login.date() > today - dt.timedelta(days=30):
        return True
    else:
        return False


def last_date(my_date):
    format_time = '%Y-%m-%dT%H:%M:%S.%fZ'
    today = dt.datetime.today()
    count_days = today - dt.datetime.strptime(my_date, format_time)
    return count_days.days + 1

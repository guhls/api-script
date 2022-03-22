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
extra_names = pd.Series(['TACCIANE', 'NUMA'])
names = names.append(extra_names).to_list()


def is_user(email):
    login = email[:email.index('@')]
    if login.split('.')[0].upper() in names:
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

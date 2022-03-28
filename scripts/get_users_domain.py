from utils import service_sheets, is_user, in_zarpo, last_date, get_users


def update_users():
    users = get_users()
    list_users = []

    for user in users:
        list_users.append(
            [user['name']['fullName'],
             user['primaryEmail'],
             user['isEnrolledIn2Sv'],
             "Pessoa" if is_user(user['name']['givenName']) else "Genérico",
             "Sim" if in_zarpo(user['lastLoginTime']) else f"{last_date(user['lastLoginTime'])} dias"]
        )

    sheet = service_sheets.spreadsheets()

    sheet.values().clear(
        spreadsheetId='146flzoz76LlNxhULcywM_Qjl9fvEaCakZ_Rlnl75X1g',
        range='users!A2:E',
    ).execute()

    sheet.values().update(
        spreadsheetId='146flzoz76LlNxhULcywM_Qjl9fvEaCakZ_Rlnl75X1g',
        range='users!A2:E',
        valueInputOption='USER_ENTERED',
        body={"values": list_users}
    ).execute()


if __name__ == '__main__':
    update_users()

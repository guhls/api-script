from utils import get_groups, service_sheets


def update_groups():
    # users = get_users()
    # dict_groups = {}
    #
    # for user in users:
    #     groups = get_groups(user['primaryEmail'])
    #     if groups is not None:
    #         for group in groups:
    #             if group['email'] in dict_groups:
    #                 dict_groups[group['email']] += [user['primaryEmail']]
    #             else:
    #                 dict_groups[group['email']] = [user['primaryEmail']]
    #
    # list_final = []
    # for key, values in dict_groups.items():
    #     list_values = values
    #     list_values = [key] + list_values
    #     list_final.append(list_values)

    groups = [[groups['name'], groups['email']] for groups in get_groups(None)]

    sheet = service_sheets.spreadsheets()

    sheet.values().clear(
        spreadsheetId='146flzoz76LlNxhULcywM_Qjl9fvEaCakZ_Rlnl75X1g',
        range='groups!A2:B',
    ).execute()

    sheet.values().update(
        spreadsheetId='146flzoz76LlNxhULcywM_Qjl9fvEaCakZ_Rlnl75X1g',
        range='groups!A2:B',
        valueInputOption='USER_ENTERED',
        body={"values": groups}
    ).execute()


if __name__ == '__main__':
    update_groups()

current_users = ['mr.freaky47', 'John', 'Big Rick', 'Bigger Rick', 'alex']
new_users = ['John', 'Bigger Rick', 'Biggest Rick', 'mark', 'glop']
for new_user in new_users:
    if new_user in current_users:
        print(f"the name {new_user} is not availible")
    else:
        print(f"the name {new_user} is availible")
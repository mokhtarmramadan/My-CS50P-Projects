amount_due = 50
insert_coin = 0

print(f"Amount due:{amount_due}")
insert_coin = input("Insert coin: ")

while insert_coin != amount_due and amount_due != 0:
    if insert_coin in ['5', '10', '25']:
        amount_due = amount_due - int(insert_coin)
        if amount_due > 0:
            print(f"Amount due:{amount_due}")
        elif amount_due < 0:
            change_owed = abs(amount_due)
            print(f"Change owed:{change_owed}")
            break
        else:
            print(f"Amount due:{amount_due}")
            break

        insert_coin = input("Insert coin: ")
    while not insert_coin in ['5', '10', '25']:
        print(f"Amount due:{amount_due}")
        insert_coin = input("Insert coin: ")
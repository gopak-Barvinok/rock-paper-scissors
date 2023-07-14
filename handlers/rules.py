async def check_winner(move_1: dict, move_2: dict) -> list or bool:
    for username1, values1 in move_1.items():
        for username2, values2 in move_2.items():
            for key1, value1 in values1.items():
                for key2, value2 in values2.items():

                    value11 = value1.replace("move_", "")
                    value22 = value2.replace("krb_", "")

                    if value11 == 'stone' and value22 == 'scissors'\
                    or value11 == 'stone' and value22 == 'well'\
                    or value11 == 'paper' and value22 == 'stone'\
                    or value11 == 'paper' and value22 == 'well'\
                    or value11 == 'scissors' and value22 == 'paper'\
                    or value11 == 'well' and value22 == 'scissors':
                        return [username1, key1]
    
                    elif value11 == 'stone' and value22 == 'paper'\
                    or value11 == 'paper' and value22 == 'scissors'\
                    or value11 == 'scissors' and value22 == 'stone'\
                    or value11 == 'scissors' and value22 == 'well'\
                    or value11 == 'well' and value22 == 'stone'\
                    or value11 == 'well' and value22 == 'paper':
                        return [username2, key2]

                    elif value11 == value22:
                        return False
def view_history():

    try:

        with open("transactions.txt", "r") as file:

            lines = file.readlines():

        return lines

    except FileNotFoundError:

        return []

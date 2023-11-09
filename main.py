import colorama

def get_data():
    data = []
    data_file = open("data.txt", encoding='UTF-8')
    game_data_strings = data_file.readlines()
    for game in game_data_strings:
        game_data = game.split("|")
        game_dict = {"name":game_data[0],
                     "release":int(game_data[1]),
                     "price":float(game_data[2]),
                     "total_sales": int(game_data[3])}
        data.append(game_dict)
    return data


def main():
    our_game_data = get_data()
    while True:
        print_menu()
        selection = input("Enter the number of your choice:")
        if selection == '2':
            highest_revenue_game = find_highest_average_game(our_game_data)
            print(f"{highest_revenue_game['name']} made the most money per year")
        elif selection == '1':
            pass
        elif selection == '3':
            break
        else:
            print("Invalid input")


def find_highest_average_game(all_games):
    highest_so_far = all_games[0]
    for game in all_games:
        age = 2024-game['release']
        revenue_per_year = game['total_sales']/age
        age_of_highest = 2024-highest_so_far['release']
        highest_revenue_per_year = highest_so_far["total_sales"]/age_of_highest
        if revenue_per_year > highest_revenue_per_year:
            highest_so_far = game
    return highest_so_far
def print_menu():
    menu = """
    [1]add a game
    [2]Find highest average revenue per year 
    [3]Quit
    """
    print(colorama.Back.GREEN+menu)

main()
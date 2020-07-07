# Write your code here
import random


class RPC:
    user_score = 0
    win_position = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    def game(self):
        user_name = input('Enter your name: ')
        self.user_score = self.rating(user_name)
        self.win_position = self.set_user_options()
        print("Okay, let's start")
        options = ['rock', 'paper', 'scissors', '!exit', '!rating']
        while True:
            user_option = input()
            if user_option not in options:
                print('Invalid input')
            elif user_option == '!exit':
                print('Bye!')
                break
            elif user_option == '!rating':
                print(f'Your rating: {self.user_score}')
            else:
                print(self.result(user_option))

    # Функция считывает рейтинг из файла rating.txt. Если введенное имя пользователя находится в файле,
    # то игрок начинает с рейтингом, записанным в файл
    def rating(self, user_name):
        with open('rating.txt') as rating_file:
            lines = [(line.split()) for line in rating_file]
            users_rating = {user: score for user, score in lines}
        if user_name in users_rating:
            return int(users_rating[user_name])
        else:
            return 0

    # Функция отвечает за результат игры
    def result(self, user_option):
        computer_option = random.choice(list(self.win_position.keys()))
        if user_option == computer_option:
            self.user_score += 50
            return f'There is a draw ({computer_option})'
        elif computer_option in self.win_position[user_option]:
            self.user_score += 100
            return f'Well done. Computer chose {computer_option} and failed'
        elif user_option in self.win_position[computer_option]:
            return f'Sorry, but computer choose {computer_option}'

    # Функция отвечает за создание словаря, в котором находятся выигрышные комбинации
    def set_user_options(self):
        user_options = input('Input game options. If you want to play the classic "rock-paper-scissors", '
                             'just press " Enter"')
        if not user_options:
            return {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        user_options = user_options.split(',')
        len_ = len(user_options) // 2
        win_position = {}
        for option in user_options:
            idx = user_options.index(option)
            copy_ = user_options[idx + 1:] + user_options[:idx]
            lose_options = copy_[len_:]
            win_position[option] = lose_options
        return win_position


if __name__ == '__main__':
    my_game = RPC()
    my_game.game()

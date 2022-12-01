"""This is my Integration Project"""
__author__ = "Amanda Smith"
# In this program I hope to give the user a better understanding of the rules of lacrosse
# a workout plan to help become game ready
# and any other needed information about lacrosse
# It also includes calculations of important skill averages
# as well as calculations for drive time and gear

"""This function is checking to see if the input is a valid integer"""
"""The parameter prompt_text is a string"""
"""The Return type is an integer"""


def get_good_input_int(prompt_text):
    good_input = False
    while not good_input:
        try:
            input_value = int(input(prompt_text))
            good_input = True
        except ValueError:
            print("Error, Must be whole number.")
    return input_value


"""This function is checking to see if the input is a valid float"""
"""The parameter prompt_text is a string"""
"""The Return type is a float"""


def get_good_input_float(prompt_text):
    good_input = False
    while not good_input:
        try:
            input_value = float(input(prompt_text))
            good_input = True
        except ValueError:
            print("Error, Must be a number.")
    return input_value


def main():
    print("Hello!" * 10)
    # I used the string operator * to say hello ten times
    print("This is Everything you need to know about Women's Lacrosse!")
    name = input("What is your name? ")
    print("Welcome " + name)
    # I used the string operator + to join welcome and the variable name together
    print("Let's get started with some important rules and information!")
    prompt = "How many players do you think are on the field at once?"
    number_of_players_on_field = get_good_input_int(prompt)
    print(12 == number_of_players_on_field)
    print("The Correct Answer is 12")
    prompt = "Who is allowed in the goal crease, 1: the goalie 2: any player on the field"
    goal_circle_question = get_good_input_int(prompt)
    print(goal_circle_question == 1)
    print("The correct answer is 1, only the goalie")
    prompt = "How many players must stay behind the restraining line while the ball is at one end?"
    restraining_line = get_good_input_int(prompt)
    print(restraining_line == 4)
    print("The correct answer is 4")
    prompt = "How long is a defender allowed to stand in the 8 meter without being a sticks length away from an " \
             "attacker? "
    seconds_rule = get_good_input_int(prompt)
    print(seconds_rule == 3)
    print("The correct answer is 3 seconds")
    prompt = "What is the result of shooting space call in the 8 meter, 1: free possession 2: a free 8 meter shot"
    shooting_space = get_good_input_int(prompt)
    print(shooting_space == 2)
    print("The correct answer is 2, an 8 meter shot")

    prompt = "If you would like to see a fun fact type '2', if not type '1': "
    user_wants_to_learn = get_good_input_int(prompt)
    if user_wants_to_learn == 2:
        # I used == to determine if the input given was 2
        print("The modern rules of lacrosse date back to 1974")
        print("when they were drafted for a match between the Native American communities of Seneca and Mohawks.")
    # This fact was found on https://www.explosion.com/132077/8-interesting-facts-about-lacrosse-you-didnt-know/

    print("Now let's look at the total cost after buying equipment")
    print("to make these calculations suitable for you google or find prices of these items that you would like to buy")
    prompt = "Please enter your budget: "
    users_budget = get_good_input_float(prompt)
    prompt = "How much do the pair of goggles you want cost? "
    goggles = get_good_input_float(prompt)
    prompt = "How much does your mouth guard cost? "
    mouth_guard = get_good_input_float(prompt)
    prompt = "How much does that stick shaft you chose cost? "
    stick_shaft = get_good_input_float(prompt)
    prompt = "How much does the lacrosse stick head you chose cost? "
    stick_head = get_good_input_float(prompt)
    prompt = "How much do your cleats cost? "
    cleats = get_good_input_float(prompt)
    # I used + as addition to find the total cost of buying each item at said amount
    overall_total = cleats + stick_head + stick_shaft + mouth_guard + goggles
    print("Your total cost after purchasing all your lacrosse gear is: $", format(overall_total, '.2f'), sep="")
    # I used an if/else statement to tell the code which output to produce
    if overall_total > users_budget:
        print("This total is over your budget by ${:,.2f}".format(overall_total - users_budget))
    else:
        print("This total is under your budget by ${:,.2f}".format(users_budget - overall_total))

    print("Now let's go through a workout to get you game ready! ")
    print("This Workout should be completed in 1 hour or less")
    # I used flood division and modulus to do the mathematics
    # to show how many minutes and how many seconds each exercise should take
    print(60 // 5, "minutes", 60 % 5, "seconds, per exercise")
    print("This workout is easy to stay consistent with because it only takes 1 hour out of your", 24 - 1, "!")
    # I used - to show how many hours are left in the day after doing my lacrosse workout
    print("Start with 3 sets of 20 passes with each hand ")
    print(3 * 20, "reps")
    # I used * multiplication to show a total of reps
    print("Next do 50 ground ball pick ups in under 2 minutes", 120 / 60, "per second")
    # I used division to calculate how many reps per second
    print("Do 3 full field sprints twice so", 3 + 3, "total")
    # I used addition to show the total amount of sprints to complete
    print("Next practice shooting with 100 shots")
    print("Practice cradling the ball while running")
    print("Repeat all 5 exercises 5 times throughout the week so", 5 ** 2, "times total")
    # I used ** to raise 5 to the second power to show 5 times itself twice

    print("Lets start getting some statistics!")
    print("Set a timer for one minute and count how many shots you make")
    print("Repeat three times!")

    # I am assigning these variables values outside the for loop, so they exist
    # shooting_average = 0
    counter_of_shots = 0
    player_name_for_shooting = input("Enter your name: ")
    # I am using a for loop because I know how many values are going to be entered.
    for value_input in range(3):
        prompt = "Enter how many shots were made in one minute: "
        shots_per_minute = get_good_input_int(prompt)
        counter_of_shots += shots_per_minute
        # I am using the variable counter to count up the values going into the variable shots_per_minute
    shooting_average = counter_of_shots / 3
    print("Name:", player_name_for_shooting)
    print("Shooting Average:", format(shooting_average, '.2f'))
    # I used format '.2f' so the average only displays two decimal points

    if (shooting_average >= 0) and (shooting_average <= 25):
        print("This is a below average shooting average")
    elif not (shooting_average < 25):
        print("This is a great shooting average!")

    print("Now lets calculate your catching percentage")
    print("Play wall ball for one minute and count how many passes are caught")
    print("Type '-13' when you are done inputting caught passes")
    prompt = "Type number of caught passes: "
    num_of_caught_passes = get_good_input_int(prompt)
    counter_of_passes = 0
    # passing_average = 0
    num_of_times_user_trys = 0
    # I am using a while loop so the user can input as many numbers as they please
    # I am using != 3 to stop the code when the user inputs number 3
    while num_of_caught_passes != -13:
        counter_of_passes = counter_of_passes + num_of_caught_passes
        num_of_times_user_trys = num_of_times_user_trys + 1
        prompt = "Type number of caught passes: "
        num_of_caught_passes = get_good_input_int(prompt)
    passing_average = counter_of_passes / num_of_times_user_trys
    print("Passing Average:", format(passing_average, '.2f'))

    # I used if, elif, and else to have three different possible outcomes depending on the players score
    if 20 <= passing_average <= 40:
        print("This is a good passing average!")
    elif passing_average > 40:
        print("This is a great passing average!")
    else:
        print("This is a below average passing average")

    if (shooting_average > passing_average) or (shooting_average >= passing_average):
        print("Your shooting average is better or equal to your passing average")
    elif shooting_average < passing_average:
        print("Your passing average is greater than your shooting average")

    print("Now lets Calculate your ground ball average!")
    print("Set a timer for one minute and count how many ground ball pick ups")
    print("Repeat three times!")

    # ground_ball_average = 0
    counter_of_ground_balls = 0
    for ground_ball_input in range(3):
        prompt = "Enter how many ground ball pick ups in one minute: "
        ground_balls_per_minute = get_good_input_int(prompt)
        counter_of_ground_balls += ground_balls_per_minute
    ground_ball_average = counter_of_ground_balls / 3
    print("Ground Ball Average:", format(ground_ball_average, '.2f'))

    print("Lets calculate the total amount of time participating in a game takes")

    def total_amount_of_time_at_lax(game_time, half_time, warm_up, drive_time):
        total_time_spent = game_time + half_time + warm_up + drive_time
        return total_time_spent

    wu = 60
    prompt = "Enter your drive time to fields in minutes: "
    dt = get_good_input_int(prompt)
    gt = 50
    ht = 10
    overall_total_time_spent = total_amount_of_time_at_lax(gt, ht, wu, dt)
    # Tylor helped with this line of code
    print(overall_total_time_spent, "minutes is your total time spent")

    print("Lets calculate the amount of time spent per week at practices")
    prompt = "How many times per week does your team practice? "
    number_of_practices_per_week = get_good_input_int(prompt)
    prompt = "How many minutes is each practice? "
    minutes_of_each_practice = get_good_input_int(prompt)
    prompt = "How many minutes is the drive to your practice fields? "
    amount_of_time_to_drive_to_practice = get_good_input_int(prompt)
    total_time_one_practice = amount_of_time_to_drive_to_practice + minutes_of_each_practice
    amount_of_time_per_week_for_practice = total_time_one_practice * number_of_practices_per_week
    print("Amount of time spent per week for practice in minutes: ", amount_of_time_per_week_for_practice)
    game_and_practice_time = overall_total_time_spent + amount_of_time_per_week_for_practice

    print("The total amount of time spent in minutes per week with practices and a game: ", game_and_practice_time)
    game_and_practice_time_hours = game_and_practice_time // 60
    game_and_practice_time_minutes = game_and_practice_time % 60
    print(game_and_practice_time_hours, "hours and ", game_and_practice_time_minutes, "minutes")

    print("Thank you! You have completed Everything you need to know about lacrosse!")
    user_enjoyment = input("Did you Enjoy this program? Enter: 'yes' or 'no'")
    if user_enjoyment == 'yes':
        print("We are so happy you enjoyed this program!")
    elif user_enjoyment == 'no':
        print("We are sorry you did not enjoy this program :(")
    else:
        print('That input is not understood')


if __name__ == "__main__":
    main()

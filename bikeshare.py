import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }

def check_valid_input(user_input, valid_answers, common_alternatives):
    if user_input.lower() in valid_answers:
        return True, user_input
    #check if user input is one of the common alternative or misspelled names
    if user_input.lower() in common_alternatives:
        corrected_input = common_alternatives[user_input.lower()]
        print(f"We assume you mean {corrected_input.title()}")
        return True, corrected_input
    return False, user_input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    user_city = ""
    city = ""
    valid_city = ["chicago","new york city","washington"]
    common_city_alternatives = {
        "chitown": "chicago",
        "new york": "new york city",
        "nyc": "new york city",
        "dc": "washington",
        "washington d.c.": "washington",
        "washington dc": "washington",
        "chigaco": "chicago",
        "chcago": "chicago",
        "chigago": "chicago",
        "chciago": "chicago",
        "new yrok city": "new york city",
        "new yourk city": "new York City",
        "new yor city": "new York City",
        "washinton": "washington",
        "washingotn": "washington",
        "washngton": "washington",
        "wahsington": "washington"
    }
    is_valid_city = False
    while not is_valid_city:
        #have the user input is one of the cities for which we have data
        user_city = input("Which city's data would you like to explore (Chicago, New York City, or Washington))").lower().strip()
        is_valid_city, corrected_city = check_valid_input(user_city, valid_city, common_city_alternatives)
        if not is_valid_city:
            print("Please input the name one of these cities (Chicago, New York City, or Washington).")
        else:
            city = corrected_city
            print("Thank you!")
            
    print(f"You selected: {city.title()}")
    # get user input for month (all, january, february, ... , june)
    user_month = "" #initialize variables
    valid_month = ["january","february","march","april","may","june"]
    common_month_alternatives = {
        "janury": "january",
        "januray": "january",
        "janaury": "january",
        "janauary": "january",
        "jan": "january",
        "feburary": "february",
        "febuary": "february",
        "febrary": "february",
        "februray": "february",
        "febraury": "february",
        "feb": "february",
        "marh": "march",
        "mrach": "march",
        "mach": "march",
        "mar": "march",
        "aprl": "april",
        "apirl": "april",
        "aprile": "april",
        "apr": "april",
        "mai": "may",
        "mey": "may",
        "jue": "june",
        "jun": "june",
        "juin": "mune"
    }
    month = ["january","february","march","april","may","june"]
    selected_month = []
    print("You may choose to narrow the data down to a month or months")
    print("Not selecting any month will default to using data across all months")
    while True:
        user_month = input("Type a month and hit enter (January, February, March, April, May, or June). Type 'done' to finish)").lower().strip()
        if user_month == 'done':
            break
        is_valid_month, corrected_month = check_valid_input(user_month, valid_month, common_month_alternatives)
        if not is_valid_month:
            print("Please pick from these months? (January, February, March, April, May, or June).")
        else:
            selected_month.append(corrected_month)
            print("Thank you! Would you like to select another month?")
    if selected_month:
        month = selected_month
    print(f"You selected: {" ".join(month).title()}")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ["monday","tueday","wednesday","thursday","friday","saturday","sunday"]
    user_day = ""
    selected_day = []
    valid_day = ["monday","tueday","wednesday","thursday","friday","saturday","sunday"]
    common_day_alternatives = {
        "monady": "monday",
        "mondy": "monday",
        "munday": "monday",
        "monay": "monday",
        "mon": "monday",
        "mo": "monday",
        "m": "monday",
        "tusday": "tuesday",
        "tuseday": "tuesday",
        "tuesady": "tuesday",
        "tuesdy": "tuesday",
        "tues": "tuesday",
        "tu": "tuesday",
        "wensday": "wednesday",
        "wedensday": "wednesday",
        "wednsday": "wednesday",
        "wendsday": "wednesday",
        "wed": "wednesday",
        "we": "wednesday",
        "w": "wednesday",
        "thrusday": "thursday",
        "thurday": "thursday",
        "thursady": "thursday",
        "thurdsay": "thursday",
        "thurs": "thursday",
        "thur": "thursday",
        "thu": "thursday",
        "th": "thursday",
        "firday": "friday",
        "fridy": "friday",
        "firady": "friday",
        "fryday": "friday",
        "fri": "friday",
        "fr": "friday",
        "saterday": "saturday",
        "satuday": "saturday",
        "satrday": "saturday",
        "saturdy": "saturday",
        "sat": "saturday",
        "sa": "saturday",
        "sundy": "sunday",
        "sundey": "sunday",
        "sunady": "sunday",
        "sundday": "sunday",
        "sund": "sunday",
        "sun": "sunday",
        "su": "sunday"
    }
    print("You may choose to narrow the data down to a day or days of the week")
    print("Not selecting any day will default to using data across all days of the week")
    while True:
        user_day = input("Type a day and hit enter (Monday, Tuesday, Wednesday, Thursday, Friday,Saturday, or Sunday). Type 'done' to finish)").lower().strip()
        if user_day == 'done':
            break
        is_valid_day, corrected_day = check_valid_input(user_day, valid_day, common_day_alternatives)
        if not is_valid_day:
            print("Please pick from these days? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday).")
        else:
            selected_day.append(corrected_day)
            print("Thank you! Would you like to select another day?")
    if selected_day:
        day = selected_day
    print(f"You selected: {" ".join(day).title()}")

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
#        df = load_data(city, month, day)
        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

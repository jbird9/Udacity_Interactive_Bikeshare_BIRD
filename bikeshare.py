import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }

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
    user_input = ""
    valid_answers = ["chicago","new york city","washington"]
    common_alternatives = {
        "chitown" : "chicago",
        "new york" : "new york city",
        "nyc" : "new york city",
        "dc" : "washington",
        "washington d.c." : "washington",
        "washington dc" : "washington"
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
    while not check_valid_input(user_input, valid_answers):
        #check if user input is one of the cities for which we have data
        if user_input in valid_answers:
            return True
        #check if user input is one of the common alternative or misspelled names
        if user_input.lower() in common_alternatives:
            corrected_input = common_alternatives[user_input.lower()]
            print(f"We assume you mean {corrected_input}.title(), right?")
            return True
        return False
        if not check_valid_input(user_input, valid_answers):
            print("Please input either Chicago, New York City, or Washington")
        else:
            print(f"{user_input}.title()")
    user_input = input("Which city's data would you like to explore (Chicago, New York City, or Washington))").lower().strip()
    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
 #   return city, month, day
    return city


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
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

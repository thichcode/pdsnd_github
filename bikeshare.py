import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. editor by thuongdv2

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the name of the city (Chicago, New York City, Washington): ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the  name of the month (all, january, february, ... , june): ").lower()
        if month in ['all', 'january', 'february', 'march','april','may','june']:
            break
        else:
            print("Invalid input. Please try again.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the  day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print("Invalid input. Please try again.")

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
    # Load the data into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract the month and day of the week from the 'Start Time' column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter the data by month if applicable
    if month != 'all':
        # Convert the month input to the corresponding month number
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter the data by the selected month
        df = df[df['Month'] == month]

    # Filter the data by day of the week if applicable
    if day != 'all':
        # Filter the data by the selected day
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # Calculate the most common month
    most_common_month = df['Month'].mode()[0]

    # Convert the month number to the corresponding month name
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month_name = months[most_common_month - 1]

    print("The most common month is:", most_common_month_name)

    # display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]

    print("The most common day of the week is:", most_common_day)

    # display the most common start hour
    # Extract the hour from the 'Start Time' column
    df['Hour'] = df['Start Time'].dt.hour

    # Calculate the most common start hour
    most_common_hour = df['Hour'].mode()[0]

    print("The most common start hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    print("The most commonly used start station is:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print("The most commonly used end station is:", most_common_end_station)

    # display most frequent combination of start station and end station trip
    start_end_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print("The most frequent combination of start station and end station trip is:", start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    # Calculate the total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("The total travel time is:", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()

    print("Counts of user types:", user_type_counts)

    # Display counts of gender
    # Check if 'Gender' column exists in the DataFrame
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:", gender_counts)

    # Display earliest, most recent, and most common year of birth
    # Check if 'Birth Year' column exists in the DataFrame
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print("\nThe earliest year of birth is:", earliest_year)
        print("The most recent year of birth is:", most_recent_year)
        print("The most common year of birth is:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """Raw data is displayed upon request by the user."""
    #ask the user whether he wants to see first 5 rows of data
    while True:
        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no?\n")
        if view_data.lower() != 'yes':
            break
        #ask the user whether he wants to see next 5 rows of data. Keep asking until he says no
        start_loc = 0
        while True:   
            print(df.iloc[start_loc:start_loc+5])
            view_display = input("\nDo you want to see the next 5 rows of data? Enter/yes or no? \n")
            if view_display.lower() == 'no':
                break
            start_loc += 5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

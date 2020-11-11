import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Enter one of the following cities Chicago, New York City or Washington: \n")).lower()
    while city not in CITY_DATA.keys():
        print("Thats not a city we have data for or you misspelled. Please try Chicago, New York City or Washington\n")
        city = str(input("Enter one of the following cities Chicago, New York City or Washington:\n ")).lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("\nIf you want to filter the data by a specific month enter 'january', 'february', 'march', 'april', 'may' or 'june'. If you dont want to filter by month enter 'all': \n")).lower()
    while month not in MONTH_DATA:
        print("Thats not a month we have data for or you misspelled. Please try 'january', 'february', 'march', 'april', 'may' or 'june'\n")
        month = str(input("\nIf you want to filter the data by a specific month enter 'january', 'february', 'march', 'april', 'may' or 'june'. If you dont want to filter by month enter 'all': \n")).lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("\nIf you want to filter the data by a weekday enter 'monday', 'tuesday', ... or 'sunday'. If you dont want to filter by day enter 'all': \n")).lower()
    while day not in DAY_DATA:
        print("Thats not a weekday or you misspelled. We have data for, please try 'monday', 'tuesday', ... or 'sunday'\n")
        day = str(input("\nIf you want to filter the data by a weekday enter 'monday', 'tuesday', ... or 'sunday'. If you dont want to filter by day enter 'all': \n")).lower()
    print('\nProcessing data and your filters! Please stay seated. \n')
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_med = df['month'].median()
    print('Most common month: ' + str(int(month_med)))
    # here happens somethin with the day of the week
    dayofweek_com = df['day_of_week'].mode()
    print('Most common day of week: ' + str(dayofweek_com).strip("0"))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour_med = df['hour'].mode()
    print('Most common start hour: ' + str(start_hour_med).strip("0"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_com = df['Start Station'].mode()
    print('Most common start station: ' + str(start_station_com).strip("0"))

    # TO DO: display most commonly used end station
    end_station_com = df['End Station'].mode()
    print('Most common end station: ' + str(end_station_com).strip("0"))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_comb'] = df['Start Station'] + " to " + df['End Station']
    station_comb_com = df['station_comb'].mode()
    print('Most common frequent combination of start station and end station trip: ' + str(station_comb_com).strip("0"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    # INFO: The if clause was taken from the Udacity Knowledge Base
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)

    else:
        print("Gender column does not exists.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        birthyear_min = df['Birth Year'].min()
        birthyear_max = df['Birth Year'].max()
        birthyear_med = df['Birth Year'].median()
        print('Earliest year of birth: ' + str(int(birthyear_min)))
        print('Most recent year of birth: ' + str(int(birthyear_max)))
        print('Most common year of birth: ' + str(int(birthyear_med)))

    else:
        print("Birth Year column does not exists.")

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
        record_no = 5

        #INFO: The following code was taken from the Udacity Knowledge Base and got slightly modified to specify user input and display all raw data
        user_input = input('\nWould you like to see more data? Please enter yes or no:\n').lower()
        if user_input in ('yes', 'y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
                if more_data not in ('yes', 'y'):
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
    df = pd.read_csv(city.replace(' ', '_') + '.csv')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

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
    correct_input = False

    while correct_input == False:
        city = str(input('What cities\' data would you like to explore (Chicago, New York City, or Washington)? ')).lower()

    # get user input for month (all, january, february, ... , june)
        month = str(input('Which month\'s data would you like to explore (all, January, February, ... , June)? ')).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input('Which day\'s data would you like to explore (all, Monday, Tuesday, ... Sunday)? ')).lower()

        if (city == "chicago" or city == "new york city" or city == "washington") and (month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june') and (day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday'):
            correct_input = True
        else:
            print('Ooops, some inputs did not match with the expected values. Please try again.')

    print('-'*40)
    return city, month, day





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_dict = {'1' : 'January',
                  '2' : 'February',
                  '3' : 'March',
                  '4' : 'April',
                  '5' : 'May',
                  '6' : 'June'
                  }

    max_month = df['month'].value_counts().index[0]
    max_month_occur = df['month'].value_counts().max()


    print('The most common MONTH is ' + month_dict[str(max_month)] + ' with ' + str(max_month_occur) + ' Times of Travel.')

    # display the most common day of week
    max_day = df['day_of_week'].value_counts().index[0]
    max_day_occur = df['day_of_week'].value_counts().max()

    print('The most common DAY is ' + max_day + ' with ' + str(max_day_occur) + ' Times of Travel.')

    # display the most common start hour
    max_hour = df['Start Time'].dt.hour.value_counts().index[0]
   # print(max_hour.value_counts().index[0])

    print('The most common STARTING HOUR is ' + str(max_hour) + ' hours.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    max_start_station = df['Start Station'].value_counts().index[0]
    print('The most commonly used START STATION is: ' + max_start_station)

    # display most commonly used end station
    max_end_station = df['End Station'].value_counts().index[0]
    print('The most commonly used END STATION is: ' + max_end_station)

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time() # required to calculate runtime duration

    # display total travel time
    print('TOTAL travel time is approximately: ' + str(df['Trip Duration'].sum()/(3600)) + ' hours.')

    # display mean travel time
    print('MEAN travel time is approximately: ' + str(df['Trip Duration'].mean()/60) + ' minutes.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except:
        print('Unfortunately, there is no Gender data for this city available')

    # Display earliest, most recent, and most common year of birth
    try:
        print('EARLIEST year of birth is: ' + str(int(df['Birth Year'].min())))
        print('Most RECENT year of birth is: ' + str(int(df['Birth Year'].max())))
        print('Most COMMON year of birth is: ' + str(int(df['Birth Year'].value_counts().index[0])))
    except:
        print('Unfortunately, there is no Birth Year data for this city available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def print_raw_data(df):
    answer_correct = False

    while answer_correct == False:
        answer = str(input('Would you like to see individual trip raw data (yes or no)? ')).lower()
        if answer == 'yes' or answer == 'no':
            answer_correct = True
        else:
            print('You provided an incorrect input, please type either yes or no.')

    print('-'*40)
    loop = int(0)
    while answer == 'yes':
        answer_correct = False
        for i in range(5):
            try:
                print('Trip Number: ' + str(df.iloc[loop + i, 0]))
                print('Start Station: ' + str(df['Start Station'].iloc[loop + i]))
                print('End Station: ' + str(df['End Station'].iloc[loop + i]))
                print('Start Time: ' + str(df['Start Time'].iloc[loop + i]))
                print('End Time: ' + str(df['End Time'].iloc[loop + i]))
                print('Trip Duration: ' + str(df['Trip Duration'].iloc[loop + i]))
                print('User Type: ' + str(df['User Type'].iloc[loop + i]))
                print('User Birth Year : ' + str(df['Birth Year'].iloc[loop + i]))
                print('User Gender: ' + str(df['Gender'].iloc[loop + i]))
                print('-'*40)
            except:
                print('End of File')
                break
        loop += 5

        while answer_correct == False:
            answer = str(input('Would you like to see individual trip raw data (yes or no)? ')).lower()
            if answer == 'yes' or answer == 'no':
                answer_correct = True
            else:
                print('You provided an incorrect input, please type either yes or no.')


def main():
    while True:
        city, month, day = get_filters()
       # city, month, day = 'Chicago', 'February', 'Tuesday'
        df = load_data(city, month, day)
        #print(df)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

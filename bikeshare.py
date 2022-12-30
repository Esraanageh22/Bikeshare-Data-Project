import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Enter the city choose chicago, new york city, or washington: ")
    city=city.lower()
    while city not in CITY_DATA.keys():
        print("Sorry, it is not a valid data choose from these cities: ")
        city=input("chigaco, new york city, or washington: ")
        city=city.lower()   
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month=input("Enter a month you want to see choose from jan to jun or all months: ")
        month=month.lower()
        if month in months:
            break
        else:
            print("sorry, it is not a valid month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day=input("Enter the day of week: ")
        day=day.lower()
        if day in days:
            break
        else:
            print("please enter a valid week day")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Day Of Week']=df['Start Time'].dt.day_name()
    df['Hour']=df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['Month']==month]

    if day != 'all':
        df = df[df['Day Of Week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['Month'].mode()[0]
    print('The most common month is :',popular_month)

    # TO DO: display the most common day of week
    popular_dayofweek=df['Day Of Week'].mode()[0]
    print('The most common day of week is :',popular_dayofweek)

    # TO DO: display the most common start hour
    popular_hour=df['Hour'].mode()[0]
    print('The most common start hour is :',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation=df['Start Station'].mode()[0]
    print('The most common start station is:',popular_startstation)

    # TO DO: display most commonly used end station
    popular_end=df['End Station'].mode()[0]
    print('The most common end station is:',popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Route']=df['Start Station']+' to '+df['End Station']
    popular_route=df['Route'].mode()[0]
    print('The most common route is:',popular_route)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum().round()
    print('Total drive time:',total_time)

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean().round()
    print('The mean travel time:',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts().to_frame()
    print('The counts of user types:',user_types)

    # TO DO: Display counts of gender
    if city!='washington':
        gender=df['Gender'].value_counts().to_frame()
        print('Counts of gender:',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        min_birth=int(df['Birth Year'].min())
        print('The earlist year of birth:',min_birth)
        max_birth=int(df['Birth Year'].max())
        print('The most recent year of birth:',max_birth)
        mode_birth=int(df['Birth Year'].mode()[0])
        print('The most common year of birth:',mode_birth)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('You can check the raw data')
    start_loc=0
    user_view=input('\n You want to see 5 rows of raw data?\n please enter yes or no').lower()
    user=['yes','no']
    
    if user_view in user:
        while user_view=='yes':
            print(df.iloc[start_loc+5])
            start_loc+=5
            user_view=input('\n Do you want to see another 5 rows?, please enter yes or no').lower()
        if user_view=='no':
            print('Thank you')
        
    if user_view not in user:
        print('please enter yes or no!')
        user_view=input('\n Do you want to see another 5 rows?, please enter yes or no').lower()
        while user_view=='yes':
            print(df.iloc[start_loc+5])
            start_loc+=5
            user_view=input('\n Do you want to see another 5 rows?, please enter yes or no').lower()
        if user_view=='no':
            print('Thank you')
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

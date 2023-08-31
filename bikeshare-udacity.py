# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:07:35 2020

@author: Mohamed Khalil 
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Enter The name of city to analyze Chicago  ,New York City ,Washington:\n').lower()
    while(not(city =='chicago' or city =='new york city' or city =='washington')):
        print('Invalid City Name, make sure the you chose from cities above!!')
        city=input('Enter The name of city to analyze(\'Chicago\'  \'New York City\'  \'Washington\'):\n').lower()
        if (city =='chicago' or city =='new york city' or city =='washington'):
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Enter The name of month to analyze January ,February ,March ,April , May ,June, All:\n').lower()
    while(not(month =='january' or month =='february' or month =='march' or month =='april' or month =='may' or month =='june' or month =='all')):
        print('Invalid Month Name, make sure the you chose from months above!!')
        month=input('Enter The name of month to analyze January ,February ,March ,April , May ,June ,All:\n').lower()
        if (month =='january' or month =='february' or month =='march' or month =='april' or month =='may' or month =='june'  or month =='all'):
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter The name of day to analyze Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All:\n').lower()
    while(not(day=='saturday' or day=='sunday' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='all')):
        print('Invalid Day Name, make sure the you chose from days above!!')
        day=input('Enter The name of day to analyze Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All:\n').lower()
        if (day=='saturday' or day=='sunday' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='all'):
            break

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
        df - pandas DataFrame containing city data filtered by month and day
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
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    print('Most Popular Month Is: ',(df['month'].mode()[0]))
    
    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    print('Most Common Day Is: ',(df['day_of_week'].mode()[0]))
    
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('Popular Hour Is: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Is: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Common End Is: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Common Start :{} \n To End Station: {}: '.format(df['Start Station'].mode()[0],df['End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time is: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travle Time Is: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print('The Total Number Of Subs And Users Is:\n',df['User Type'].value_counts())
    try:
        # TO DO: Display counts of gender
        print('\nThe Total Number Of Gender Types Is:\n',df['Gender'].value_counts())
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe Earliest Year Of Birth Is:\n',df['Birth Year'].min())
        print('\nThe Most Recent Year Of Birth Is:\n',df['Birth Year'].max())
        print('\nThe Most Common Year Of Birth Is:\n',df['Birth Year'].mode()[0])
    except:
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_rows(df):
    i=0
    head_5=input('Would you like to see first 5 raws in dataframe (y,n)\n')
    while head_5.lower() =='y':
        print(df[i:i+5])
        head_5=input('Would you like to see Next 5 raws in dataframe (y,n)\n')
        i+=5
        if i>200:
            break
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_rows(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

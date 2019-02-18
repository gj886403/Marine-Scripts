#!/usr/bin/python
# -*- coding: utf8 -*-

import ephem
import math


# ----------------------------------------------------------------------------------------------------------------------
def decimal_time(q, list, value):
    """
    a function to convert either a list of times, or a single time to decimal time.

    :param q: options. Choose between:
    q = 0 - a single datetime (returns date and time).
    q = 1 - a list of datetimes.
    q = 2 - a single time (ie not date and time, but just time).
    :param list: list of datetimes to be converted to decimal time. set this to 0 if a single datetime is being
    converted.
    :param value: a single datetime value.

    :return: a list of, or a single datetime converted into decimal time.
    """
    # for a list
    if q == 1:
        decimaltimes = []
        for item in list:
            decimaltime = ((((item.second / 60.) + item.minute) / 60.) + item.hour) / 24. + item.timetuple().tm_yday
            decimaltimes.append(decimaltime)
        return decimaltimes
    # for a single datetime
    if q == 0:
        decimaltime = ((((value.second / 60.) + value.minute) / 60.) + value.hour) / 24. + value.timetuple().tm_yday
        return decimaltime
    # for JUST the time (ie sunset/ sunrise TIME, and not date)
    if q == 2:
        decimaltime = ((((value.second / 60.) + value.minute) / 60.) + value.hour) / 24
        return decimaltime


# ----------------------------------------------------------------------------------------------------------------------
def calculate_time(date, lat, lon, whatdoyouwant, utc_time):
    """
    a function to calculate times of sunrise or sunset or noon for a given day and location.

    :param date: datetime object of the time to convert to decimal time.
    :param lat: latitude of the location for which the times are being calculated.
    :param lon: longitude of the location for which the times are being calculated.
    :param whatdoyouwant: tell the function what you want to caclulate. 3 options:
    0 = time of sunrise.
    1 = time of sunset.
    2 = time of noon.
    :param utc_time: how many hours to add on to convert to UTC time.

    :return forreturn: time in decimal time.
    """
    # strip the datetime object
    datestripped = date.strftime("%Y/%m/%d 00:00:00")

    # Use lat and lon to create ephem observer instance and update with given
    # values
    my_location = ephem.Observer()
    my_location.lat = str(lat)
    my_location.lon = str(lon)
    my_location.date = datestripped

    # Get sunrise of the current day
    sunrise = my_location.next_rising(ephem.Sun())
    sunset = my_location.next_setting(ephem.Sun())
    noon = my_location.next_transit(ephem.Sun())

    # choices of what you want to calculate
    if whatdoyouwant == 0:
        # sunrise
        forreturn = ephem.Date(sunrise + utc_time * ephem.hour).datetime()
    if whatdoyouwant == 1:
        # sunset
        forreturn = ephem.Date(sunset + utc_time * ephem.hour).datetime()
    if whatdoyouwant == 2:
        # 'transit' -- i.e noon, for us normal speaking people
        forreturn = ephem.Date(noon + utc_time * ephem.hour).datetime()

    return forreturn


# ----------------------------------------------------------------------------------------------------------------------
def split_times(lat,
                lon,
                inclusiveobvstimes,
                inclusiveobvsvalues,
                inclusiveukvvalues,
#                inclusivelonvalues):
                inclusivelonvalues,param_UTC=0):
    """
    A function to split data into different times (night, transition, morning, afternoon). This function is used after
    all the common times are found between ukv, London model and obs, and after all NaNs have been removed.

    :param lat: latitude of the location of the data
    :param lon: longitude of the location of the data
    :param inclusiveobvstimes: a list of times - this corresponds to inclusiveobvsvalues, inclusiveukvvalues,
    inclusivelonvalues (must all be the same length)
    :param inclusiveobvsvalues: a list of observations with no NaNs, and times matching with the UKV and London models.
    :param inclusiveukvvalues: a list of output from the UKV model with no NaNs, and times matching with the obs and
    London model.
    :param inclusivelonvalues: a list of output from the London model with no NaNs, and times matching with the obs and
    UKV model.

    :0return transtimes: list of times of the transition periods.
    :1return morningtimes: list of times of the morning periods.
    :2return afternoontimes: list of times of the afternoon periods.
    :3return nighttimes: list of times of the night periods.
    :4return transobvs: list of observations falling into the transition period times.
    :5return morningobvs: list of observations falling into the morning period times.
    :6return afternoonobvs: list of observations falling into the afternoon period times.
    :7return nightobvs: list of observations falling into the night period times.
    :8return transukv: list of UKV output falling into the transition period times.
    :9return morningukv: list of UKV output falling into the morning period times.
    :10return afternoonukv: list of UKV output falling into the afternoon period times.
    :11return nightukv: list of UKV output falling into the night period times.
    :12return translon: list of London model output falling into the transition period times.
    :13return morninglon: list of London model output falling into the morning period times.
    :14return afternoonlon: list of London model output falling into the afternoon period times.
    :15return nightlon: list of London model output falling into the night period times.
    """
    # SPLITTING TIMES
    # getting latitude and longitude from the observation file
    print ' '
    print '------------------'
    print 'Splitting the times up to day/night:'

    # empty lists to hold times of sunrise, sunset and noon.
    sunriselist = []
    sunsetlist = []
    noonlist = []

    # turns the time list inclusiveobvstimes into decimal time.
    # decimal time is used thought here, as calculations are made easier.
    inclusivedecimal = decimal_time(1, inclusiveobvstimes, 0)
    # uses the calculate_time function, and the ephem module to calculate times of sunrise, sunset and noon.
    for item in inclusiveobvstimes:
#        epsunrise = calculate_time(item, lat, lon, 0, 0)
#        epsunset = calculate_time(item, lat, lon, 1, 0)
#        epnoon = calculate_time(item, lat, lon, 2, 0)
        epsunrise = calculate_time(item, lat, lon, 0, param_UTC)
        epsunset = calculate_time(item, lat, lon, 1, param_UTC)
        epnoon = calculate_time(item, lat, lon, 2, param_UTC)
        # turns times into decimal time
        sunrise = decimal_time(2, 0, epsunrise)
        sunset = decimal_time(2, 0, epsunset)
        noon = decimal_time(2, 0, epnoon)
        # appends the decimal times to the lists defined above.
        sunriselist.append(sunrise)
        sunsetlist.append(sunset)
        noonlist.append(noon)

    # list, which will have numbers appended to it, based on what the corresponding
    # index in the time list is classed as.
    indilist = []

    for item, sunrise, sunset, noon in zip(inclusivedecimal, sunriselist, sunsetlist, noonlist):
        # here, math.floor(item) is used to find the DOY
        # 1-hour is (1/24.)
        # TRANSITION 1 (morning)-- 0
        # transition defined as an hour before and after sunrise/ sunset (including these times)
        if (sunrise - (1 / 24.) + int(math.floor(item))) <= item <= (sunrise + (1 / 24.) + int(math.floor(item))):
            indilist.append(0)
        # MORNING -- 1
        # morning defined as times after transition to noon (including noon).
        elif (sunrise + (1 / 24.) + int(math.floor(item))) < item <= (noon + int(math.floor(item))):
            indilist.append(1)
        # AFTERNOON -- 2
        # afternoon defined as times from noon to the start of transition
        elif (noon + int(math.floor(item))) < item < (sunset - (1 / 24.) + int(math.floor(item))):
            indilist.append(2)
        # TRANSITION 2 (evening)-- 3
        # transition 2 defined as an hour before and after sunset (including these times)
        # CURRENTLY BOTH TRANSITION ONE AND TWO ARE TOGETHER IN TRANSITION 1
        elif (sunset - (1 / 24.) + int(math.floor(item))) <= item <= (sunset + (1 / 24.) + int(math.floor(item))):
            indilist.append(0)
        # NIGHT -- 4
        # night defined as all other times.
        else:
            indilist.append(4)

    # indilist and the original datetime observation list are the same length, continue. else, error.
    if len(inclusiveobvstimes) == len(indilist):
        # create empty list for each time
        transtimes = []
        morningtimes = []
        afternoontimes = []
        nighttimes = []
        transobvs = []
        morningobvs = []
        afternoonobvs = []
        nightobvs = []
        transukv = []
        morningukv = []
        afternoonukv = []
        nightukv = []
        translon = []
        morninglon = []
        afternoonlon = []
        nightlon = []

        # append times, obs and model values based on the value in indilist and list index.
        for time, obv, ukv, lon, indi in zip(inclusiveobvstimes, inclusiveobvsvalues, inclusiveukvvalues,
                                             inclusivelonvalues, indilist):
            if indi == 0:
                transtimes.append(time)
                transobvs.append(obv)
                transukv.append(ukv)
                translon.append(lon)
            if indi == 1:
                morningtimes.append(time)
                morningobvs.append(obv)
                morningukv.append(ukv)
                morninglon.append(lon)
            if indi == 2:
                afternoontimes.append(time)
                afternoonobvs.append(obv)
                afternoonukv.append(ukv)
                afternoonlon.append(lon)
            if indi == 3:
                transtimes.append(time)
                transobvs.append(obv)
                transukv.append(ukv)
                translon.append(lon)
            if indi == 4:
                nighttimes.append(time)
                nightobvs.append(obv)
                nightukv.append(ukv)
                nightlon.append(lon)

        # checking if all the things are the same length once they've been split into night and day
        if len(indilist) == len(transtimes) + len(morningtimes) + len(afternoontimes) + len(
                nighttimes) == len(transobvs) + len(morningobvs) + len(afternoonobvs) + len(
            nightobvs) == len(transukv) + len(morningukv) + len(afternoonukv) + len(nightukv) == len(
            translon) + len(morninglon) + len(afternoonlon) + len(nightlon):
            print 'List length is correct'

            return (transtimes,
                    morningtimes,
                    afternoontimes,
                    nighttimes,
                    transobvs,
                    morningobvs,
                    afternoonobvs,
                    nightobvs,
                    transukv,
                    morningukv,
                    afternoonukv,
                    nightukv,
                    translon,
                    morninglon,
                    afternoonlon,
                    nightlon)

        else:
            print '!!! List length is incorrect !!!'

    else:
        print '!!! List length is incorrect !!!'

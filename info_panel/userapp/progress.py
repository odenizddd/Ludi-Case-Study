import json
from datetime import datetime, timedelta

def timestamp_to_datetime(timestamp):
    start_datetime_str = "01-01-1900 00:00:00"
    start_datetime = datetime.strptime(start_datetime_str, '%d-%m-%Y %H:%M:%S')

    day_delta = int(timestamp)
    second_delta = (timestamp - day_delta) * 24 * 60 * 60

    return start_datetime + timedelta(days=day_delta, seconds=second_delta)

def get_cumulative_user_count_per_date():
    with open('users.json') as file:
        users = json.load(file)["users"]

    user_count_per_date = {}

    for user in users:
        date = timestamp_to_datetime(user["signup_datetime"]).date()
        if date in user_count_per_date:
            user_count_per_date[date] += 1
        else:
            user_count_per_date[date] = 1


    user_count_per_date = sorted(user_count_per_date.items(), key=lambda x: x[0])

    cumulative_user_count_per_date = {}

    for i, date in enumerate(user_count_per_date):
        if i == 0:
            cumulative_user_count_per_date[date[0]] = date[1]
        else:
            cumulative_user_count_per_date[date[0]] = cumulative_user_count_per_date[user_count_per_date[i-1][0]] + date[1]

    return [{"date": str(date), "count": count} for date, count in cumulative_user_count_per_date.items()]

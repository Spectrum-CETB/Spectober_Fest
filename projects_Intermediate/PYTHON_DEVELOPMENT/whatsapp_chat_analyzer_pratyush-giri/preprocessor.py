import pandas as pd
import re

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({"user_message": messages, "Date": dates})
    df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%y, %H:%M - ')
    users = []
    messages = []
    for message in df["user_message"]:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append("group_notification")
            messages.append(entry[0])

    df["Users"] = users
    df["Message"] = messages
    df.drop(columns=["user_message"], inplace=True)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    df["Day"] = df['Date'].dt.day
    df['Hour'] = df['Date'].dt.hour
    df['Minute'] = df['Date'].dt.minute
    df.drop(columns=["Date"], inplace=True)

    return df
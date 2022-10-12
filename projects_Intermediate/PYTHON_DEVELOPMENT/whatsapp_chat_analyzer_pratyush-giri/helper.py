from urlextract import URLExtract

extractor = URLExtract()
def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df['Users'] == selected_user]
    # fetch the number of messages
    num_messages=  df.shape[0]
    # fetch the total number of words
    words = []
    for message in df["Message"]:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['Message']=='<Media omitted>\n'].shape[0]

    # fetch the no of links shared
    links= []
    for message in df["Message"]:
        links.extend(extractor.find_urls(message))



    return num_messages, len(words),num_media_messages,len(links)

def most_busy_users(df):
    x=df["Users"].value_counts().head()
    df = round((df['Users'].value_counts()/df.shape[0])*100,2).reset_index().rename(
        columns = {"index":"name","Users":"percent"}
    )
    return x,df
import streamlit as st
import preprocessor,helper
st.sidebar.title("Whatsapp Chat Analyzer")
import matplotlib.pyplot as plt

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #fetch unique users
    user_list = df['Users'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    # starting the analysis
    if st.sidebar.button("Show analysis"):

        num_messages,words,num_media_messages,links =  helper.fetch_stats(selected_user,df)

        col1,col2,col3,col4 = st.beta_columns(4)

        with col1:
            st.header("total Messages")
            st.title(num_messages)

        with col2:
            st.header("total Words")
            st.title(words)

        with col3:
            st.header(" Media shared")
            st.title(num_media_messages)
        with col4:
            st.header(" links shared")
            st.title(links)

        # finding the busiest user in the group
        if selected_user =="Overall":
            st.title('Most busy users')
            x,new_df = helper.most_busy_users(df)
            fig ,ax = plt.subplots()

            col1,col2 = st.beta_columns(2)

            with col1:
                ax.bar(x.index, x.values)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
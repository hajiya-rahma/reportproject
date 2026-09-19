#Libraries importation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Course Registration Analysis")
df=pd.read_csv("courses.csv")
st.dataframe(df)

st.subheader("FIRST THREE RECORDS")
st.dataframe(df.head(3))

st.subheader("LAST THREE RECORDS")
st.dataframe(df.tail(3))

st.subheader("STATISTICAL SUMMARY")
st.dataframe(df.describe())

st.subheader("DATA SUMMARY")
st.dataframe(df.info())


if st.button("SHOW ATTENDANCE DETAILS > 50"):
    highest_attendance=df[df["Attendance"]>50]
    st.dataframe(highest_attendance)

if st.button("SHOW ATTENDANCE DETAILS < 50"):
    lowest_attendance=df[df["Attendance"]<50]
    st.dataframe(lowest_attendance)

age_filter=st.slider(0,50,100)
attendance=df[df["Attendance"]>= age_filter]
st.dataframe(attendance)

#age_filter=st.slider(0,25,50,100)
#attendance=df[df["Attendance"]>= age_filter]
#st.write(attendance)

st.subheader("LINE CHART")
st.line_chart(df[["CourseTitle", "Attendance"]])

st.subheader("BAR CHART")
st.bar_chart(df[["CourseTitle", "Attendance"]])

st.subheader("SCATTER CHART")
st.scatter_chart(df[["CourseID", "Attendance"]])
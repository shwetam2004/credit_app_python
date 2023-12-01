# import reqd libraries
import streamlit as st
import pandas as pd
import plotly.express as px

uploaded_file = st.file_uploader("Upload a file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Streamlit app
    st.title(":bar_chart: Exploratory Data Analysis - Credit dataset :credit_card:")

    # Displaying the dataframe
    st.subheader("Dataset")
    st.write(df)

    # Scatter Plot
    st.subheader("Scatter Plot - Credit Amount vs Age")
    scatter_fig = px.scatter(df, x="age", y="Camt", title="Credit Amount vs Age")
    st.plotly_chart(scatter_fig)

    # Bar chart
    st.subheader("Bar Chart - Credit Purpose Count")
    bar_fig = px.bar(df['Cpur'].value_counts().reset_index(), x="index", y="Cpur",
                    labels = {'index':'Credit Purpose', 'Cpur':'Count'},
                    title = "Credit Purpose Count")
    st.plotly_chart(bar_fig)

    # Pie chart
    st.subheader("Pie Chart - Credit Score Distribution")
    pie_fig = px.pie(df['creditScore'].value_counts().reset_index(), names='index', values='creditScore',
                    title='Credit Score Distribution')
    st.plotly_chart(pie_fig)

    # Histogram
    st.subheader('Histogram - Credit Duration Distribution')
    hist_fig = px.histogram(df, x='Cdur', title='Creidt Duration Distribution')
    st.plotly_chart(hist_fig)

    # Box Plot
    st.subheader('Box Plot - Credit Amount by Property')
    box_fig = px.box(df, x='Prop', y='Camt', title='Credit Amount by Property')
    st.plotly_chart(box_fig)
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the app
st.title('Class Participation Heatmap')

# File uploader to upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("### Data Preview:")
    st.write(df.head())
    
    # Ensure the dataset contains the required columns
    if 'Student' not in df.columns or 'Date' not in df.columns or 'Participation' not in df.columns:
        st.error("The dataset must contain 'Student', 'Date', and 'Participation' columns.")
    else:
        # Convert Date column to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Pivot the data for the heatmap
        pivot_df = df.pivot_table(index='Student', columns='Date', values='Participation', aggfunc='sum', fill_value=0)
        
        # Plot the heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_df, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Participation'}, linewidths=0.5)
        
        # Display the heatmap
        st.write("### Class Participation Heatmap:")
        st.pyplot(plt)
        
        # Additional details or statistics
        st.write("### Participation Summary:")
        total_participation = df.groupby('Student')['Participation'].sum()
        st.write(total_participation)

        # Option to download the participation summary
        st.download_button(
            label="Download Participation Summary",
            data=total_participation.to_csv().encode(),
            file_name="participation_summary.csv",
            mime="text/csv"
        )


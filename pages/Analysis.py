import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set page configuration
st.set_page_config(page_title='Loan Prediction Analysis', layout='wide')

# Title for the Streamlit app

# Load the dataset
df = pd.read_csv('loan_approval_dataset.csv')


# Clean column names by stripping whitespace (recommended)
df.columns = df.columns.str.strip()

# Sidebar selection
option = st.sidebar.selectbox("Select Analysis Option", ['no_of_dependents', 'education', 'self_employed','income_annum',
'loan_amount','loan_term','cibil_score','residential_assets_value','luxury_assets_value','bank_assets_value'])


# Function to filter by number of dependents
def load_no_of_dependents(selected_dependents):

    st.header("👨‍👩‍👧‍👦 Dependents & Loan Analysis")


    if selected_dependents == 'Overall_Analysis':
        # Distribution of no_of_dependents
        st.subheader("🔢 Distribution of Number of Dependents")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=df, x='no_of_dependents', ax=ax1, palette='pastel')
        ax1.set_title("Distribution of No. of Dependents")
        ax1.set_xlabel("Number of Dependents")
        ax1.set_ylabel("Frequency")
        st.pyplot(fig1)

        # Boxplot of loan amount by number of dependents
        st.subheader("💰 Loan Amount Distribution by Dependents (Box Plot)")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x='no_of_dependents', y='loan_amount', ax=ax2, palette='Set2')
        ax2.set_title("Loan Amount Distribution by Number of Dependents")
        ax2.set_xlabel("Number of Dependents")
        ax2.set_ylabel("Loan Amount")
        st.pyplot(fig2)
    
    else:

       # Filter data
       filtered_df = df[df['no_of_dependents'] == selected_dependents]

       # Count Approved/Rejected loans
       loan_counts = filtered_df['loan_status'].value_counts()
    
       st.subheader(f"Loan Status Counts for {selected_dependents} Dependents")
       st.write(loan_counts)
    
       # Bar chart
       st.subheader("Bar Chart")
       fig, ax = plt.subplots()
       loan_counts.plot(kind='bar', ax=ax, color=['green', 'red'])
       ax.set_ylabel("Count")
       ax.set_xlabel("Loan Status")
       ax.set_title(f"Loan Status for {selected_dependents} Dependents")
       st.pyplot(fig)



# Function to filter by education
def load_education(selected_education):

    st.header("🎓 Education Level & Loan Status Analysis")

    filtered_df = df[df['education'] == selected_education]

    # Count Approved/Rejected loans
    loan_counts = filtered_df['loan_status'].value_counts()
    
    st.subheader(f"Loan Status Counts for {selected_education} education")
    st.write(loan_counts)
    
    # Bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    loan_counts.plot(kind='bar', ax=ax, color=['green', 'red'])
    ax.set_ylabel("Count")
    ax.set_xlabel("Loan Status")
    ax.set_title(f"Loan Status for {selected_education} education")
    st.pyplot(fig)
    

# Function to filter by self_employed
def load_self_employed(selected_self_employed):

    st.header("👨‍💼 Self Employment & Loan Status Analysis")

    filtered_df = df[df['self_employed'] == selected_self_employed]

    # Count Approved/Rejected loans
    loan_counts = filtered_df['loan_status'].value_counts()
    
    st.subheader(f"Loan Status Counts for {selected_self_employed} Employed")
    st.write(loan_counts)
    
    # Bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    loan_counts.plot(kind='bar', ax=ax, color=['green', 'red'])
    ax.set_ylabel("Count")
    ax.set_xlabel("Loan Status")
    ax.set_title(f"Loan Status for {selected_self_employed} Employed")
    st.pyplot(fig)
    

def load_income_annum(selected_loan_status):

    st.header("💰 Income & Loan Status Analysis")

    

    # Define income bins and labels
    income_bins = [0, 100000, 300000, 500000, 800000, 1000000,
                   2000000, 3000000, 4000000, 5000000, df['income_annum'].max()]
    income_labels = ['<1L', '1-3L', '3-5L', '5-8L', '8-10L',
                     '10-20L', '20-30L', '30-40L', '40-50L', '50L+']

    # Add income range to full dataset
    df['income_range'] = pd.cut(df['income_annum'], bins=income_bins, labels=income_labels)

    # Filter by selected loan status (0 = rejected, 1 = approved)
    filtered_df = df[df['loan_status'] == selected_loan_status]

    # Count loans in each income range
    loan_counts_by_income = filtered_df['income_range'].value_counts().sort_index()

    # Display table
    st.subheader(f"Loan Count by Income Range (Loan Status: {selected_loan_status})")
    st.dataframe(loan_counts_by_income.reset_index().rename(columns={
        'index': 'Income Range', 'income_range': 'Number of Loans'
    }))

    # Plot bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    loan_counts_by_income.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel("Income Range")
    ax.set_ylabel("Number of Loans")
    ax.set_title(f"Loan Count by Annual Income (Status: {selected_loan_status})")
    st.pyplot(fig)
    

def load_loan_amount():

    st.header("📊 Overall loan_amount Analysis")

    st.write("#### Summary Statistics")
    st.write(df['loan_amount'].describe())

    st.write("#### Distribution of loan_amount")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['loan_amount'], bins=30, kde=True, color='purple', ax=ax1)
    ax1.set_title("Overall loan_amount Distribution")
    ax1.set_xlabel("loan_amount")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    st.write("#### loan_amount by Income Bracket")
    income_brackets = pd.cut(df['income_annum'], bins=[0, 500000, 1000000, 2000000, 3000000, 5000000 , 10000000], labels=["0-5L", "5k-10L", "10k-20L", "20k-30L", "30-50L" ,"50L+"])
    df['income_bracket'] = income_brackets

    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='income_bracket', y='loan_amount', data=df, ax=ax9)
    ax9.set_title('loan_amount by Income Bracket')
    ax9.set_xlabel('Income Bracket')
    ax9.set_ylabel('loan_amount')
    st.pyplot(fig9)

    st.write("#### loan_amount by Loan Term")
    fig10, ax10 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='loan_term', y='loan_amount', data=df, ax=ax10)
    ax10.set_title('loan_amount by Loan Term')
    ax10.set_xlabel('Loan Term')
    ax10.set_ylabel('loan_amount')
    st.pyplot(fig10)

    st.write("#### Pairplot of Key Variables")
    fig13 = sns.pairplot(df[['cibil_score','residential_assets_value', 'loan_amount', 'income_annum']])
    st.pyplot(fig13)

    # Categorical Features Anlaysis

    st.header("📚 Categorical Feature vs loan_amount Analysis")

    categorical_features = ['education', 'self_employed', 'loan_status']
    
    selected_feature = st.selectbox("Select a categorical feature:", categorical_features)

    #  Show which feature was selected
    st.write(f"You selected: **{selected_feature}**")

    # Drop NA values if present
    temp_df = df[[selected_feature, 'loan_amount']].dropna()

    # Boxplot
    st.write(f"#### Boxplot: cibil_score by {selected_feature}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=selected_feature, y='loan_amount', data=temp_df, ax=ax1)
    ax1.set_title(f'loan_amount by {selected_feature}')
    ax1.set_xlabel(selected_feature)
    ax1.set_ylabel('loan_amount')
    st.pyplot(fig1)

    # Barplot of average values
    st.write(f"#### Average loan_amount by {selected_feature}")
    avg_df = temp_df.groupby(selected_feature)['loan_amount'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=selected_feature, y='loan_amount', data=avg_df, palette='viridis', ax=ax2)
    ax2.set_title(f'Average loan_amount by {selected_feature}')
    ax2.set_xlabel(selected_feature)
    ax2.set_ylabel('Average loan_amount')
    st.pyplot(fig2)

    # DataFrame
    st.write("#### Summary Table")
    st.dataframe(avg_df)



def load_loan_term():

    st.header("📅 Loan Term Analysis")

    # Display Loan Term Summary
    st.subheader('Loan Term Summary:')
    loan_term_summary = df['loan_term'].describe()

    # Display the summary in Streamlit
    st.write(loan_term_summary)

    st.subheader("Loan Term Distribution")

    # Plot simple distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['loan_term'], bins=10, color='skyblue', ax=ax)
    ax.set_title("Loan Term Distribution (All Loans)")
    ax.set_xlabel("Loan Term")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Average loan term by loan status
    st.subheader("Average Loan Term by Loan Status")
    avg_loan_term = df.groupby('loan_status')['loan_term'].mean().reset_index()
    

    st.dataframe(avg_loan_term)

    # Plotting average loan term
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=avg_loan_term, x='loan_status', y='loan_term', palette='Set2', ax=ax2)
    ax2.set_title("Average Loan Term by Loan Status")
    ax2.set_xlabel("Loan Status")
    ax2.set_ylabel("Average Loan Term")
    st.pyplot(fig2)

    # 3. Loan Term Count by Loan Status (Comparison between Approved and Rejected)
    st.subheader("Loan Term Count by Loan Status")
    loan_term_count = df.groupby(['loan_status', 'loan_term']).size().unstack(fill_value=0).T
    st.dataframe(loan_term_count)

    # Plot loan term count by loan status
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    loan_term_count.plot(kind='bar', stacked=True, ax=ax3, color=['green', 'red'])
    ax3.set_title("Loan Term Count by Loan Status (Approved vs Rejected)")
    ax3.set_xlabel("Loan Term")
    ax3.set_ylabel("Number of Loans")
    st.pyplot(fig3)

def load_cibil_score():

    st.header("📊 Overall cibil_score Analysis")

    st.write("#### Summary Statistics")
    st.write(df['cibil_score'].describe())

    st.write("#### Distribution of cibil_score")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['cibil_score'], bins=30, kde=True, color='purple', ax=ax1)
    ax1.set_title("Overall cibil_score Distribution")
    ax1.set_xlabel("cibil_score")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)


    st.write("#### cibil_score by Income Bracket")
    income_brackets = pd.cut(df['income_annum'], bins=[0, 500000, 1000000, 2000000, 3000000, 5000000 , 10000000], labels=["0-5L", "5k-10L", "10k-20L", "20k-30L", "30-50L" ,"50L+"])
    df['income_bracket'] = income_brackets

    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='income_bracket', y='cibil_score', data=df, ax=ax9)
    ax9.set_title('cibil_score by Income Bracket')
    ax9.set_xlabel('Income Bracket')
    ax9.set_ylabel('cibil_score')
    st.pyplot(fig9)

    st.write("#### cibil_score by Loan Term")
    fig10, ax10 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='loan_term', y='cibil_score', data=df, ax=ax10)
    ax10.set_title('cibil_score by Loan Term')
    ax10.set_xlabel('Loan Term')
    ax10.set_ylabel('cibil_score')
    st.pyplot(fig10)

    st.write("#### Pairplot of Key Variables")
    fig13 = sns.pairplot(df[['cibil_score','residential_assets_value', 'loan_amount', 'income_annum']])
    st.pyplot(fig13)

    # Categorical Features Anlaysis

    st.header("📚 Categorical Feature vs cibil_score Analysis")

    categorical_features = ['education', 'self_employed', 'loan_status']
    
    selected_feature = st.selectbox("Select a categorical feature:", categorical_features)

    #  Show which feature was selected
    st.write(f"You selected: **{selected_feature}**")

    # Drop NA values if present
    temp_df = df[[selected_feature, 'cibil_score']].dropna()

    # Boxplot
    st.write(f"#### Boxplot: cibil_score by {selected_feature}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=selected_feature, y='cibil_score', data=temp_df, ax=ax1)
    ax1.set_title(f'cibil_score by {selected_feature}')
    ax1.set_xlabel(selected_feature)
    ax1.set_ylabel('cibil_score')
    st.pyplot(fig1)

    # Barplot of average values
    st.write(f"#### Average cibil_score by {selected_feature}")
    avg_df = temp_df.groupby(selected_feature)['cibil_score'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=selected_feature, y='cibil_score', data=avg_df, palette='viridis', ax=ax2)
    ax2.set_title(f'Average cibil_score by {selected_feature}')
    ax2.set_xlabel(selected_feature)
    ax2.set_ylabel('Average cibil_score')
    st.pyplot(fig2)

    # DataFrame
    st.write("#### Summary Table")
    st.dataframe(avg_df)


def residential_assets_value():

    st.header("📊 Overall residential_assets_value Analysis")

    st.write("#### Summary Statistics")
    st.write(df['residential_assets_value'].describe())

    st.write("#### Distribution of residential_assets_value")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['residential_assets_value'], bins=30, kde=True, color='purple', ax=ax1)
    ax1.set_title("Overall residential_assets_value Distribution")
    ax1.set_xlabel("residential_assets_value")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    st.write("#### residential_assets_value by Income Bracket")
    income_brackets = pd.cut(df['income_annum'], bins=[0, 500000, 1000000, 2000000, 3000000, 5000000 , 10000000], labels=["0-5L", "5k-10L", "10k-20L", "20k-30L", "30-50L" ,"50L+"])
    df['income_bracket'] = income_brackets

    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='income_bracket', y='residential_assets_value', data=df, ax=ax9)
    ax9.set_title('residential_assets_value by Income Bracket')
    ax9.set_xlabel('Income Bracket')
    ax9.set_ylabel('residential_assets_value')
    st.pyplot(fig9)

    st.write("#### residential_assets_value by Loan Term")
    fig10, ax10 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='loan_term', y='residential_assets_value', data=df, ax=ax10)
    ax10.set_title('residential_assets_value by Loan Term')
    ax10.set_xlabel('Loan Term')
    ax10.set_ylabel('residential_assets_value')
    st.pyplot(fig10)

    st.write("#### Pairplot of Key Variables")
    fig13 = sns.pairplot(df[['residential_assets_value', 'loan_amount', 'income_annum']])
    st.pyplot(fig13)

    # Categorical Features Anlaysis

    st.header("📚 Categorical Feature vs residential_assets_value Analysis")

    categorical_features = ['education', 'self_employed', 'loan_status']
    
    selected_feature = st.selectbox("Select a categorical feature:", categorical_features)

    #  Show which feature was selected
    st.write(f"You selected: **{selected_feature}**")

    # Drop NA values if present
    temp_df = df[[selected_feature, 'residential_assets_value']].dropna()

    # Boxplot
    st.write(f"#### Boxplot: residential_assets_value by {selected_feature}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=selected_feature, y='residential_assets_value', data=temp_df, ax=ax1)
    ax1.set_title(f'residential_assets_value by {selected_feature}')
    ax1.set_xlabel(selected_feature)
    ax1.set_ylabel('residential_assets_value')
    st.pyplot(fig1)

    # Barplot of average values
    st.write(f"#### Average residential_assets_value by {selected_feature}")
    avg_df = temp_df.groupby(selected_feature)['residential_assets_value'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=selected_feature, y='residential_assets_value', data=avg_df, palette='viridis', ax=ax2)
    ax2.set_title(f'Average residential_assets_value by {selected_feature}')
    ax2.set_xlabel(selected_feature)
    ax2.set_ylabel('Average residential_assets_value')
    st.pyplot(fig2)

    # DataFrame
    st.write("#### Summary Table")
    st.dataframe(avg_df)


def luxury_assets_value():

    st.header("📊 Overall luxury_assets_value Analysis")

    st.write("#### Summary Statistics")
    st.write(df['luxury_assets_value'].describe())

    st.write("#### Distribution of luxury_assets_value")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['luxury_assets_value'], bins=30, kde=True, color='purple', ax=ax1)
    ax1.set_title("Overall luxury_assets_value Distribution")
    ax1.set_xlabel("luxury_assets_value")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)


    st.write("#### luxury_assets_value by Income Bracket")
    income_brackets = pd.cut(df['income_annum'], bins=[0, 500000, 1000000, 2000000, 3000000, 5000000 , 10000000], labels=["0-5L", "5k-10L", "10k-20L", "20k-30L", "30-50L" ,"50L+"])
    df['income_bracket'] = income_brackets

    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='income_bracket', y='luxury_assets_value', data=df, ax=ax9)
    ax9.set_title('luxury_assets_value by Income Bracket')
    ax9.set_xlabel('Income Bracket')
    ax9.set_ylabel('luxury_assets_value')
    st.pyplot(fig9)

    st.write("#### luxury_assets_value by Loan Term")
    fig10, ax10 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='loan_term', y='luxury_assets_value', data=df, ax=ax10)
    ax10.set_title('luxury_assets_value by Loan Term')
    ax10.set_xlabel('Loan Term')
    ax10.set_ylabel('luxury_assets_value')
    st.pyplot(fig10)

    st.write("#### Pairplot of Key Variables")
    fig13 = sns.pairplot(df[['luxury_assets_value', 'loan_amount', 'income_annum']])
    st.pyplot(fig13)

    # Categorical Features Anlaysis

    st.header("📚 Categorical Feature vs luxury_assets_value Analysis")

    categorical_features = ['education', 'self_employed', 'loan_status']
    
    selected_feature = st.selectbox("Select a categorical feature:", categorical_features)

    # Show which feature was selected
    st.write(f"You selected: **{selected_feature}**")

    # Drop NA values if present
    temp_df = df[[selected_feature, 'luxury_assets_value']].dropna()

    # Boxplot
    st.write(f"#### Boxplot: luxury_assets_value by {selected_feature}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=selected_feature, y='luxury_assets_value', data=temp_df, ax=ax1)
    ax1.set_title(f'luxury_assets_value by {selected_feature}')
    ax1.set_xlabel(selected_feature)
    ax1.set_ylabel('luxury_assets_value')
    st.pyplot(fig1)

    # Barplot of average values
    st.write(f"#### Average luxury_assets_value by {selected_feature}")
    avg_df = temp_df.groupby(selected_feature)['luxury_assets_value'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=selected_feature, y='luxury_assets_value', data=avg_df, palette='viridis', ax=ax2)
    ax2.set_title(f'Average luxury_assets_value by {selected_feature}')
    ax2.set_xlabel(selected_feature)
    ax2.set_ylabel('Average luxury_assets_value')
    st.pyplot(fig2)

    # DataFrame
    st.write("#### Summary Table")
    st.dataframe(avg_df)
    

def bank_assets_value():


    st.header("📊 Overall bank_asset_value Analysis")

    st.write("#### Summary Statistics")
    st.write(df['bank_asset_value'].describe())

    st.write("#### Distribution of bank_asset_value")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['bank_asset_value'], bins=30, kde=True, color='purple', ax=ax1)
    ax1.set_title("Overall bank_asset_value Distribution")
    ax1.set_xlabel("bank_asset_value")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    st.write("#### Bank Asset Value by Income Bracket")
    income_brackets = pd.cut(df['income_annum'], bins=[0, 500000, 1000000, 2000000, 3000000, 5000000 , 10000000], labels=["0-5L", "5k-10L", "10k-20L", "20k-30L", "30-50L" ,"50L+"])
    df['income_bracket'] = income_brackets

    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='income_bracket', y='bank_asset_value', data=df, ax=ax9)
    ax9.set_title('Bank Asset Value by Income Bracket')
    ax9.set_xlabel('Income Bracket')
    ax9.set_ylabel('Bank Asset Value')
    st.pyplot(fig9)

    st.write("#### Bank Asset Value by Loan Term")
    fig10, ax10 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='loan_term', y='bank_asset_value', data=df, ax=ax10)
    ax10.set_title('Bank Asset Value by Loan Term')
    ax10.set_xlabel('Loan Term')
    ax10.set_ylabel('Bank Asset Value')
    st.pyplot(fig10)

    st.write("#### Pairplot of Key Variables")
    fig13 = sns.pairplot(df[['bank_asset_value', 'loan_amount', 'income_annum']])
    st.pyplot(fig13)

    # Categorical Features Anlaysis

    st.header("📚 Categorical Feature vs Bank Asset Value Analysis")

    categorical_features = ['education', 'self_employed', 'loan_status']
    
    selected_feature = st.selectbox("Select a categorical feature:", categorical_features)

    #Show which feature was selected
    st.write(f"You selected: **{selected_feature}**")

    # Drop NA values if present
    temp_df = df[[selected_feature, 'bank_asset_value']].dropna()

    # Boxplot
    st.write(f"#### Boxplot: Bank Asset Value by {selected_feature}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=selected_feature, y='bank_asset_value', data=temp_df, ax=ax1)
    ax1.set_title(f'Bank Asset Value by {selected_feature}')
    ax1.set_xlabel(selected_feature)
    ax1.set_ylabel('Bank Asset Value')
    st.pyplot(fig1)

    # Barplot of average values
    st.write(f"#### Average Bank Asset Value by {selected_feature}")
    avg_df = temp_df.groupby(selected_feature)['bank_asset_value'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=selected_feature, y='bank_asset_value', data=avg_df, palette='viridis', ax=ax2)
    ax2.set_title(f'Average Bank Asset Value by {selected_feature}')
    ax2.set_xlabel(selected_feature)
    ax2.set_ylabel('Average Bank Asset Value')
    st.pyplot(fig2)

    # DataFrame
    st.write("#### Summary Table")
    st.dataframe(avg_df)
    
    

# Run logic if "no_of_dependents" is selected
if option == 'no_of_dependents':
    dependents_list = [0, 1, 2, 3, 4, 5 , 'Overall_Analysis']
    selected_dependents = st.sidebar.selectbox('Select Number of Dependents', dependents_list)
    
    if st.sidebar.button('Find no_of_dependents Details'):
        load_no_of_dependents(selected_dependents)

elif option == 'education':
    education_list = df['education'].dropna().unique().tolist()
    selected_education = st.sidebar.selectbox('Select Education', education_list)
    if st.sidebar.button('Find Education Details'):
        load_education(selected_education)

elif option == 'self_employed':
    self_employed_list = df['self_employed'].dropna().unique().tolist()
    selected_self_employed = st.sidebar.selectbox('Select Self Employment Status', self_employed_list)
    if st.sidebar.button('Find Self Employed Details'):
        load_self_employed(selected_self_employed)
    


elif option == 'income_annum':
    loan_statuses = df['loan_status'].dropna().unique().tolist()
    selected_loan_status = st.sidebar.selectbox('Select Loan Status', loan_statuses)

    if st.sidebar.button('Find incom_annum Details'):
        load_income_annum(selected_loan_status)

elif option == 'loan_amount':
    if st.sidebar.button('Find loan_amount Details'):
        load_loan_amount()


elif option == 'loan_term':
    # Button to trigger loan term analysis without status filtering
    if st.sidebar.button('Analyze Loan Term '):
        load_loan_term()

elif option == 'cibil_score':
    if st.sidebar.button('Analyze cibil_score'):
        load_cibil_score()

elif option == 'residential_assets_value':
    if st.sidebar.button('Analyze residential_assets_value'):
        residential_assets_value()


elif option == 'luxury_assets_value':
    if st.sidebar.button('Analyze luxury_assets_value'):
        luxury_assets_value()

elif option == 'bank_assets_value':
    if st.sidebar.button('Analyze bank_assets_value'):
        bank_assets_value()

#elif option == 'bank_assets_value':
    #bank_assets_value()
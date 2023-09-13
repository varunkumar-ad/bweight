import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np
df=pd.read_csv('BirthWt.csv')
def home():
    st.title("Welcome to Birth Weight data presentation")
    image = Image.open('image.png')
    st.image(image, caption='Birth Weight')
def Data_Header():
    st.write(df.head())
def Pinfo():
    tab1 = st.tabs(['Birth weight'])
    st.title('Birth weight of the newborn')
    bweight_selection = st.slider('Birth weight:',
                                 min_value=min(df['bweight']),
                                 max_value=max(df['bweight']),
                                 value=(min(df['bweight']), max(df['bweight'])))
    mask = (df['bweight'].between(*bweight_selection))

    sex_level = st.multiselect("Select the sex:",
                               options=df["sex"].unique(),
                               default=df["sex"].unique(), key="k2")
    df_selection = df.query(
        "sex == @sex_level"
    )
    fig1 = px.histogram(df_selection[mask], x="bweight", title="Histogram based on Birth weight and sex",
                      labels={'bweight': 'Birth weight'}, color='sex')
    st.plotly_chart(fig1)

    mask = (df['bweight'].between(*bweight_selection)) & (df['sex'].isin(df_selection))

    t1 = df_selection.groupby(['sex'])['bweight'].aggregate(['count','sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t1)
    st.write("1. Majority of the newborn's birth weight lies between 2500 and 3700, but birth weight more than 4600 could be found in less proportion.")
    st.write("2. Almost constant number of newborns from the birth weight spread between 0 to 2100")
    st.write("3. From the table, first half of the male newborns are below the birth weight of 3290 ")
    st.write("4. From the table, first half of the female newborns are below the birth weight of 3120 ")

def Minfo():
    options = st.selectbox('select the variable', ["Hypertension","Maternal age group","Gestational age categories"])
    if options=='Hypertension':
        ht()
    elif options =='Maternal age group':
        matagegp()
    elif options =='Gestational age categories':
        gestcat()
st.sidebar.title("Direction")
side=st.sidebar.radio('Select what you want to see:', ['Home', 'Data Header', "Baby's Info","Mother's Info", 'Report'])

def report():
    st.title('Conclusion')
    st.write('1. Birth weight of newborns are more consistent when the mother has no hypertension.')
    st.write('2. Maternal age group slightly affect the birth weight.')
    st.write('3. When the gestational age category >=37 weeks, newborns birth weight is more consistent.')
    st.write('4. Birth weight decrease when the mother is a hypertension patient and maternal age group increases.')
    st.write('5. Birth weight increase when the gestational week group increase.')
    st.write('6. Birth weight of the female newborns is relatively less compared to male newborns')
def ht():
    st.header('Hypertension')
    ht_level = st.multiselect("Select the Hyertension(Yes/No):",
                              options=df["ht"].unique(),
                              default=df["ht"].unique(), key='k5')
    df_selection = df.query(
        "ht == @ht_level"
    )
    st.subheader("Birth weight based on the Hypertension")
    fig1 = px.box(df_selection, x='ht', y='bweight',labels={'ht':'Hypertension','bweight':'Birth weight'})
    st.plotly_chart(fig1)
    t4 = df_selection.groupby(['ht'])['bweight'].aggregate(['count','sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t4)
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(t4)
    st.download_button(
        label="Download",
        data=csv,
        file_name='Hypertension.csv',
        mime='text/csv',)

    st.write("1. We can see lowest birthweight and some extreme value is present when the mother is a hypertension patient but when the mother is hypertension patient the lower fence is 980.")
    st.write("2. The boxplot is more consistent for mother with no hypertension compared to mother with hypertension.")
    st.write("3. From the mean we can see there is a huge difference in the birth weight which is relatively greater when the mother is not a hypertension patient.")

def matagegp():
    st.subheader('Maternal age group')
    matagegp_level = st.multiselect("Select the Matagegp :",
                                   options=df["matagegp"].unique(),
                                   default=df["matagegp"].unique(), key='k5')
    df_selection = df.query(
        "matagegp == @matagegp_level"
    )
    st.subheader("Birth weight based on the maternal age group")
    fig3 = px.box(df_selection, x='matagegp', y='bweight', labels={'matagegp':'Maternal age group','bweight':'Birth weight'})
    st.plotly_chart(fig3)
    t5 = df_selection.groupby(['matagegp'])['bweight'].aggregate(['count','sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t5)
    st.write("1. All the boxplot median looks relatively same.")
    st.write('2. First three boxplot having almost same 25% birth weight except when the maternal age group is >=40')
    st.write('3. We can see lower birth weight is found in all the groups but in maternal age group 30-34 and 35-39 it is more.')
def gestcat():
    st.header('Gestational age categories')
    gestcat_level = st.multiselect("Select the gestational age categories:",
                                    options=df["gestcat"].unique(),
                                    default=df["gestcat"].unique(), key='k5')
    df_selection = df.query(
        "gestcat == @gestcat_level"
    )
    st.subheader("Birth weight based on the Gestational age categories")
    fig = px.box(df_selection, x='gestcat', y='bweight', labels={'gestcat':'Gestational age category','bweight':'Birth weight'})
    st.plotly_chart(fig)
    t6 = df_selection.groupby(['gestcat'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t6)
    st.write("1. Birth weight is more consistent when the gestational age category is  >=37 and 25% of the babies are 3000 from this category.")
    st.write("2. Birth weight is maximum when the gestational age category is >=37.")
    st.write("3. Birth weight of the newborns in the gestational age category <37 are below 2320.")

df['matagegp']=np.where((df['matagegp']==1),'20–29',
                np.where((df['matagegp']==2),'30–34',
                np.where((df['matagegp']==3),'35–39 ',
                '>=40')))
df['gestcat']=np.where((df['gestcat']==1),'<37', '>=37')
if side == 'Home':
    home()
    st.write("Birthweight refers to the weight of a newborn baby at the time of their birth, typically measured in grams. It is a critical indicator of an infant's overall health and development. Low birthweight, often defined as less than 2,500 grams, can be associated with various health risks and complications, while a healthy birthweight is generally considered to be between 2,500 and 4,000 grams.")
    st.subheader('Questions')
    st.write('What factors affect the babies weight?')
elif side == 'Data Header':
    st.title("Birth weight dataset")
    Data_Header()
    st.write('Dimensions of the dataset')
    df.shape
    st.write("Attributes \n1) Matage - Mother's age at the time of delivery \n2) Ht - Hypertension, whether the mother is hypertension patient or not. \n3) Gestwks - Gestational age is the common term used during pregnancy to describe how far along the pregnancy is. It is measured in weeks.\n4) Sex - Gender of the newborn baby whether male/female \n5) Bweight - Birth weight is the first weight of the newborn baby, taken just after being born. It is measured in grams (g). \n6) Matagegp - Maternal age group, women were categorised according to maternal age into four groups; maternal age 20–29 years, maternal age 30–34 years, maternal age 35–39 years and maternal age 40 years and older. \n7) Gestcat - Gestational age categories tells us Pre-term: less than 259 days (37 weeks), term: 259–293 days (37–42 weeks)")

elif side =="Baby's Info":
    Pinfo()
elif side =="Mother's Info":
    Minfo()
elif side =='Report':
    report()

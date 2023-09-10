import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
df=pd.read_csv('BirthWt.csv')
def home():
    st.title("Welcome to Birth Weight data presentation")
    image = Image.open('image.png')
    st.image(image, caption='Birth Weight')
def Data_Header():
    st.write(df.head())
def Pinfo():
    tab1, tab2 = st.tabs(['Birth weight', "Mother's age"])
    with tab1:
        sex_level = st.multiselect("Select the sex:",
                                               options=df["sex"].unique(),
                                               default=df["sex"].unique(), key='k2')
        df_selection = df.query(
            "sex == @sex_level"
        )
        fig1 = px.histogram(df_selection, x='bweight', color='sex', title='Birth Weight of the newborn based on gender',labels={'bweight':'Birth weight'})
        st.plotly_chart(fig1)
        t1 = df_selection.groupby(['sex'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t1)
        st.write("1. Majority of the newborn's birth weight lies between 2500 and 3700, but birth weight more than 4600 could be found in less proportion.")
        st.write("2. Almost constant number of newborns from the birth weight spread between 0 to 2100")
        st.write("3. From the table, first half of the male newborns are below the birth weight of 3290 ")
        st.write("3. From the table, first half of the femmale newborns are below the birth weight of 3120 ")
    with tab2:
        matage_selection = st.slider('Mother age:',
                                  min_value=min(df['matage']),
                                  max_value=max(df['matage']),
                                  value=(min(df['matage']), max(df['matage'])))
        mask = (df['matage'].between(*matage_selection))

        sex_level = st.multiselect("Select the sex:",
                                   options=df["sex"].unique(),
                                   default=df["sex"].unique(),key="k1")
        df_selection = df.query(
            "sex == @sex_level"
        )
        fig2 = px.scatter(df_selection[mask], x="matage", y="bweight", title="Birth weight based on mother's age",
                          labels={'bweight': 'Birth weight', 'matage': 'Mother age'}, color='sex')
        st.plotly_chart(fig2)

        mask = (df['matage'].between(*matage_selection)) & (df['sex'].isin(df_selection))

        st.write("1. From this graph we could see that more number of male newborns are greater than birth weight of 4000 compared to female newborns.")
        st.write("2. Also from this graph we could see that there are few number of newborns less than birth weight of 1000, in which majority are female newborns.")
        st.write("3. Most of the newborn's birth weight is in the range of 2500 to 3700.")
        st.write("4. From this graph we could see that birth weight between 2500 to 4000, the mother's age is below 25 and the gender of the newborns are female.")
def Minfo():
    options = st.selectbox('select the variable', ["Hypertension","Gestational week","Matagegp","Gestational age categories"])
    if options=='Hypertension':
        ht()
    elif options =='Gestational week':
        gestwks()
        st.write("1. From this graph we can see there are some newborns birth weight less than 1000 when the gestational week in the range between 24 to 32.")
        st.write("2. Also from the graph we can see that maximum number of newborns birthweight in the range 2500 to 4000 and when the Gestational week is between 37 and 42.")
        st.write("3. It is a postive slope line, from this we can say when birthweight depends on Gestational week")
    elif options =='Matagegp ':
        matagegp()
    elif options =='Gestational age categories':
        gestcat()
st.sidebar.title("Direction")
side=st.sidebar.radio('Select what you want to see:', ['Home', 'Data Header', 'Personal Info','Medical Info', 'Report'])

def report():
    st.title('Conclusion')
    st.write('1. Birth weight of newborns are more consistent when the mother has no hypertension.')
    st.write('2. When the gestational week increases the birth weight of the newborns also increase respectively.')
    st.write('3. Matagegp does not affect the birth weight.')
    st.write('4. When the gestational age category 2, newborns birth weight is more consistent.')
    st.write('5. Average number of healthly newborn weight is in the range between 2500 to 4000 based on the graph.')
    st.write('6. Factor that affect birth weight are hypertension, sex, gestational week and gestational age categories.')
def ht():
    st.header('Hypertension')
    ht_level = st.multiselect("Select the Hyertension(Yes/No):",
                              options=df["ht"].unique(),
                              default=df["ht"].unique(), key='k5')
    df_selection = df.query(
        "ht == @ht_level"
    )
    fig1 = px.box(df_selection, x='ht', y='bweight',labels={'ht':'Hypertension','bweight':'Birth weight'})
    st.plotly_chart(fig1)
    t4 = df_selection.groupby(['ht'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t4)
    st.write("1. From the graph person without hypertension have more consistent birth weight compared to person with hypertension graph.")
    st.write("2. Newborn with lowest birth weight is born for person with no hypertension.")
    st.writr("3. The average birth weight of the person with hypertension is significantly less ")
def gestwks():
    st.header('Gestational week')
    fig2 = px.scatter(df, x='gestwks', y='bweight', labels={'gestwks':'Gestational week','bweight':'Birth weight'})
    st.plotly_chart(fig2)
def matagegp():
    st.header('Matagegp ')
    matagegp_level = st.multiselect("Select the Matagegp :",
                                   options=df["matagegp"].unique(),
                                   default=df["matagegp"].unique(), key='k5')
    df_selection = df.query(
        "matagegp == @matagegp_level"
    )
    fig3 = px.box(df_selection, x='matagegp', y='bweight', labels={'matagegp':'Matagegp (in years)','bweight':'Birth weight'})
    st.plotly_chart(fig3)
    t5 = df_selection.groupby(['matagegp'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t5)
    st.write("1. From this graph Matagegp does not affect the birth weight of the newborns.")
    st.write('2. Maximum birth weight is significantly less for Matagegp ')
def gestcat():
    st.header('Gestational age category')
    gestcat_level = st.multiselect("Select the gestational age category:",
                                    options=df["gestcat"].unique(),
                                    default=df["gestcat"].unique(), key='k5')
    df_selection = df.query(
        "gestcat == @gestcat_level"
    )
    fig = px.box(df_selection, x='gestcat', y='bweight', labels={'gestcat':'Gestational age category','bweight':'Birth weight'})
    st.plotly_chart(fig)
    t6 = df_selection.groupby(['gestcat'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t6)
    st.write("1. From this graph we can see that birth weight is more consistent when the gestational age category is 2 compare to gestational age category as 1.")
    st.write("2. Birth weight is maximum when the gestational age category is 2.")
    st.write("3. Birth weight is minimum when  the gestational age category is 1.")

if side == 'Home':
    home()
    st.write("The Birth Weight dataset is a collection of records documenting the birth weights of newborn infants.This dataset includes variables like Id, birth weight, gestational age, maternal age, hypertension, sex, maternal gap, and Gestcat.")
elif side == 'Data Header':
    st.title("Birth weight dataset")
    Data_Header()
    st.write('Dimensions of the dataset')
    df.shape
    st.write("Attributes \n1) Matage - Mother's age \n2) Ht - Hypertension, whether the mother is hypertension patient or not. \n3) Gestwks - Gestational age is the common term used during pregnancy to describe how far along the pregnancy is. It is measured in weeks. \n4) Bweight - Birth weight is the first weight of the newborn baby, taken just after being born. It is measured in grams (g). \n5) Matagegp - Mother's gap between the first baby and next baby .  \n6) Gestcat - Gestational age categories.")

elif side =='Personal Info':
    Pinfo()
elif side =='Medical Info':
    Minfo()
elif side =='Report':
    report()

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
    tab1, tab2, tab3 = st.tabs(['Birth weight', "Mother's age", 'Sex'])
    with tab1:
        sex_level = st.multiselect("Select the sex:",
                                               options=df["sex"].unique(),
                                               default=df["sex"].unique(), key='k2')
        df_selection = df.query(
            "sex == @sex_level"
        )
        fig1 = px.histogram(df_selection, x='bweight', color='sex', title='Birth Weight of the newborn based on gender')
        st.plotly_chart(fig1)
        t1 = df_selection.groupby(['sex'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t1)
        st.write("1. Majority of birth weight lies between 2300 and 3900, but birth weight more than 4600 could found in less proportion.")
        st.write("2. Almost constant birth weight spread from 0 to 2100")
        st.write("3. This graph shows many number of male newborns with birth weights are more compared to female newborns")

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
        t2 = df_selection[mask].groupby(['sex'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t2)

        mask = (df['matage'].between(*matage_selection)) & (df['sex'].isin(df_selection))

        st.write("1. From this graph we could see that more number of male newborns are greater than birth weight of 4000 compared to female newborns.")
        st.write("2. Also from this graph we could see that there are few number of newborns less than birth weight of 1000, in which majority are female newborns.")
        st.write("3. Most of the newborn's birth weight is in the range of 2500 to 3900.")
        st.write("4. From this graphs we could see that birth weight between 2500 to 4000 the mother's age is below 25 and the gender of the newborns are female.")
        st.write("5. More birth weight spread in the range 2500 to 3700.")

    with tab3:
        sex_level = st.multiselect("Select the sex:",
                                   options=df["sex"].unique(),
                                   default=df["sex"].unique(), key='k3')
        df_selection = df.query(
            "sex == @sex_level"
        )
        fig3 = px.box(df_selection, y='bweight', x='sex', title='Birth weight based on the sex',
                      labels={'bweight': 'Birth weight', 'sex': 'Sex'})
        st.plotly_chart(fig3)
        t3 = df_selection.groupby(['sex'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t3)
        st.write("1. After comparing both the box plot, we can conclude that male newborn birth weight is relatively greater than female newborn.")
        st.write("2. By comparing extreme points for birth weight with respect to gender, birth weight for female newborn is less than male newborn.")
        st.write("3. More spread in birth weight when the gender is male by comparing female.")
def Minfo():
    options = st.selectbox('select the variable', ["Hypertension","Gestational week","Menstrual gap","Gestational period"])
    if options=='Hypertension':
        ht()
    elif options =='Gestational week':
        gestwks()
        st.write("1. From this graph we can see there are some newborns birth weight less than 1000 when the gestational week in the range between 24 to 32.")
        st.write("2. Also from the graph we can see that maximum number of newborns birthweight in the range 2500 to 4000 and when the Gestational age is between 37 and 42.")
        st.write("3. It is a postive slope line, from this we can say when birthweight depends on Gestational week")
    elif options =='Menstrual gap':
        matagegp()
    elif options =='Gestational period':
        gestcat()
st.sidebar.title("Direction")
side=st.sidebar.radio('Select what you want to see:', ['Home', 'Data Header', 'Personal Info','Medical Info', 'Report'])

def report():
    st.title('Conclusion')
    st.write('1. Birth weight of newborns are more consistent when the mother has no hypertension.')
    st.write('2. When the gestational week increases the birth weight of the newborns also increase respectively.')
    st.write('3. Menstrual gap does not affect the birth weight.')
    st.write('4. When the gestational period is 2 the newborns birth weight is more consistent.')
    st.write('5. Birth weight of the newborns also depends on it is sex.')
    st.write('6. Average number of healthly newborn weight is in the range between 2500 to 4000 based on the graph.')
    st.write('7. Factor that affect birth weight are hypertension, sex, gestational week and gestational period.')
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
    st.write("1. From the graph person without hyper tension have more consistent birth weight compared to person with hypertension graph.")
    st.write("2. Newborn with lowest birth weight is born for person with no hypertension.")
def gestwks():
    st.header('Gestational week')
    fig2 = px.scatter(df, x='gestwks', y='bweight', labels={'gestwks':'Gestational week','bweight':'Birth weight'})
    st.plotly_chart(fig2)
def matagegp():
    st.header('Menstrual gap')
    matagegp_level = st.multiselect("Select the Menstrual gap:",
                                   options=df["matagegp"].unique(),
                                   default=df["matagegp"].unique(), key='k5')
    df_selection = df.query(
        "matagegp == @matagegp_level"
    )
    fig3 = px.box(df_selection, x='matagegp', y='bweight', labels={'matagegp':'Menstrual gap (in years)','bweight':'Birth weight'})
    st.plotly_chart(fig3)
    t5 = df_selection.groupby(['matagegp'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t5)
    st.write("1. From this graph Menstrual gap does not affect the birth weight of the newborns.")
def gestcat():
    st.header('Gestational period')
    gestcat_level = st.multiselect("Select the Gestational period:",
                                    options=df["gestcat"].unique(),
                                    default=df["gestcat"].unique(), key='k5')
    df_selection = df.query(
        "gestcat == @gestcat_level"
    )
    fig = px.box(df_selection, x='gestcat', y='bweight', labels={'gestcat':'Gestational period','bweight':'Birth weight'})
    st.plotly_chart(fig)
    t6 = df_selection.groupby(['gestcat'])['bweight'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
    st.dataframe(t6)
    st.write("1. From this graph we can see that birth weight is more consistent when the gestational period is 2 compare to gestational period as 1.")
    st.write("2. Birth weight is maximum when the gestational period is 2.")
    st.write("3. Birth weight is minimum when  the gestational period is 1.")

if side == 'Home':
    home()
    st.write("The Birth Weight dataset is a collection of records documenting the birth weights of newborn infants.This dataset includes variables like Id, birth weight, gestational age, maternal age, hypertension, sex, maternal gap, and Gestcat.")
elif side == 'Data Header':
    st.title("Birth weight dataset")
    Data_Header()
    st.write("Attributes \n1) Matage - Mother's age \n2) Ht - Hypertension, whether the mother is hypertension patient or not. \n3) Gestwks - Gestational age is the common term used during pregnancy to describe how far along the pregnancy is. It is measured in weeks. \n4) Bweight - Birth weight is the first weight of your baby, taken just after being born. It is measured in grams (g). \n5) Matagegp - Mother's gap between the first baby and next baby (in years).  \n6) Gestcat - The gestational period, in a medical context, refers to the duration of time that a pregnancy lasts, typically measured from the first day of the last menstrual period to the birth of the baby.")
    st.write('Dataset dimension')
    df.shape

elif side =='Personal Info':
    Pinfo()
elif side =='Medical Info':
    Minfo()
elif side =='Report':
    report()

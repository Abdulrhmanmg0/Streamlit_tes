import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from time import sleep
import sklearn
from sklearn.model_selection import train_test_split


page = 'Main'

df = pd.read_csv("C:\\Users\\abdul\\Downloads\\archive (6)\\insurance.csv")

df = df.dropna()
label_encoder = preprocessing.LabelEncoder()
label_encoder = preprocessing.LabelEncoder()

df['sex']= label_encoder.fit_transform(df['sex'])
df['smoker']= label_encoder.fit_transform(df['smoker'])
df['region']= label_encoder.fit_transform(df['region'])
Y = df['charges']
X = df.drop(['charges'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
from sklearn.linear_model import LinearRegression

LR = LinearRegression()
LR.fit(X_train, y_train)

train_predictions = LR.predict(X_train)
test_predictions = LR.predict(X_test)

if page == "Main":
    st.title("Machine Learning")
    st.write("## DataFrame")
    st.dataframe(df)
    col = X.columns.tolist()

    v1 = st.text_input(f"Enter value of {col[0]}")
    v2 = st.text_input(f"Enter value of {col[1]}")
    v3 = st.text_input(f"Enter value of {col[2]}")
    v4 = st.text_input(f"Enter value of {col[3]}")
    v5 = st.text_input(f"Enter value of {col[4]}")
    v6 = st.text_input(f"Enter value of {col[5]}")


    if st.button("Predict"):
        data = {
            col[0]: [int(v1)],
            col[1]: [int(v2)],
            col[2]: [int(v3)],
            col[3]: [int(v4)],
            col[4]: [int(v5)],
            col[5]: [int(v6)],
        }
        query = pd.DataFrame(data)
        prediction = LR.predict(query)
        st.markdown(f"Charges : ${prediction[0]}")



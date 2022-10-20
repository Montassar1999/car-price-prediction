import pickle
import streamlit as st

filename = 'model.sav'
# loading the saved model
loaded_model = pickle.load(open(filename, 'rb'))


# creating a function for Prediction

def price_prediction(input_data):

    prediction = loaded_model.predict([input_data])
    print(prediction)

    return prediction


def main():
    # giving a title
    st.title('Car Price Prediction Web App')

    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        Year = st.selectbox('Year', range(2005, 2022))
    with col2:
        Owner = st.selectbox('Owner', [0, 1, 2, 3, 4, 5])
    col3, col4 = st.columns(2)

    with col3:
        Fuel_Type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
    with col4:
        Seller_Type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
    Transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    col4, col5 = st.columns(2)
    with col4:
        Present_Price = st.text_input('Present Price')
    with col5:
        Kms_Driven = st.slider('Kms Driven',500,500000)


    #Casting Categorical Inputs
    f = [{'Petrol':0,'Diesel':1,'CNG':2}]
    fuel = f[0][Fuel_Type]
    s= [{'Dealer':0,'Individual':1}]
    seller = s[0][Seller_Type]
    t = [{'Manual':0,'Automatic':1}]
    transmission = t[0][Transmission]

    price = [0] * 1

    # creating a button for Prediction
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        btn = st.button('Get Price')
        if btn:
            price = price_prediction(
                [Year,Present_Price ,Kms_Driven ,fuel ,seller ,transmission,Owner])
    if btn:
        st.success(price[0])

    st.text('Developed By Montassar Khefifi')

if __name__ == '__main__':
    main()
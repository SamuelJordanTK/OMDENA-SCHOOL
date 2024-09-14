import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/PC/OneDrive/Attachments/MaintenacePredection/training_model.sav', 'rb'))

#creating a function for prediction

def machine_prediction(data_to_predict):
    
    input_data_as_numpy_array = np.asarray(data_to_predict)
    input_data_reshaping = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaping)
    print("Predicted class:", prediction)

    if prediction[0] == 0:
        return 'No Failure'
    elif prediction[0] == 1:
        return 'Heat Dissipation Failure'
    elif prediction[0] == 2:
        return 'Power Failure'
    elif prediction[0] == 3:
        return 'Overstrain Failure'
    elif prediction[0] == 4:
        return 'Tool Wear Failure'
    else:
        return 'Random Failures'
    

def main():
    #giving the title
    st.title('Machine Prediction Web App')
    # getting the input data from the user
    
    Type = st.text_input('Type')
    Air_temperature = st.text_input('Air_temperature temp[k]')
    Process_temperature = st.text_input('Process_temperature temp[k]')
    Rotational_speed  = st.text_input('Rotational_speed speed[rpm]')
    Torque = st.text_input('Torque Nm')
    Tool_wear =st.text_input('Tool_wear [min]')
    Target = st.text_input('Target')

    #code for prediction
    Machine_condition = ''
    #creatin a button for prediction
    
    if st.button('Machine Failer Type Result'):
        Machine_condition = machine_prediction([Type,Air_temperature,Process_temperature,Rotational_speed,Torque,Tool_wear,Target])

    st.success(Machine_condition)


# Run the Streamlit app
if __name__ == '__main__':
    main()
    
# install streamlit
import streamlit as st

# 1 Kilometer (km) = 1,000 Meters (m)
# 1 Meter = 0.001 Kilometers (km)
# 1 KiloMeter = 100000 Centimeters
# 1 Centimeter = 0.00001 Kilometer
# 1 Kilometer = 1000000 Millimeters
# 1 Millimeter = 0.000001 Kilometer
# 1 Kilometer = 39370.1 Inches
# 1 Inch = 0.0000254 Kilometer
# 1 foot = 0.0003048 Kilometer.
# 1 Kilometer = 1093.61 Yards
# 1 Yard = 0.0009144 Kilometer
# 1 Meter = 1000 Millimeters
# 1 Millimeter = 0.001 Meter
# 1 Meter = 39.3701 Inches.
# 1 Inch = 0.0254 Meter.
# 1 Meter = 1.09361 Yards.
# 1 Yard = 0.9144 Meter
# 1 Centimeter = 10 Millimeters
# 1 Millimeters = 0.1 Centimeter
# 1 Centimeter = 0.393701 Inches.
# 1 Inch = 2.54 Centimeters
# 1 Centimeter = 0.0109361 Yards.
# 1 Yard = 91.44 Centimeters
# 1 Millimeter = 0.03937 Inches.
# 1 Inch = 25.4 Millimeters.
# 1 Millimeter = 0.00109361 Yards.
# 1 Yard = 914.4 Millimeter
# 1 Inch = 0.02778 Yards. 
# 1 Yard = 36 Inches.

# conversion function
def unit_converter(value:float, convert_from:str, convert_to:str):
    print(value)
    print(convert_from)
    print(convert_to)
    # conditions
    if convert_from == "Kilometer" and convert_to == "Meter" :
        return value * 1000
    elif convert_from == "Meter" and convert_to == "Kilometer" :
        return value * 0.001
    elif convert_from == "Kilometer" and convert_to == "Centimeter" :
        return value * 100000
    elif convert_from == "Centimeter" and convert_to == "Kilometer" :
        return value * 0.00001
    elif convert_from == "Kilometer" and convert_to == "Millimeter" :
        return value * 1000000
    elif convert_from == "Millimeter" and convert_to == "Kilometer" :
        return value * 0.000001
    elif convert_from == "Kilometer" and convert_to == "Inch" :
        return value * 39370.1
    elif convert_from == "Inch" and convert_to == "Kilometer" :
        return value * 0.0000254
    elif convert_from == "Kilometer" and convert_to == "Yard" :
        return value * 1093.61
    elif convert_from == "Yard" and convert_to == "Kilometer" :
        return value * 0.0009144
    elif convert_from == "Meter" and convert_to == "Centimeter":
        return value * 100
    elif convert_from == "Centimeter" and convert_to == "Meter":
        return value * 0.01
    elif convert_from == "Meter" and convert_to == "Millimeter":
        return value * 1000
    elif convert_from == "Millimeter" and convert_to == "Meter":
        return value * 0.001
    elif convert_from == "Meter" and convert_to == "Inch":
        return value * 39.3701
    elif convert_from == "Inch" and convert_to == "Meter":
        return value * 0.0254
    elif convert_from == "Meter" and convert_to == "Yard":
        return value * 1.09361
    elif convert_from == "Yard" and convert_to == "Meter":
        return value * 0.9144
    elif convert_from == "Centimeter" and convert_to == "Millimeter":
        return value * 10
    elif convert_from == "Millimeter" and convert_to == "Centimeter":
        return value * 0.1
    elif convert_from == "Centimeter" and convert_to == "Inch":
        return value * 0.393701
    elif convert_from == "Inch" and convert_to == "Centimeter":
        return value * 2.54
    elif convert_from == "Centimeter" and convert_to == "Yard":
        return value * 0.0109361
    elif convert_from == "Yard" and convert_to == "Centimeter":
        return value * 91.44
    elif convert_from == "Millimeter" and convert_to == "Inch":
        return value * 0.03937 
    elif convert_from == "Inch" and convert_to == "Millimeter":
        return value * 25.4  
    elif convert_from == "Millimeter" and convert_to == "Yard":
        return value *  0.00109361 
    elif convert_from == "Yard" and convert_to == "Millimeter":
        return value *  914.4 
    elif convert_from == "Inch" and convert_to == "Yard":
        return value *  0.02778  
    elif convert_from == "Yard" and convert_to == "Inch":
        return value * 36  
    else:
        return "Conversion not supported"


       
# Streamlit UI
st.set_page_config(page_title="Google Unit Converter", page_icon="🔁")
st.title("🔁 :blue[Google Unit Converter]")

# Custom background color using CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;  
    }
    .stApp {    
        background-color: #000000;
      
    }
    </style>
""", unsafe_allow_html=True)



# main function with streamlit  ** for bold 
st.selectbox("**:blue[Unit]**", ["Lenght"])

# Input: value to convert
value = float(st.number_input("**:blue[Enter your value]**", min_value=0))

col1,col2 = st.columns([4,4])
with col1:
  # Select box for choosing units
  convert_from = st.selectbox("**:blue[Choose unit to convert from]**", ["Kilometer", "Meter", "Centimeter", "Millimeter", "Inch", "Yard"])

with col2:  
  # Select box for choosing units
  convert_to = st.selectbox("**:blue[Choose unit to convert to]**", ["Kilometer", "Meter", "Centimeter", "Millimeter", "Inch", "Yard"])


# Call the converter function and display the result
if st.button("**Convert**") :
    result = unit_converter(value, convert_from, convert_to)
   # result_str = "{:.1e}".format(result)  # This formats the result as scientific notation with 1 decimal place

   # f: This indicates that you're formatting a floating-point number (i.e., a decimal number).
    #.2: This specifies that you want the number to be displayed with 2 decimal places.
    st.write(f"Result: {value} {convert_from} is equal to {result:2f} {convert_to}")


    
    
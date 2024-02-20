import streamlit as st
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Calculate Haversine distance between two points in kilometers
    R = 6371  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def main():
    st.title("Find Nearest Delivery Office")
    
    # File upload widget for delivery offices CSV file
    uploaded_file = st.file_uploader("Upload Delivery Offices CSV", type="csv")
    
    if uploaded_file is not None:
        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)
        
        # User input for latitude and longitude
        latitude = st.number_input("Enter Latitude:", value=18.9101004)
        longitude = st.number_input("Enter Longitude:", value=72.83394)
        
        # Process DataFrame to extract office codes and coordinates
        delivery_offices = dict(zip(df['FR CODE'], zip(df['Latitude'], df['Longitude'])))
        
        # Calculate Haversine distance for each delivery office
        min_distance = float('inf')
        nearest_office = None
        for office_code, office_point in delivery_offices.items():
            distance = haversine_distance(latitude, longitude, office_point[0], office_point[1])
            if distance < min_distance:
                min_distance = distance
                nearest_office = office_code
        
        # Display results
        st.write(f"The minimum Haversine distance is {min_distance:.2f} km.")
        st.write(f"Nearest CP: {nearest_office}")

if __name__ == "__main__":
    main()

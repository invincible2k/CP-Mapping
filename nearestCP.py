import pandas as pd
from math import radians, sin, cos, sqrt, atan2
import streamlit as st

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = radians(float(lat1))
    lon1_rad = radians(float(lon1))
    lat2_rad = radians(float(lat2))
    lon2_rad = radians(float(lon2))
    
    # Calculate Haversine distance between two points in kilometers
    R = 6371  # Earth radius in kilometers
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def find_nearest_delivery_office(point, delivery_offices):
    # Calculate Haversine distance for each delivery office
    min_distance = float('inf')
    nearest_office = None
    for office_code, office_point in delivery_offices.items():
        distance = haversine_distance(point.latitude, point.longitude, office_point[0], office_point[1])
        if distance < min_distance:
            min_distance = distance
            nearest_office = office_code
    return min_distance, nearest_office

def main():
    st.title("Find Nearest Delivery Office")
    
    try:
        # User input for latitude and longitude
        latitude_str = st.text_input("Enter Latitude (in degrees):")
        latitude = float(latitude_str)
        
        longitude_str = st.text_input("Enter Longitude (in degrees):")
        longitude = float(longitude_str)
    except ValueError:
        st.error("Invalid input. Latitude and longitude must be numeric values.")
        return
    
    # Create a point object using the provided latitude and longitude
    point = Point(latitude, longitude)
    
    # Load delivery offices data from Excel file
    delivery_offices_df = pd.read_excel("cp_coord.xlsx")
    delivery_offices = dict(zip(delivery_offices_df['FR CODE'], zip(delivery_offices_df['Latitude'], delivery_offices_df['Longitude'])))
    
    # Find nearest delivery office
    min_distance, nearest_office = find_nearest_delivery_office(point, delivery_offices)
    
    # Display results
    st.write(f"The minimum Haversine distance is {min_distance:.2f} km.")
    st.write(f"Nearest CP: {nearest_office}")

if __name__ == "__main__":
    main()

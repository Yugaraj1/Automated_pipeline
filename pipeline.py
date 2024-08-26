import requests
import pandas as pd
import sqlalchemy
import random

def randomcitygenerator():
    cities = [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
        'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
        'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Indianapolis',
        'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'El Paso',
        'Detroit', 'Boston', 'Memphis', 'Baltimore', 'Oklahoma City',
        'Las Vegas', 'Louisville', 'Milwaukee', 'Albuquerque', 'Tucson',
        'Fresno', 'Sacramento', 'Kansas City', 'Mesa', 'Virginia Beach',
        'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami',
        'Cleveland', 'Tulsa', 'Oakland', 'Minneapolis', 'Wichita',
        'Arlington', 'Bakersfield', 'Tampa', 'Aurora', 'Honolulu',
        'Anaheim', 'Santa Ana', 'Corpus Christi', 'Riverside', 'St. Louis',
        'Lexington', 'Stockton', 'Henderson', 'Greensboro', 'Jersey City',
        'Chula Vista', 'Buffalo', 'Fort Wayne', 'Chandler', 'St. Petersburg',
        'Laredo', 'Norfolk', 'Durham', 'Madison', 'Lubbock',
        'Irvine', 'Winston-Salem', 'Glendale', 'Garland', 'Hialeah',
        'Reno', 'Baton Rouge', 'Richmond', 'Boise', 'Des Moines',
        'Spokane', 'San Bernardino', 'Modesto', 'Fargo', 'Tacoma',
        'Bellevue', 'Santa Clara', 'Salem', 'Providence', 'Murrieta',
        'Oceanside', 'Temecula', 'Grand Prairie', 'Brownsville', 'Overland Park',
        'Jackson', 'Chattanooga', 'Fort Collins', 'Montgomery', 'Augusta',
        'Akron', 'Little Rock', 'Huntington Beach', 'Yonkers', 'Glendale',
        'Fargo', 'Boulder', 'Champaign', 'Peoria', 'Springfield',
        'Denton', 'Cary', 'Lakewood', 'Carrollton', 'Clearwater',
        'Draper', 'Sandy', 'West Jordan', 'Kennewick', 'Bellingham',
        'La Habra', 'Eugene', 'Vancouver', 'Pasadena', 'Tempe',
        'Sunnyvale', 'Garden Grove', 'Inglewood', 'Cleveland Heights', 'Yuma',
        'Palm Bay', 'Bismarck', 'Lynn', 'Portsmouth', 'Gainesville',
        'Macon', 'Warner Robins', 'Shreveport', 'Springdale', 'Richmond',
        'Jacksonville', 'Napa', 'Burlington', 'Asheville', 'Manhattan',
        'Waco', 'College Station', 'Brunswick', 'Huntington', 'Lynchburg',
        'Lima', 'Guayaquil', 'Quito', 'Bogotá', 'Lima',
        'Mexico City', 'Buenos Aires', 'São Paulo', 'Rio de Janeiro', 'Santiago',
        'Montevideo', 'Asunción', 'Caracas', 'Lima', 'La Paz',
        'Sucre', 'San Salvador', 'Guatemala City', 'San José', 'Managua',
        'Havana', 'Port-au-Prince', 'Kingston', 'Nassau', 'Bridgetown'
    ]

    return random.choice(cities)

def fetch_and_store_weather_data():
    # Weatherstack API details
    API_KEY = '#######################'
    BASE_URL = 'http://api.weatherstack.com/current'
    city = randomcitygenerator()

    # Construct the URL
    url = f'{BASE_URL}?access_key={API_KEY}&query={city}'

    # Fetch weather data from Weatherstack API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()
        print("Weather Data Fetched Successfully")
        print(weather_data)
        
        # Extract relevant data
        data = {
            'City': [weather_data['location']['name']],
            'Country': [weather_data['location']['country']],
            'Region': [weather_data['location']['region']],
            'Latitude': [weather_data['location']['lat']],
            'Longitude': [weather_data['location']['lon']],
            'Timezone': [weather_data['location']['timezone_id']],
            'Local_Time': [pd.to_datetime(weather_data['location']['localtime'])],
            'Temperature': [weather_data['current']['temperature']],
            'Weather_Description': [weather_data['current']['weather_descriptions'][0]],
            'Weather_Icon': [weather_data['current']['weather_icons'][0]],
            'Wind_Speed': [weather_data['current']['wind_speed']],
            'Wind_Direction': [weather_data['current']['wind_dir']],
            'Pressure': [weather_data['current']['pressure']],
            'Precipitation': [weather_data['current']['precip']],
            'Humidity': [weather_data['current']['humidity']],
            'Cloud_Cover': [weather_data['current']['cloudcover']],
            'Feels_Like': [weather_data['current']['feelslike']],
            'UV_Index': [weather_data['current']['uv_index']],
            'Visibility': [weather_data['current']['visibility']],
            'Is_Day': [weather_data['current']['is_day']]
        }
        
        # Create DataFrame
        weather_df = pd.DataFrame(data)
        print(weather_df)
        
        # Database connection string
        engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost/api')
        
        # Insert DataFrame into MySQL table
        weather_df.to_sql(name='weather_data', con=engine, if_exists='append', index=False)

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Create an object of ToastNotifier class
n = ToastNotifier()

# function defined to get URL
def getdata(url):
    try:
        r = requests.get(url)
        r.raise_for_status() 
        return r.text
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Website for weather report
url = "https://weather.com/en-IN/weather/today/l/953a2fdc38286a392c415532b7c33980cd9f07b148cac5950911c711473e018a"
htmldata = getdata(url)

if htmldata:
    soup = BeautifulSoup(htmldata, 'html.parser')

    #Extracting info
    location_element = soup.find("h1", class_="CurrentConditions--location--1YWj_")
    location = location_element.text if location_element else "N/A"

    current_condition = soup.find("div", class_="CurrentConditions--phraseValue--mZC_p")
    condition = current_condition.text if current_condition else "N/A"

    current_temp = soup.find("span", class_="CurrentConditions--tempValue--MHmYY")
    temperature = current_temp.text if current_temp else "N/A"
    
    # Construct the result
    result = f"Location: {location}\nCondition: {condition}\nTemperature: {temperature}"

    # Display the toast notification
    n.show_toast("Live Weather Update", result, duration=20)
else:
    print("Failed to retrieve weather data.")

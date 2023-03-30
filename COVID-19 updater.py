import requests

url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
response = requests.get(url)

data = response.content.decode().split("\n")

# Get the latest data
latest_data = data[-2].split(",")

new_cases = latest_data[5]
new_deaths = latest_data[7]

print("COVID-19 Update:")
print("New Cases:", new_cases)
print("New Deaths:", new_deaths)

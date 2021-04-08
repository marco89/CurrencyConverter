import requests
from bs4 import BeautifulSoup

# Requests HTML from source website
page = requests.get('https://www.x-rates.com/table/?from=GBP&amount=1')

# Converts and parses HTML to usable data
soup = BeautifulSoup(page.content, 'html.parser')

# Finds relevant data types needed which is all currency to currency figures (those that begin with rtRates)
soup_figure = soup.find_all('td', attrs={'class': 'rtRates'})

# Selects the required currency from list, in this case GBP to USD
initial_rate = str(soup_figure[0])

# Cuts away all unneeded text from previous selection, also converts to float
rate = float(str(initial_rate[81:88]))

# Asks user input in float form
gbp_input = float(input('Please input amount of GBP you would like to convert to USD:'))

# Multiplies user input figure by current exchange rate
conv = round(gbp_input * rate, 2)

print('£', gbp_input, 'is', '$', conv)


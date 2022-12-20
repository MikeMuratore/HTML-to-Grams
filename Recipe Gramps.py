import requests
from bs4 import BeautifulSoup

# Prompt the user for a link to a recipe website
link = input("Enter the link to the recipe website: ")

# Make a request to the website and retrieve the HTML
html = requests.get(link).text

# Use Beautiful Soup to parse the HTML and extract the ingredients
soup = BeautifulSoup(html, 'html.parser')
ingredients = soup.find_all('li', {'class': 'ingredient'})

# Convert each ingredient to grams
for ingredient in ingredients:
  # Extract the ingredient name and amount
  name = ingredient.find('span', {'class': 'ingredient-name'}).text
  amount = ingredient.find('span', {'class': 'ingredient-amount'}).text

  # Convert the amount to grams
  # (Note: This conversion will only work for ingredients that are measured in cups, tablespoons, or teaspoons)
  if 'cup' in amount:
    amount_in_grams = float(amount.split(' ')[0]) * 236.588
  elif 'tablespoon' in amount:
    amount_in_grams = float(amount.split(' ')[0]) * 14.7868
  elif 'teaspoon' in amount:
    amount_in_grams = float(amount.split(' ')[0]) * 4.92892

  # Print the ingredient name and amount in grams
  print(f'{name}: {amount_in_grams:.2f} grams')

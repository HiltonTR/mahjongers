from dotenv import dotenv_values

config = dotenv_values('.env')
print(config['YELP_API_KEY'])
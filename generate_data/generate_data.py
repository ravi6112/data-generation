import random
import pandas as pd
from faker import Faker
from collections import defaultdict
import random 
# from sqlalchemy import create_engine

fake =  Faker()

fake_data = defaultdict(list)

for i in range(1000):
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )
    fake_data["project_id"].append( random.randint(1, 10000))


df_fake_data = pd.DataFrame(fake_data)

df_fake_data.to_csv('/Users/ganeshandineshkumar/Documents/generates_data/sample.csv')
print(df_fake_data)
import pandas as pd
df = pd.read_csv('customer_shopping_behavior.csv')

# print(df.head())
# print(df.info())
# print(df.describe())

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
df = df.rename(columns={'purchase_amount_(usd)':'purchased_amount'})

#create a column age_group

labels = ['Young Adult','Adult','Mid-aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels = labels)

#create column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['frequency_of_purchases']= df['frequency_of_purchases'].map(frequency_mapping)


# print(df.isnull().sum())
# print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
# print(df.info())


# print((df['discount_applied'] == df['promo_code_used']).all())
df = df.drop('promo_code_used', axis=1)
# print(df.columns)

from sqlalchemy import create_engine

username = "root"
password = "urvansh33!"       # your new password
host = "127.0.0.1"
port = "3306"
database = "customer_behavior"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

df.to_sql(
    "customer",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into MySQL")


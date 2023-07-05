import pandas as pd
from pprint import pprint

def generate_keywords(products, words):
    keywords_list = []
    
    for product in products:
        for word in words:
            keywords_list.append([product, product + ' ' + word])
            keywords_list.append([product, word + ' ' + product])
    
    return keywords_list

# Input from the user
products = input("Enter products (comma-separated): ").split(",")
words = input("Enter words (comma-separated): ").split(",")

# Generate keywords
keywords_list = generate_keywords(products, words)
pprint(keywords_list)

keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it
print(keywords_df)

keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})

keywords_df['Campaign'] = 'SEM_Sofas'

keywords_df['Criterion Type'] = 'Exact'

keywords_phrase = keywords_df.copy()
keywords_phrase['Criterion Type'] = 'Phrase'

keywords_df_final = pd.concat([keywords_df, keywords_phrase])

keywords_df_final.to_csv('keywords.csv', index=False)

summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
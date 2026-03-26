"""
Lab Assignment-1
Question: Create a Panda Dataframe script by reading a file "books.csv". 
The "books.csv" contains information regarding the books such as title, 
name of author, edition, publication year and publishing house, price. 
Create an application to perform the following operations:
a) Print the complete report of books in a Tabular form.
b) Print the list of available books of a given author.
c) Print the list of available books of a given publishing house.
d) Print the Titles of cheapest & costliest book available.
e) Print the list by sorting based on the year of publication.
"""

import pandas as pd

# Creating a sample CSV for demonstration (Run this once to create the file)
data = {
    'title': ['Python Basics', 'Data Science', 'ML Guide', 'AI Ethics', 'Deep Learning'],
    'author': ['John Smith', 'Jane Doe', 'John Smith', 'Robert Brown', 'Jane Doe'],
    'edition': [1, 3, 2, 1, 4],
    'year': [2015, 2021, 2018, 2023, 2019],
    'publisher': ['TechPress', 'GlobalPub', 'TechPress', 'Sage', 'GlobalPub'],
    'price': [450, 800, 600, 350, 1200]
}
pd.DataFrame(data).to_csv('books.csv', index=False)

# Main Application
def book_analysis():
    df = pd.read_csv('books.csv')

    # a) Complete report
    print("\n--- a) Complete Book Report ---")
    print(df.to_string(index=False))

    # b) Books by given author
    author_name = "John Smith"
    print(f"\n--- b) Books by {author_name} ---")
    print(df[df['author'] == author_name])

    # c) Books by given publisher
    pub_house = "TechPress"
    print(f"\n--- c) Books from {pub_house} ---")
    print(df[df['publisher'] == pub_house])

    # d) Cheapest & Costliest
    cheapest = df.loc[df['price'].idxmin(), 'title']
    costliest = df.loc[df['price'].idxmax(), 'title']
    print(f"\n--- d) Price extremes ---")
    print(f"Cheapest: {cheapest} | Costliest: {costliest}")

    # e) Sort by year
    print("\n--- e) Sorted by Publication Year ---")
    print(df.sort_values(by='year'))

if __name__ == "__main__":
    book_analysis()

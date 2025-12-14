import pandas as pd
data = {
    'Name': ['Ali', 'Sara', 'John', 'Ayesha', 'Tom'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi'],
    'Score': [88, 92, 95, 70, 60]
}
df = pd.DataFrame(data)

# 1. head() → Top 3 rows
print("Top 3 rows:")
print(df.head(3))

# 2. tail() → Last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# 3. at[] → Specific value by label
print("\nValue at row 1, column 'City':")
print(df.at[1, 'City'])  # Sara ka sheher

# 4. iat[] → Specific value by position
print("\nValue at row 2, column 3 (Score):")
print(df.iat[2, 3])  # John ka score

# 5. iloc[] → Pure integer-location based selection
print("\nRows 1 to 3, columns 0 to 2:")
print(df.iloc[1:4, 0:3])  # Sara se Ayesha tak, Name-Age-City

# 6. get() → Get column by key
print("\nGet 'Score' column:")
print(df.get('Score'))

# 7. isin() → Check if values exist
print("\nCheck if City is Lahore:")
print(df['City'].isin(['Lahore']))

# 8. where() → Filter with condition
print("\nWhere Score > 80:")
print(df.where(df['Score'] > 80))

# 9. mask() → Opposite of where
print("\nMask Score > 80:")
print(df.mask(df['Score'] > 80))

# 10. query() → Boolean expression
print("\nQuery: Age > 25 and City == 'Karachi'")
print(df.query("Age > 25 and City == 'Karachi'"))

# 11. insert() → Add new column
df.insert(2, 'Gender', ['M', 'F', 'M', 'F', 'M'])
print("\nAfter inserting 'Gender' column:")
print(df)

# 12. lookup() → Fancy indexing (deprecated in latest pandas)
# Note: lookup is deprecated, use .at or .loc instead
# Example alternative:
print("\nAlternative to lookup: Get Score for Ali and John")
names = ['Ali', 'John']
scores = [df.loc[df['Name'] == name, 'Score'].values[0] for name in names]
print(scores)

# 13. pop() → Remove column
print("\nPop 'Gender' column:")
gender_col = df.pop('Gender')
print("Popped column:", gender_col)
print("Remaining DataFrame:")
print(df)

# 14. xs() → Cross-section by label
print("\nCross-section by row index 2:")
print(df.xs(2))  # John ki row
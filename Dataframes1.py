import pandas as pd

list1 = ['this','is','pamdas','dataframes']

df1 = pd.DataFrame(list1)
print(df1)

dict1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 22],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df2 = pd.DataFrame(dict1)
print(df2)

print('\n********************************')
print(df2[['Name','Age']])

print(df2.nunique())
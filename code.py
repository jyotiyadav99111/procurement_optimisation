import pandas as pd

# Upload files and get into the format
file_path = 'data.xlsx'
df = pd.read_excel(file_path, skiprows=1)
df.drop(['Unnamed: 0', 'Unnamed: 1', 'S.No'], axis=1, inplace = True)
df.sort_values('Units Produced', inplace=True, ascending=False)
df_exp = df.copy()
print(df)

# Define parameters
N = 4
COLUMN = 'Units Produced'
PROD_CHANGE_COUNT = 0
EXTRA_ITEMS_PRODUCED = 0

# create a baseline
for item in df_exp[COLUMN]:
    EXTRA_ITEMS_PRODUCED += round(item) % N
    PROD_CHANGE_COUNT += 1

print('-'*100)
print('In the baseline model:')
print('PROD_CHANGE_COUNT: ', PROD_CHANGE_COUNT)
print('EXTRA_ITEMS_PRODUCED: ', EXTRA_ITEMS_PRODUCED)

# optimisation 1
PROD_CHANGE_COUNT = 0
EXTRA_ITEMS_PRODUCED = 0

if df_exp[COLUMN].shape[0] % N == 0:
    for item_no in range(df_exp[COLUMN].shape[0]):
        if item_no % N == 0 or item_no == 0:
            PROD_CHANGE_COUNT += 1
            EXTRA_ITEMS_PRODUCED += (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 1]) + \
                                    (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 2]) +\
                                    (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 3])
else:
    items_total = df_exp[COLUMN].shape[0] - (df_exp[COLUMN].shape[0] % N)
    for item_no in range(items_total):
        if item_no % N == 0 or item_no == 0:
            PROD_CHANGE_COUNT += 1
            EXTRA_ITEMS_PRODUCED += (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 1]) + \
                                    (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 2]) +\
                                    (df_exp[COLUMN][item_no] - df_exp[COLUMN][item_no + 3])

    PROD_CHANGE_COUNT += 1



print('-' * 100)
print('In the v01 model:')
print('PROD_CHANGE_COUNT: ', PROD_CHANGE_COUNT)
print('EXTRA_ITEMS_PRODUCED: ', EXTRA_ITEMS_PRODUCED)


#!/usr/bin/env python
# coding: utf-8

# # Automating Report Genaration with Pandas
# 
# Report showing the Annual profit for each product

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

def generate_pivot(df):
    df_pvt = df.pivot_table(index="Product",
                             aggfunc='sum',
                             )

    df_pvt.loc[:, 'Profit'] = df_pvt.Revenue - df_pvt.Expenditure
    return df_pvt

def plot_barchart(df):
    ax = sns.barplot(data = df.reset_index(),
                 y = 'Profit',
                 x = 'Product',
                )
    plt.title('Annual Profit for each Product');
    plt.tight_layout()
    plt.savefig('annual_profit.jpg')
    return ax

def store_in_excel(df, ax):
    imgdata = BytesIO()
    ax.figure.savefig(imgdata)

    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as FH:
        df_pvt[new_cols].to_excel(FH, sheet_name=year)
        shobj = FH.sheets[year]
        shobj.insert_image('E4', '', {'image_data': imgdata})


# Main starts from here
excel_filename = "Annual_Report.xlsx"
year = "2014"

toys_url = "https://raw.githubusercontent.com/asarfraaz/PyPractice/master/data/toys.csv"

df_toys = pd.read_csv(toys_url)

cols = df_toys.columns[1:] 
df_pvt = generate_pivot(df_toys[cols])

# Plotting the bar chart
ax = plot_barchart(df_pvt)

# ## Save the Annual Revenue Report in excel file
# 
# - The columns should be in the following order
#     - Revenue
#     - Expenditure
#     - Profit
# - Also include the image in it
# 

cols = df_pvt.columns.to_list()

# Prefer to do this, instead of writing the names of columns
new_cols = [ cols[1], cols[0], cols[-1] ]
#df_pvt[new_cols]

# Storing DataFrame and a plot in excel file
store_in_excel(df_pvt[new_cols], ax)

print("Successfully generated the report")

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataframe
df = pd.read_excel(r"C:\\Users\\Shivani\\.jupyter\\ANZ.xlsx")
print("Concise view of dataset:")
print(df.head(), "\n")


# In[3]:


print("Columns in dataframe:")
print(df.columns, "\n")

print(f'Total number of unique customers: {df["account"].nunique()}\n')

# Dropping irrelevant features like 'bpay_biller_code', 'account',
#      'currency', 'long_lat', 'txn_description', 'merchant_id',
#      'merchant_code', 'first_name','extraction','merchant_long_lat','transaction_id', 'country'

print("New dataframe after dropping irrelevant features:")
df = df[["status", "card_present_flag", "balance", "date", "gender", "age",
    "merchant_suburb", "merchant_state", "amount",
    "customer_id", "movement"]]
df["date"] = pd.to_datetime(df["date"])
print(df1.head(), "\n")


# Exploratory Data Analysis :

# In[8]:


print("Total number of transactions made each day decreasing order:\n")
print("Date \t Frequency")
print(df["date"].value_counts(), "\n")              


# In[9]:


print("Total number of transactions made by each customer in decreasing order:\n")
print("Customer ID \t Frequency")
print(df["customer_id"].value_counts(), "\n") 


# In[10]:


# Splitting dataset into three months - August, September and October
months = []
for date in df["date"]:
    if date.month == 8:
        months.append("August")
    elif date.month == 9:
        months.append("September")
    elif date.month == 10:
        months.append("October")

df["Months"] = months


# In[11]:


#VISUALIZATION

# Transaction volume each day
df_date_count = df.groupby("date").count()

trans_vol = df_date_count["customer_id"].mean()
n_points = len(df_date_count.index)

plt.figure()
plt.plot(df_date_count.index, df_date_count["customer_id"], c="black", label="Customer ID")
plt.plot(df_date_count.index, np.linspace(trans_vol, trans_vol, n_points), c="r", label="Mean transaction volume")
plt.title("ANZ Transaction Volume vs. Date")
plt.xlabel("Date")
plt.ylabel("Number of customers")
plt.legend()


# In[12]:


# Mean transaction amount each day
df_date_mean = df.groupby("date").mean()

trans_amt = df_date_mean["amount"].mean()
n_points = len(df_date_count.index)

plt.figure()
plt.plot(df_date_count.index, df_date_mean["amount"], c="black", label="Amount")
plt.plot(df_date_count.index, np.linspace(trans_amt, trans_amt, n_points), c="r", label="Overall mean transaction amount")
plt.title("ANZ Mean Transaction Amount vs. Date")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[13]:


# Mean customer balance and payment amount by age for each month in dataset
df_cus_aug = df[df["Months"] == "August"].groupby("customer_id").mean()
df_gen_aug = df[df["Months"] == "August"].groupby("gender").mean()

mean_f_bal_aug = df_gen_aug["balance"].iloc[0]
mean_m_bal_aug = df_gen_aug["balance"].iloc[1]
n_points = len(df_cus_aug["age"])

plt.figure()
plt.scatter(df_cus_aug["age"], df_cus_aug["balance"], c="black", label="Balance")
plt.plot(df_cus_aug["age"], np.linspace(mean_f_bal_aug, mean_f_bal_aug, n_points), c="r", label="Mean female balance")
plt.plot(df_cus_aug["age"], np.linspace(mean_m_bal_aug, mean_m_bal_aug, n_points), c="b", label="Mean male balance")
plt.title("ANZ Customer Balance vs. Age for August")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[14]:


mean_f_amt_aug = df_gen_aug["amount"].iloc[0]
mean_m_amt_aug = df_gen_aug["amount"].iloc[1]

plt.scatter(df_cus_aug["age"], df_cus_aug["amount"], c="black", label="Amount")
plt.plot(df_cus_aug["age"], np.linspace(mean_f_amt_aug, mean_f_amt_aug, n_points), c="r", label="Mean female amount")
plt.plot(df_cus_aug["age"], np.linspace(mean_m_amt_aug, mean_m_amt_aug, n_points), c="b", label="Mean male amount")
plt.title("ANZ Customer Mean Payment Amount vs. Age for August")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:


df_cus_sep = df[df["Months"] == "September"].groupby("customer_id").mean()
df_gen_sep = df[df["Months"] == "September"].groupby("gender").mean()

mean_f_bal_sep = df_gen_sep["balance"].iloc[0]
mean_m_bal_sep = df_gen_sep["balance"].iloc[1]
n_points = len(df_cus_sep["age"])

plt.figure()
plt.scatter(df_cus_sep["age"], df_cus_sep["balance"], c="black", label="Balance")
plt.plot(df_cus_sep["age"], np.linspace(mean_f_bal_sep, mean_f_bal_sep, n_points), c="r", label="Mean female balance")
plt.plot(df_cus_sep["age"], np.linspace(mean_m_bal_sep, mean_m_bal_sep, n_points), c="b", label="Mean male balance")
plt.title("ANZ Customer Balance vs. Age for September")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:


mean_f_amt_sep = df_gen_sep["amount"].iloc[0]
mean_m_amt_sep = df_gen_sep["amount"].iloc[1]

plt.scatter(df_cus_sep["age"], df_cus_sep["amount"], c="black", label="Amount")
plt.plot(df_cus_sep["age"], np.linspace(mean_f_amt_sep, mean_f_amt_sep, n_points), c="r", label="Mean female amount")
plt.plot(df_cus_sep["age"], np.linspace(mean_m_amt_sep, mean_m_amt_sep, n_points), c="b", label="Mean male amount")
plt.title("ANZ Customer Mean Payment Amount vs. Age for September")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:


df_cus_oct = df[df["Months"] == "October"].groupby("customer_id").mean()
df_gen_oct = df[df["Months"] == "October"].groupby("gender").mean()

mean_f_bal_oct = df_gen_oct["balance"].iloc[0]
mean_m_bal_oct = df_gen_oct["balance"].iloc[1]
n_points = len(df_cus_oct["age"])

plt.figure()
plt.scatter(df_cus_oct["age"], df_cus_oct["balance"], c="black", label="Balance")
plt.plot(df_cus_oct["age"], np.linspace(mean_f_bal_oct, mean_f_bal_oct, n_points), c="r", label="Mean female balance")
plt.plot(df_cus_oct["age"], np.linspace(mean_m_bal_oct, mean_m_bal_oct, n_points), c="b", label="Mean male balance")
plt.title("ANZ Customer Balance vs. Age for October")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:


mean_f_amt_oct = df_gen_oct["amount"].iloc[0]
mean_m_amt_oct = df_gen_oct["amount"].iloc[1]

plt.scatter(df_cus_oct["age"], df_cus_oct["amount"], c="black", label="Amount")
plt.plot(df_cus_oct["age"], np.linspace(mean_f_amt_oct, mean_f_amt_oct, n_points), c="r", label="Mean female amount")
plt.plot(df_cus_oct["age"], np.linspace(mean_m_amt_oct, mean_m_amt_oct, n_points), c="b", label="Mean male amount")
plt.title("ANZ Customer Mean Payment Amount vs. Age for October")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





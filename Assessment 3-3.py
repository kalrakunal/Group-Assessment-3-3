#import pandas to read the file
import pandas as pd

# Read the CSV file
order =  pd.read_csv("./orders.csv")

#Check the frequency of customers and convert to a dataframe to get most frequent names
df = pd.DataFrame(order["customer_name"].value_counts())
df["Customer_names"] = df.index
df = df.rename(columns = {"customer_name": "frequncy"})
frequent_customers = list(df["Customer_names"])


#Get he name of top most three frequent buyers
print(f"Most three frequent buyers are: 1-{frequent_customers[0]}, 2-{frequent_customers[1]}, and 3-{frequent_customers[2]}.")
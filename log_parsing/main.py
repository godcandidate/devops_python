"""
    1 : Reading the file
    2 : extract ip address and error and success logs
    3 : save the output in csv/excel file
    4 : send email
"""
from pathlib import Path
import re
import pandas as pd
import pprint

# Get file path
file_path = Path(__file__).parent / "service_logs.log"
log_file = open(file_path, "r")


# pattern for ip_address
pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")

ip_addr_list = []
failed_list = []
success_list = []

for log in log_file:
    # ip address
    ip_address = re.search(pattern, log)
    ip_addr_list.append(ip_address.group())

    # get failed and success codes
    log_list = log.split(" ")
    failed_list.append(int(log_list[-1]))
    success_list.append(int(log_list[-4]))

df = pd.DataFrame(columns=['IP Address', 'Success','Failed'])
df['IP Address'] = ip_addr_list
df['Success'] = success_list
df['Failed'] = failed_list

df.to_csv("output.csv",index=False)


pprint.pprint(df)
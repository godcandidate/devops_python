from pathlib import Path
import re
import pandas as pd
import pprint

# Get file path
file_path = Path(__file__).parent / "service_logs.log"

# Regex pattern for IP address
pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")

log_data = []

# Read file
with open(file_path, "r") as log_file:
    for log in log_file:
        
        # Extract IP address
        ip_match = re.search(pattern, log)
        if ip_match:
            ip_address = ip_match.group()

            # Extract success or failure
            log_parts = log.split(" ")
            success = int(log_parts[-4])
            failed = int(log_parts[-1])

            # Add the processed data as a dictionary to the list
            log_data.append({
                "IP Address": ip_address,
                "Success": success,
                "Failed": failed
            })

# Convert log data into a DataFrame
df = pd.DataFrame(log_data)

# Save the DataFrame to CSV
df.to_csv("output.csv", index=False)

# Optionally: Preview the data in a human-readable format
pprint.pprint(df)


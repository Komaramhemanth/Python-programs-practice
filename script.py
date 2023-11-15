from datetime import datetime
import pytz  # For handling time zones

# Get the current date and time
current_datetime = datetime.now()

# Convert to IST (Indian Standard Time)
ist_timezone = pytz.timezone('Asia/Kolkata')
current_datetime_ist = current_datetime.astimezone(ist_timezone)

# Format the date as per the specified format
formatted_date = current_datetime_ist.strftime("%a %b %d %H:%M:%S %Z %Y")

# Print the formatted date
print("Current Date:", formatted_date)

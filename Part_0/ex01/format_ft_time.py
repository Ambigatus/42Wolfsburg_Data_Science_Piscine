import time

# Getting current time in seconds since January 1, 1970
starting_time = time.time()

# Formatting time
formatted_time = f"{starting_time:,.4f} or {starting_time:.2e} in scientific notation"

# 4f - it's format "floating point number", cut the number up to four digits
# 2e - it's scientific notation with two digits after the decimal point

# Current time, exactly in this moment
current_time = time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_time}")
print(current_time)

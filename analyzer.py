from functions import *

# UNCOMMENT DEPENDING ON DATABASE YOU'D LIKE TO SEE
#database = 'first_quarter'
#database = 'second_quarter'
#database = 'halftime'
#database = 'third_quarter'
#database = 'fourth_quarter'
database = 'superbowl'

# You can comment or uncomment based on what data you'd like in your Excel file
setup_workbook(database)
unique_users(database)
flairs(database)
gilded(database)
comments(database)
comments_per_minute(database)
print("Done!")

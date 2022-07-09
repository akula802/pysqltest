import mysql.connector 


# Connect to the server
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'def bobby_tables(INP):',
    database = 'testdb',
    #autocommit = 'true',
    )


# Create a cursor - first thing you need, pretty much always
my_cursor = mydb.cursor(buffered=True)


###############################
###### Create a database ######
###############################

#my_cursor.execute("CREATE DATABASE testdb;")

# Run a 'show databases' command - this just shows the command written out
#my_cursor.execute("SHOW DATABASES")

# For loop to actually print the databases
#For db in my_cursor:
#    print(db)


############################
###### Create a table ######
############################

# Create the table
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INT(10), user_id INTEGER AUTO_INCREMENT PRIMARY key)")

# Add some rows with data, one at a time
#my_cursor.execute("INSERT INTO users (name, email, age) VALUES ('Muki', 'muki@gridnorth.tech', 4);")
#my_cursor.execute("INSERT INTO users (name, email, age) VALUES ('Brian', 'brian@gridnorth.tech', 38);")

# Show the table(s)
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#    print(table)


#############################################
###### Create multiple records at once ######
#############################################

# Multiline comment sort of, per: https://www.w3schools.com/python/python_comments.asp
"""
sql_stuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [
    ('Melissa', 'melissa@email.net', 36),
    ('Lunchbox', 'lunchbox@catsemail.com', 8),
    ('Rissypoo', 'sheis@psycho.path', 5),
    ('theChicken', 'eatme@dinner.com', 3)
]

# Loop and write - don't need to loop if you use 'executemany'
for record in records:
    my_cursor.execute(sql_stuff, record)

# Execute many
my_cursor.executemany(sql_stuff, record)

""" # End 'multiline comment'


#####################################
###### Commit changes and show ######
#####################################

# Commit the changes
#mydb.commit()

# Show the table data
#my_cursor.execute("SELECT * FROM users")
#for user in my_cursor:
#    print(user)



##################################################################
###### Select and display results better (but still shitty) ######
##################################################################

# I used the 'texttable' module in the past to display DB query results better

my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()

# Column headers
print("NAME\t\tEMAIL\t\t\t\tAGE")
print("----\t\t-----\t\t\t\t---")

# Loop results
for row in result:
    if len(row[0]) <= 7:
        print("{}\t\t{}\t\t{}".format(row[0], row[1], row[2]))
    else:
        print("{}\t{}\t\t{}".format(row[0], row[1], row[2]))





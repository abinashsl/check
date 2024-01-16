import boto3

# Set up AWS credentials
aws_access_key = 'AKIAQOWNALIXFNUC7BJV'
aws_secret_key = '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'

# Create an RDS client
rds = boto3.client('rds', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

# Specify RDS instance details
db_instance_identifier = 'database-1'

# Describe RDS instance details
response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)

# Print information about the RDS instance
db_instance = response['DBInstances'][0]
print(f"DB Instance Identifier: {db_instance['DBInstanceIdentifier']}")
print(f"DB Engine: {db_instance['Engine']}")
print(f"DB Endpoint: {db_instance['Endpoint']['Address']}:{db_instance['Endpoint']['Port']}")
print("RDS Service Connected")

import mysql.connector

# Replace 'your_db_user' and 'your_db_password' with your actual database credentials
db_user = 'admin'
db_password = '1Abinash'
db_name = 'STUDENT'

# Replace 'your_host', 'your_port' with your RDS instance details
db_host = db_instance['Endpoint']['Address']
db_port = db_instance['Endpoint']['Port']

# Connect to the database
conn = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)

print("Connected to Database")

# Create a cursor
cursor = conn.cursor()

def search(usern,pwd):
    # Example query
    cursor.execute(f"SELECT * from USER_CRED where Username like ('{usern}');")

    # Fetch and print result
    result = cursor.fetchall()

    if bool(result)==True:
        if pwd==result[0][1]:
            print("Logged IN")
            return "Logged IN"
        else:
            print("Check Password")
            return "Check Password"
    else:
        print('Invalid User')
        return 'Invalid User'
    # Perform other database operations as needed

    # Close cursor and connection
    cursor.close()
    conn.close()
users = {
    'Johnathan': {   # Username as the key
        'first_name': 'johnathan',
        'last_name': 'ward',
        'location': 'New York',
        'occupation': 'Programming'
    },
    
}

# Loop through the outer dictionary
# 'username' holds the key, 'user_info' holds the inner dictionary
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
firstName = user_info['first_name']
lastName = user_info['last_name']
loc = user_info['location']
job = user_info['occupation']

print(f"Hey, my name is {firstName.title()} {lastName.title()}, I live in {loc} and I am in {job.lower()}.")
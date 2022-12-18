import requests
import pygithub
import matplotlib.pyplot as plt

# Replace TOKEN with your personal access token
headers = {'Authorization': 'Token PAT'}

# Make a GET request to the GitHub API to retrieve your activity data
response = requests.get('https://api.github.com/users/swastikgorai/events', headers=headers)

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()

    # Filter the data to only include push events (commits)
    push_events = [event for event in data if event['type'] == 'PushEvent']

    # Extract the dates and number of commits for each push event
    dates = [event['created_at'] for event in push_events]
    num_commits = [len(event['payload']['commits']) for event in push_events]

    # Plot the data using matplotlib
    plt.plot(dates, num_commits)
    plt.xlabel('Date')
    plt.ylabel('Number of commits')

    # Save the plot to a file
    plt.savefig('activity.png')
else:
    print('Something went wrong')

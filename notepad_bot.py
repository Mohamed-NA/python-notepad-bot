import requests
import pyautogui
import time
import os
import subprocess

# Configuration

# API settings for fetching data from a public API
# Using ?_limit=10 to limit the number of posts fetched to the required number
API_URL = "https://jsonplaceholder.typicode.com/posts?_limit=10"
# data file to store fetched data
DATA_FILE = "data.txt"

#Path to the desktop and project folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
project_dir = os.path.join(desktop_path, "tjm-project")

# Function to fetch data from the API and save it to a file

def main():
    """
    main function to run the automation bot
    1.Create a project directory on the desktop if it doesn't exist
    2.Fetch data from the API
    3.Automation loop to open notepad, write data, and save the file for every post
    4.Close notepad after saving the file
    """
    
    print("Starting the automation bot...")
    
    # 1.Create project directory if it doesn't exist
    try:
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            print(f"Created project directory at {project_dir}")
        else:
            print(f"Project directory already exists at {project_dir}")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return # Stop execution if we can't create the directory
        
    # 2.Fetch data from the API
    try:
        posts = requests.get(API_URL)
        posts.raise_for_status()  # Raise an error for HTTP errors
        posts = posts.json()
        print(f"{len(posts)} posts fetched from the API.")
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return # Stop execution if we can't fetch data
    
    # 3.Automation loop for each post
    for post in posts:
        post_id = post['id']
        title = post['title']
        body = post['body']
        
        file_name = f"post {post_id}.txt"
        full_path = os.path.join(project_dir, file_name)
        
        # If file already exists, skip to next post
        if os.path.exists(full_path):
            print(f"Skipping Post ID: {post_id}. File '{file_name}' already exists.")
            continue
        
        # Preparing the content to write
        content_to_write = f"Title: {title}\n\nPost:\n{body}"
        
        print(f"Processing post {post_id} -> {file_name}")
        
        try:
            # Open Notepad
            print("Attempting to open Notepad...")
            subprocess.Popen(['notepad.exe'])
            time.sleep(2)  # Wait for Notepad to open
            
            # Write title and body to Notepad
            pyautogui.write(content_to_write, interval=0.01)
            time.sleep(1)  # Wait for typing to finish
            
            # Save the file
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)  # Wait for Save dialog to open
            
            # Type the full path and save
            pyautogui.write(full_path, interval=0.05)
            time.sleep(1)  # Wait for typing to finish
            pyautogui.press('enter')
            time.sleep(1)  # Wait for file to save
            
            # Close Notepad
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)  # Wait for Notepad to close

            print(f"Saved {file_name} successfully using pyautogui(GUI Automation).")
        except Exception as e:
            print(f"(!) GUI Automation failed for Post ID {post_id}: {e}")
            print("--> Executing Fallback: Direct file write.")
            # Try to close any lingering Notepad window to prevent issues
            pyautogui.hotkey('alt', 'f4')
            # Fallback
            try:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content_to_write)
                print(f"Saved {file_name} successfully using direct file write.")
            except OSError as file_error:
                print(f"Error writing file {file_name}: {file_error}")  
                continue  # Proceed to the next post if there's an error

    print("\nAutomation task completed successfully!")
    
if __name__ == "__main__":
    main()
import urllib.parse
import os

def decode_url(url):
    # Use the unquote function to decode the URL
    return urllib.parse.unquote(url)

# Open the file outside of the loop to avoid opening and closing it multiple times
with open("data.txt", "w") as file:
    while True:
        # Ask the user to input an encoded URL
        encoded_url = input("Enter the encoded Data: ")
        
        # Check if the input is empty
        if not encoded_url:
            break
        
        # Decode the URL
        decoded_url = decode_url(encoded_url)
        
        # Write the decoded URL to the file and include a newline for each entry
        file.write(decoded_url + "\n")
        print("Successfully data added to data.txt")

print("Finished. Data adding ")
os.system('clear')
os.system('python3 major.py')


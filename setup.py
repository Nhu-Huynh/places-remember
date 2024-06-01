import os

# Check if .env file already exists
if os.path.exists(".env"):
    print(".env file already exists. Please ensure it contains the correct values.")
else:
    # Copy the example .env file to .env
    with open(".env.example", "r") as example_file:
        env_content = example_file.read()

    google_client_id = input("Enter your Google Client ID: ")
    google_client_secret = input("Enter your Google Client Secret: ")

    # Replace placeholder values in .env file content
    env_content = env_content.replace("your_google_client_id_here", google_client_id)
    env_content = env_content.replace(
        "your_google_client_secret_here", google_client_secret
    )

    # Write the content to .env file
    with open(".env", "w") as env_file:
        env_file.write(env_content)

    print(".env file has been created and configured.")

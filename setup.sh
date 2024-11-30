#!/bin/bash

# Update package lists
sudo apt-get update

# Install necessary packages
sudo apt-get install -y libsqlite3-dev sqlite3

# Install Python dependencies
pip install flask python-dotenv pysqlite3

echo "Setup complete! You can now run 'flask run' to start the server."
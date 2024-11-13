# test-backend-kosmos-juan-diaz
Test backend Kosmos Juan Diaz


## Description
This project implements a TCP server and client in Python that communicate with each other on localhost using port 5000.

To run the TCP server and client in Python you will need to have Python installed on your machine. Here are the steps to make sure you have everything you need:


1. **Install Python**

Windows:

1. Go to the official Python [site](https://www.python.org/downloads/).
Download the installer for Windows.
During installation, make sure to check the "Add Python to PATH" option.

macOS:

1. You can install Python using Homebrew. If you don't have Homebrew, install it from [here](https://brew.sh/).

2. Then, open the terminal and run:

     brew install python

Linux:

On most distributions, Python is already installed. If not, you can install it using your distribution's package manager. For example, in Ubuntu:

    sudo apt update
    sudo apt install python3

2. **Verify Installation**

After installing Python, verify that it is installed correctly by opening a terminal (or command prompt on Windows) and running:

    python --version

    or 

    python3 --version


3. **Install a Virtual Environment**

If you want to work in a virtual environment, you can install virtualenv:

    pip install virtualenv

Then, you can create a virtual environment:
    
    virtualenv venv

And activate it:

Windows:
    venv\Scripts\activate

macOS/Linux:
    source venv/bin/activate


4. **Install the dependencies:**

   Make sure the virtual environment is enabled and then run:

   ```bash
   pip install -r requirements.txt


#
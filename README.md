# LM_Studio_Local_Server
This will show you how to run a local server with LM Studio.  You will not need an API key.  This will allow you to run Hugging Face models outside of the chat interface on your PC without an internet connection.  I have added multiple .py files.  There are 3 .py files in total.  Each will allow you to start the local server.  The 2 files that offer the most functionality are the llm.py file and the lmst_ext.py file.  Choose any 1 file to run.  
## Getting Started
Follow these steps to set up and run the project on your local machine.
### Prerequisites
    - Anaconda (https://www.anaconda.com/)

    - LM Studio (https://lmstudio.ai/)

### Setting Up Your Python Environment
    1. Install Anaconda: Download and install Anaconda from the official website. Follow the installation instructions for your operating system.
    
    2. Create a New Conda Environment (recommended):
        conda create -n myenv python=3.11

Replace "myenv" with your preferred environment name.

    3. Activate the Environment:
        conda activate myenv

### Clone the repository
        git clone https://github.com/VideotronicMaker/LM_Studio_Local_Server.git
    
    4. Install Required Packages:
    
Navigate to the project directory and install the required packages using the provided requirements.txt file:
        pip install -r requirements.txt

### Running the Project
    LLM Python Script (llm.py): This is the main script for running the language model.

    System Messages File (system_message.txt): This file contains custom instructions or system messages for the model's behavior.

    To run the script, use the following command in your terminal or command prompt:

        python llm.py

    Make sure system_message.txt is in the same directory as llm.py, or update the script to point to its location.


## Need More Help?
    If you're unfamiliar with using the command line for tasks like navigating directories, creating folders, or managing Python environments, tools like ChatGPT or Gemini Pro can provide step-by-step guidance on these processes.


# LM_Studio_Local_Server
This will show you how to run a local server on LM Studio.  You will not need an API key.  This will allow you to run Hugging Face models on your PC without an internet connection.
## Getting Started
Follow these steps to set up and run the project on your local machine.
### Prerequisites
-Anaconda (https://www.anaconda.com/)

-LM Studio (https://lmstudio.ai/)

### Setting Up Your Python Environment
    1. Install Anaconda: Download and install Anaconda from the official website. Follow the installation instructions for your operating system.
    
    2. Create a New Conda Environment (recommended):
        `conda create -n myenv python=3.11`

Replace "myenv" with your preferred environment name.

    3. Activate the Environment:
        `conda activate myenv`
    
    4. Install Required Packages:
    
Navigate to the project directory and install the required packages using the provided requirements.txt file:

        `pip install -r requirements.txt`

## Clone the repository
        'git clone https://github.com/VideotronicMaker/LM_Studio_Local_Server.git'
'

### Running the Project
    LLM Python Script (llm.py): This is the main script for running the language model.

    System Messages File (system_message.txt): This file contains custom instructions or system messages for the model's behavior.

    To run the script, use the following command in your terminal or command prompt:

        `python llm.py`

    Make sure system_message.txt is in the same directory as llm.py, or update the script to point to its location.


    
```python
# Example Python code
def example_function():
    return "Hello, World!"
```

```
```javascript
// Example JavaScript code
function exampleFunction() {
    return "Hello, World!";
}
```

```



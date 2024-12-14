## Setup
Here is the steps to setup the application on local device

### 1. Clone the repository
First, clone the repository to your local machine:
```
git clone https://github.com/rikzakurnia/tbi-tk4
cd tbi-tk4
```
### 2. Create a Virtual Environment
To isolate the project dependencies, create a virtual environment:
```
python -m venv env
```

### 3. Activate the Virtual Environment
Activate the virtual environment based on your operating system:

**Windows**:
```
.\env\Scripts\activate
```
**Linux/Unix, e.g. Ubuntu, macOS**:
```
source env/bin/activate
```

### 4. Install Dependencies
Once the virtual environment is activated, install the required Python packages using pip:
```
pip install -r requirements.txt
```
This will install all dependencies listed in the requirements.txt file.

### 5. Adding New Dependencies
If you add new dependencies to the project, you can update the requirements.txt file by running:
```
pip freeze > requirements.txt
```

### 6. Run the Application
To start the Flask development server, run the following command:
```
python run.py
```
This will start the application, and it should be accessible at http://127.0.0.1:8080/ in your browser.

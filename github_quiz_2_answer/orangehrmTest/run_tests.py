import subprocess
import sys
from pathlib import Path

def setup_environment():
    '''
        This whole test is built based on pytest and pytest-bdd (the Python version of Cucumber)
        This function is for setting up test environment
        environment includes:
        1. create necessary directories
        2. install dependencies from requirements.txt
    '''
    print("Setting up test environment...")
    # create necessary directories
    Path("reports").mkdir(exist_ok=True)
    Path("reports/screenshots").mkdir(exist_ok=True)
    Path("features").mkdir(exist_ok=True)
    # install dependencies
    try:
        # install dependencies from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

def run_pytest_tests():
    '''
        run pytest tests
    '''
    try:
        # make command to run pytest tests according to the pytest requirements
        # 1. test_claims_bdd.py - run this file only
        # 2. -v verbose mode
        # 3. --html= - generate html report
        # 4. self-contained - independent html report
        # 5. -s - capture stdout/stderr
        cmd = [
            sys.executable, "-m", "pytest", # make sure to use the correct python interpreter
            "test_claims_bdd.py",
            "-v",
            "--html=reports/pytest_report.html",
            "--self-contained-html",
            "-s"]
        # run pytest tests
        result = subprocess.run(cmd)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

def main():
    if not setup_environment():
        return 1
    print("Running pytest-bdd tests...")
    success = run_pytest_tests()
    
    if success:
        print("\n" + "="*50)
        print("Tests completed successfully!")
        print("Check the report at: reports/pytest_report.html")
        print("="*50)
        return 0
    else:
        print("\n" + "="*50)
        print("Some tests failed!")
        print("Check the report at: reports/pytest_report.html for details")
        print("="*50)
        return 1

if __name__ == "__main__":
    # run main function and exit with return code
    sys.exit(main())
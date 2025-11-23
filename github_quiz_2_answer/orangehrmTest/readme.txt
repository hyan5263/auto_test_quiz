project: 		github_quiz_2_answer

project env:	Windows 11
			python 3.14
			chromdriver 142.0.7444.175
			msedgedriver 142.0.3595.80
			selenium

project structure: Project/
			├──features<folder>
				├──assign_claims.feature -- features file (Gherkin)
			├── conftest.py -- config pytest
			├── test_claims_bdd.py -- BDD tests
			├── pages.py --create page objects
			├── utils.py -- create tools
			├── requirements.txt -- required dependencies (auto install)
			└── run_tests.py -- entrance of the test 


how to run: 	1. save file name of the selenium driver to drivernm.ini (chromedriver.exe or msedgedriver.exe)
			2. fetch all project files to local folder
			3. go to the local folder 
			4. run command "python run_tests.py"
			5. need to re-config drivernm.ini for different browser

Test passed 3/3 round in my test environment.



### Answer for https://github.com/atquiz/auto_test_quiz
All the code is developed based on the Python environment. If a Java is mandatory, I will rewrite it in Java.

---
project: github_quiz_1_answer

project env: 
- Windows 11
- python 3.14
- chromdriver 142.0.7444.175
- msedgedriver 142.0.3595.80
							
- selenium
							
project structure: 	

-- Project/

----| screenshots (folder)-- save screenshots
   
----| chromedriver.exe
				            
----| msedgedriver.exe

----| github_quiz_1_answer.py -- entrance of the test 
			            	
----| github_quiz_1_test.log -- the test results and logs

how to run: 

1. fetch all project files to local folder
2. go to the local folder 
3. run command "python github_quiz_1_answer.py"
4. test will finish 2 rounds tests for Chrome and Edge

---
project: 		        github_quiz_2_answer

project env:

- Windows 11
- python 3.14
- chromdriver 142.0.7444.175
- msedgedriver 142.0.3595.80
- selenium

project structure:  
-- Project/

----| features(folder)

--------| assign_claims.feature -- features file (Gherkin)

----| conftest.py -- config pytest

----| test_claims_bdd.py -- BDD tests

----| pages.py --create page objects

----| utils.py -- create tools

----| requirements.txt -- required dependencies (auto install)

----| run_tests.py -- entrance of the test 


how to run: 

1. save file name of the selenium driver to drivernm.ini (chromedriver.exe or msedgedriver.exe)
2. fetch all project files to local folder
3. go to the local folder
4. run command "python run_tests.py"
5. need to re-config drivernm.ini for different browser

---
---
# Open Automation Quiz
---

## 0. 任务要求

> **特别注意**：请于完成后，将项目源码更新至候选者您本人的Github，在您项目的**Settings**页面，例如本项目为此[链接](https://github.com/atquiz/auto_test_quiz) ，将您的项目设置为**Private Repository**以免借阅, 并于**Manage access**邀请**nnnlyy**作为协作者(collaborator)后，在**nnnlyy**的Repo发起[issue](https://github.com/atquiz/auto_test_quiz/issues)声明您的项目链接，并最终反馈给HR/Vendor/猎头等渠道

### 基本要求

* 请**Fork**本项目到您自己的Github账号下 (本项目已关联Github Actions, 会自动编译检测Fork项目提交质量)
* 以下内容均基于**Java**进行考察，并同时涉及到了Git, Maven, Selenium, Cucumber 和 Appium等技术
* 第一题Selenium和第二题Cucumber必做，第三题Appium视为加分项可以选做
* 网页端内容需同时对[Chrome](https://www.google.cn/intl/zh-CN/chrome/)和[Microsoft Edge (IE Mode)](https://www.microsoft.com/zh-cn/edge/business/ie-mode)两种浏览器进行实现
* 手机端内容可以基于Android或iOS平台二选一
* 若担心环境问题，可以将运行结果的截图添加至项目资源目录内，并声明截图路径
* 允许锦上添花，额外增加体现个人情况的功能，但是无视题目要求自行发挥的，直接判定失败

### 加分项

希望，我们可以遇到这样的您

* 认真理解题目的要求，若有不明确的地方，可以直接给**nnnlyy**提[issue](https://github.com/atquiz/auto_test_quiz/issues)沟通 或 通过HR/Vendor/猎头等反馈
* 思路清晰，代码规范，尽量完成了更多的任务，针对**项目结构**和**代码质量**进行了完善
* 尽量提交可以直接运行的项目，至少也应该是可以通过**Maven**构建的
* 提交一个规范的Java项目，符合标准的项目结构，根据需求引入必要的依赖并解决冲突，创建必要的文件和配置
* 项目不依赖于特定的IDE，可以通过命令行或者接口的形式被调用，以便于测试平台或框架级别的引用

> 以下任务内容均来源于基本的日常需求，请您反馈项目前认真思考，是否适应并胜任，比这些任务更加复杂的日常工作

### 校验方式

项目根目录执行以下命令后，查看即时生成的测试结果及报告

> mvn clean test

---

## 1. 基础验证(Selenium)

请使用[Selenium](https://github.com/SeleniumHQ/selenium)打开[测试网站](https://practicetestautomation.com/practice/)

1. 点击**Test Login Page**，完成页面下方case
2. 返回
3. 点击**Test Exceptions**，完成页面下方case

请注意，每一步操作请附带**步骤说明**和**截图**，生成文档

## 2. 表单验证(Cucumber)
请基于[Cucumber](https://cucumber.io/)，以[BDD](https://cucumber.io/docs/bdd/)的形式，自行实现所需的[Feature](https://cucumber.io/docs/gherkin/reference/#feature)和[Gherkin](https://cucumber.io/docs/gherkin/)，用于以下操作
打开[测试网站](https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index)，在左边栏点击**Claims**进入页面

1. 点击**Employee Claims**, 添加一条**Assign Claims**记录：
   **Create Claim Request**：
   
   Employee Name：Amelia  Brown(如果搜索不到，可以自己找一条有效数据)

   Event：Travel allowances

   Currency：Euro
   截图
3. 点击**Create**后验证成功提示信息, 截图
4. 跳转至**Assign Claim**详情页，验证与前一步数据一致，截图
5. 添加**Expenses**，选择**Expense Type**和**Date**，填写**amount**，点击**Submit**，验证成功提示信息，截图
6. 检查数据与填写数据一致，点击**Back**返回，截图
7. 验证Record中存在刚才的提交记录，截图

测试完成后，应生成相应的[HTML]测试报告，报告包括截图，操作步骤，状态等，如果case失败，附有失败截图和失败日志

## 3. 手机APP(Appium)

请基于 [Appium](http://appium.io/)  完成任意一款APP的自动化测试，请附带可下载的测试APP样例链接。或者直接基于本模板项目给定样例APP [app-debug-1.0.0.apk] 完成测试。
测试内容需包括以下操作

* 点击按钮
* 提取资源文本
* 断言不同页面的资源

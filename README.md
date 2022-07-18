# **Extra Automation Project By Luka Kekenadze**
___
* go to the [Extra Website](https://extra.ge/). 
#**Basic installation Commands**
* generate requirements.txt file **pip3 freeze > requirements.txt**
* you should install **requirements.txt** file to run tests
* 
___

#**Run Test**
to run tests use ```pytest``` command in cli
after test is complete,allure report starts automatically in the default browser.if allure reports fails opening,run:

```
allure serve reports/allure/
```

run pytest
```
pytest tests/Test_extra_main_page.py
```
collect only tests
````
pytest --collect-only tests/Test_extra_main_page.py
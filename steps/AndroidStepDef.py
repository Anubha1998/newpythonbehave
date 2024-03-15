import os
import requests
from appium import webdriver
from behave import given
import appConfig as appConf

# Modify the given step to start the automation test
@given("Start the android app automation test")
def startAndroidAppAutomationTest(context):
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    # Desired capabilities with LambdaTest username and access key
    desired_caps = {
        "username": username,
        "accessKey": accesskey,
        
    "deviceName":"Galaxy S20",
    "w3c": True,
    "platformName":"Android",
    "platformVersion":"10",
    "build":"Python Behave - Android",
    "name":"Sample Test Android",
    "isRealMobile":True,
    "visual":True,
    "video":True,
    "app":"lt://APP1016053741710416415042354",
    "enableImageInjection": True
    
        # Add other desired capabilities as needed
    }

    # Add browser capabilities specific to LambdaTest Selenium Grid
    desired_caps["browserName"] = "chrome"  # Example: Use Chrome browser
    desired_caps["version"] = "latest"  # Example: Latest version of Chrome

    # Call LambdaTest media upload API to upload image and get media URL
    url = "https://mobile-mgm.lambdatest.com/mfs/v1.0/media/upload"
    payload = {'type': 'image', 'custom_id': 'SampleImage'}
    files = [('media_file', ('testImage.png', open('/workspace/newpythonbehave/testImage.png', 'rb'), 'image/png'))]
    headers = {'Authorization': 'Basic cHJha2hhcmdhaGxvdDpLU0Z5WGlWb1BrUTl4V1NjelZsUjBCZUw4WjZtVTRvSHZKV1pYSGdUb0Q2aEVscnVXTg=='}

    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        response.raise_for_status()  # Check if the request was successful

        # Extract media URL from the API response
        media_url = response.json()["media_url"]
        print("Media URL:", media_url)

        # Add the media URL to desired capabilities
        desired_caps["mediaUrl"] = media_url

        # Start the WebDriver session with desired capabilities
        driver = webdriver.Remote(
            command_executor=f"https://{username}:{accesskey}@mobile-hub.lambdatest.com/wd/hub",
            desired_capabilities=desired_caps
        )

        try:
            # Your test steps here
            print("WebDriver session started successfully")
            pass

        except Exception as e:
            print("Error in test steps:", e)

        finally:
            # Quit the WebDriver session
            driver.quit()
            print("WebDriver session terminated")

    except requests.RequestException as ex:
        print("Error during media upload:", ex)


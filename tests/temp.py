
import os
import json
import subprocess

# -------------------------------
# Fixture: Read the config file
# -------------------------------

#@pytest.fixture 
def chrome_config():
    CHROME_DRIVER_BASE_URL="https://chromedriver.storage.googleapis.com"
    #https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip

    # Read the config file
    proj_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    with open(os.path.join(proj_dir, 'config.json')) as config_file:
        config = json.load(config_file)
    # Verify webdriver config
    assert 'webdriver' in config
    assert 'name' in config['webdriver']
    assert 'browserName' in config['webdriver']
    assert 'version' in config['webdriver']
    assert 'platform' in config['webdriver']

    drivercfg = config['webdriver']
    driver_folder = "/tmp/{}".format(drivercfg['name'])
    driver_file = "{}_{}".format(drivercfg['name'], drivercfg['platform'])
    driver_url = "{}/{}/{}.zip".format(CHROME_DRIVER_BASE_URL, drivercfg['version'], driver_file)
    driver_pathzip = "{}/{}.zip".format(driver_folder, driver_file)
    driver_path = "{}/{}".format(driver_folder, drivercfg['name'])
    driver_pathver = "{}/{}_{}".format(driver_folder, drivercfg['name'], drivercfg['version'])
    os.environ['PATH'] += ':'+driver_folder
    if os.path.exists(driver_folder) == False: 
        os.mkdir(driver_folder)
    if os.path.exists(driver_pathver) == False:
        p=subprocess.Popen("curl {} -o {}".format(driver_url, driver_pathzip, driver_pathzip, driver_pathzip), shell=True)
        p.wait()
        p=subprocess.Popen("unzip -o {} -d {}".format(driver_pathzip, driver_folder), shell=True)
        p.wait()
        #p=subprocess.Popen("mv {} {}".format(driver_path, driver_pathver), shell=True)
        #p.wait()

if __name__ == '__main__':
    chrome_config()
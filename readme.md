<div align="center">

# pip-cli 

[![Pylint](https://github.com/4cecoder/pip-cli/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/4cecoder/pip-cli/actions/workflows/pylint.yml)
[![Python application](https://github.com/4cecoder/pip-cli/actions/workflows/python-app.yml/badge.svg)](https://github.com/4cecoder/pip-cli/actions/workflows/python-app.yml)


<video src="https://user-images.githubusercontent.com/88108711/203481427-eaaa4480-966e-462e-a2dd-8125382319ab.mp4">
  
<video/>

</div>
  
# Run 
  `git clone https://github.com/carrotshniper21/pip-cli.git`
  
  `cd pip-cli`
  
  `python pip_cli.py`

# Pre-Requisites

## Mozilla's Geckodriver
### Linux Install
```shell
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/path-to-extracted-file/.
```
## Chromium Chromedriver
### Linux Install
```sudo apt-get install unzip;
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip && sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;
export PATH=$PATH:/path/to/driver/chrome-driver/.
```
### Mac Install
```wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip
unzip chromedriver_mac32.zip
mkdir -p $HOME/bin
mv chromedriver $HOME/bin
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
```
  
### OSX
`brew install geckodriver`

### Windows
`Not Supported Yet`

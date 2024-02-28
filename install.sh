#Update and upgrade
sudo apt update
sudo apt upgrade
#install venv
pip3 install virtualenv
#creating and activating venv
virtualenv venv
source venv/bin/activate
#installing required pip packages
pip3 install selenium pandas
#Everything related to geckodriver
sudo apt install wget -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
#running the scrape.py file
python3 scrape.py
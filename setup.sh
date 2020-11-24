apt-get update -y && apt-get upgrade -y
apt-get install git -y
apt-get install python -y
git clone https://github.com/zettamus/facebook-cracker
cd facebook-cracker
pip install -r requirements.txt
clear
echo All dependencies installed

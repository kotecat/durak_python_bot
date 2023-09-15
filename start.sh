git pull

if ! [ -f /venv/ ]; then
    echo -e "\e[32Red CREATE VENV"
    python3 -m pip install virtualenv
    echo "creating venv dir..."
    python3 -m venv venv
    echo "install all requirements..."
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
fi

echo -e "\e[32Green running..."

source venv/bin/activate

python3 durak/bot.py
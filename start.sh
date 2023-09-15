git pull

if ! [ -d /venv ]; then
    echo "CREATE VENV"
    python3 -m pip install virtualenv
    echo "creating venv dir..."
    python3 -m venv venv
    echo "install all requirements..."
    . venv/bin/activate
    python3 -m pip install -r requirements.txt
fi

echo "running..."

. venv/bin/activate

python3 durak/bot.py
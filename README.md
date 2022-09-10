# Improvisation

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/YohannL/Improvisation/blob/main/ImproSablier/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment.

```bash
git clone https://github.com/YohannL/Improvisation  # clone
cd Improvisation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # install
```

</details>

<details open>
<summary>Using the app</summary>

First launch the API, then the webapp. Use the `--admin` and `--monitor` flags to lauch the webapp in these privileged modes.

```bash
# Launch API
python main.py

# Launch the webapp in public mode 
python webapp.py

# Launch the webapp in admin mode
python webapp.py --admin

# Launch the webapp in monitor mode
python webapp.py --monitor
```

</details>

<details open>
<summary>:construction: Testing :construction:</summary>

Under construction 

```bash
# Launch tests
python -m pytest
```

</details>
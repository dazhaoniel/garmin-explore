# garmin-explore

Looking at some garmin .FIT data for fun


## Development

Start Jupyter Notebook
```
jupyter notebook
```

Run script to convert .gpx (Strava) and .fit (Garmin) activties to dataframe
```python
# Start python virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# generate requirement file
pip freeze > requirements.txt

# Leave virtual environment
deactivate

# Run script
python main.py
```
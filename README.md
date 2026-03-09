# garmin-explore

Looking at some garmin .FIT data for fun


## Development

Start Jupyter Notebook
```
jupyter notebook
```

Run script to convert .FIT.gz (Garmin) activties to dataframe then export to csv for my husband
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

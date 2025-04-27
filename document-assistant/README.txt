# Project to ask Q&A using local documents

## To activate the virtual env from ".venv"

```
source .venv/bin/activate
```

# Login to Hugging Face / confirm the login to access Gated repository
```
huggingface-cli login
huggingface-cli whoami
```

## To test
```
pytest -s

pytest -s test_data_load.py     ### to test document load

pytest -s test_Q_and_A.py       ### to test full Question-Answer system
```

## Streamlit app
```
streamlit run app.py
```
# Remaining Tasks

## Installation
```
python -m venv venv (optional)
venv\Scripts\activate (optional)
pip install -r requirements.txt
```

## 1. Member 1: Data Understanding & Cleaning
The files `src/loader.py` and `src/cleaning.py` exist but are currently **skeletons/placeholders**.
- [ ] **Report**: Write dataset description (Source, History, Purpose) & Column meanings.
- [ ] **Statistics**: Implement code to output data info (`.info()`, `.describe()`) effectively.
- [ ] **Data Cleaning Logic (`src/cleaning.py`)**:
    - [ ] Handle missing values (fill or drop).
    - [ ] Remove duplicate rows.
    - [ ] Normalize text formats (if any).
    - [ ] Detect and handle outliers.
    - [ ] Implement logging for the cleaning process.

## 2. Member 2: Documentation 
- [ ] **Report**: Write report section explaining Transformation (Encoding, Scaling, Feature Engineering) and Visualization (Interpretation of the 5 charts).

## 3. Member 3: Integration & UI
The `src/main.py` is functional for the script pipeline, but the UI requirement is missing.
- [ ] **UI Development**: Build the **Streamlit** interface as requested.
    - *Note: `src/main.py` currently runs as a console script. Member 3 needs to adapt this.*
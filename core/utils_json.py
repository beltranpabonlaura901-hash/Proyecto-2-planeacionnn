import io
import pandas as pd

def _j(df):
    """Convierte DataFrame a JSON para guardar en dcc.Store"""
    return df.to_json(orient="split") if not df.empty else "{}"

def _rj(j):
    """Convierte JSON a DataFrame"""
    if not j or j in ("{}", "null", "None"):
        return pd.DataFrame()
    try:
        return pd.read_json(io.StringIO(j), orient="split")
    except:
        return pd.DataFrame()

def _j_dict(d):
    """Convierte dict de DataFrames a dict de JSON"""
    return {k: _j(v) for k, v in d.items()}

def _rj_dict(d):
    """Convierte dict de JSON a dict de DataFrames"""
    return {k: _rj(v) for k, v in d.items()}

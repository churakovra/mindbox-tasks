from pandas import DataFrame, Timedelta
from pandas import factorize

SESSION_GAP_MINUTES: int = 3

def add_session_id(dataframe: DataFrame, session_limit: int = SESSION_GAP_MINUTES):
    df = dataframe.sort_values(["customer_id", "timestamp"]).copy()
    df['time_diff'] = df.groupby('customer_id')['timestamp'].diff()
    df['new_session'] = (df['time_diff'] > Timedelta(minutes=session_limit)) | (df['time_diff'].isna())

    dataframe['session_in_user'] = dataframe.groupby('customer_id')['new_session'].cumsum()

    df['session_id'] = df['customer_id'] * 1_000_000 + df['session_number']
    dataframe.drop(columns=['time_diff', 'new_session', 'session_in_user'], inplace=True)

    return dataframe
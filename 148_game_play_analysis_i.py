# Group the player IDs based on the first event date (first_login) and return.

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    return activity.rename(columns = {'event_date': 'first_login'})
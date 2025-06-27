import pandas as pd 

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    filtered = stadium[stadium['people'] >= 100].copy()
    # case in which we have less than 3
    if len(filtered) < 3:
        return pd.DataFrame(columns=['id', 'visit_date', 'people'])
    
    # sort by id for checking consecutive works
    filtered = filtered.sort_values('id')
    filtered['diff'] = filtered['id'].diff().fillna(1) # checking the differences
    filtered['group'] = (filtered['diff'] != 1).cumsum()
    
    groups = filtered.groupby('group')
    
    valid_groups = [group for _, group in groups if len(group) >= 3]
    
    if not valid_groups:
        return pd.DataFrame(columns=['id', 'visit_date', 'people'])
    # concatenate or (merging ~ in other words)
    valid_ids = pd.concat(valid_groups)['id']
    
    result = stadium[stadium['id'].isin(valid_ids)].sort_values('visit_date')
    return result
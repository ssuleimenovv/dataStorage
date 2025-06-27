import pandas as pd 

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # setting (statuses - roles) for both of them 
    client_status = users[users['role'] == 'client'].set_index('users_id')['banned']
    driver_status = users[users['role'] == 'driver'].set_index('users_id')['banned']
    
    # now total trips 
    trips['valid_client'] = trips['client_id'].map(client_status) == 'No'
    trips['valid_driver'] = trips['driver_id'].map(driver_status) == 'No'
    
    # valid_trips 
    valid_trips = trips[trips['valid_client'] & trips['valid_driver']]
    valid_trips['cancelled'] = valid_trips['status'].str.contains('cancelled')
    
    # daily stats analysis
    daily_stats = valid_trips.groupby('request_at').agg(
        total=('id', 'count'),
        cancelled=('cancelled', 'sum')
    ).reset_index()
    
    daily_stats['Cancellation Rate'] = (daily_stats['cancelled'] / daily_stats['total']).round(2)
    result = daily_stats[['request_at', 'Cancellation Rate']].rename(columns={'request_at': 'Day'})
    
    return result
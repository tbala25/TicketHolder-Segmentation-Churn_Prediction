from localLibrary_DatabaseSchema import *
from localLibrary_dataQueries.py import *

STM_queries = {'SG_STM':SG_STM,'MK_STM':MK_STM, 'YZ_STM':YZ_STM,
                'FTS_STM':FTS_STM, 'CRM_STM':CRM_STM}
nonSTM_queries = {'SG_nonSTM':SG_nonSTM,'MK_nonSTM':MK_nonSTM,
                'YZ_nonSTM':YZ_nonSTM, 'FTS_nonSTM':FTS_nonSTM,
                'CRM_nonSTM':CRM_nonSTM}
lost_queries = {'SG_lost':SG_lost,'MK_lost':MK_lost, 'YZ_lost':YZ_lost,
                'FTS_lost':FTS_lost, 'CRM_lost':CRM_lost}

for k,query in STM_queries:
    cursor.executeStament(query)
    df_columns = [column[0] for column in cursor.description]
    df_data = cursor.fetchall()
    df_arr = []
    for row in df_data:
        df_arr.append(dict(zip(df_columns, row)))
    df = pd.DataFrame(df_arr, columns = df_columns)
    df.to_csv(k+'.csv')
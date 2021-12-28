import configparser
import psycopg2
from sql_queries import copy_table_queries, \
    insert_table_queries, \
    select_table_queries, \
    copy_table_queries_test, \
    ts_test_queries

import time


def load_staging_tables_test(cur, conn):
    """
        Loading test for staging tables
    """
    for query in copy_table_queries_test:
        cur.execute(query)
        conn.commit()

def load_staging_tables(cur, conn):
    """
        Loading from s3 to staging tables using copy sql 
    """
    for query in copy_table_queries:
        # print(query)
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """
        Inserting data from staging tables to DW tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def test(cur):
    """
        Run Select statements from all newly created/inserted 
        DW tables to verify import
    """
    for query in select_table_queries:
        cur.execute(query)
        print(cur.fetchall())
def test_ts(cur):
    for query in ts_test_queries:
        cur.execute(query)
        print(cur.fetchall())


def main():
    """
        Main function to retive config / connect to db and run etl queries
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    test(cur)

    # load_staging_tables_test(cur, conn)
    # test_ts(cur)
    # insert_tables(cur, conn)
    # test(cur)

    conn.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("%s Time taken for etl(seconds): " % (time.time() - start_time))
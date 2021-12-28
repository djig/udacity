import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries, create_table_queries_test, drop_table_queries_test


def drop_tables_test(cur, conn):
    for query in drop_table_queries_test:
        cur.execute(query)
        conn.commit()


def create_tables_test(cur, conn):
    for query in create_table_queries_test:
        cur.execute(query)
        conn.commit()


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print(*config['CLUSTER'].values())
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    # following is for testing after stage data copied to db.
    # drop_tables_test(cur, conn)
    # create_tables_test(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
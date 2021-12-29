import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

ARN             = config.get('IAM_ROLE', 'ARN')
LOG_DATA        = config.get('S3', 'LOG_DATA')
LOG_JSONPATH    = config.get('S3', 'LOG_JSONPATH')
SONG_DATA       = config.get('S3', 'SONG_DATA') 

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
    event_id    BIGINT IDENTITY(0,1)    NOT NULL,
    artist      VARCHAR                 NULL,
    auth        VARCHAR                 NULL,
    firstName   VARCHAR                 NULL,
    gender      VARCHAR                 NULL,
    itemInSession VARCHAR               NULL,
    lastName    VARCHAR                 NULL,
    length      VARCHAR                 NULL,
    level       VARCHAR                 NULL,
    location    VARCHAR                 NULL,
    method      VARCHAR                 NULL,
    page        VARCHAR                 NOT NULL SORTKEY DISTKEY,
    registration VARCHAR                NULL,
    sessionId   INTEGER                 NOT NULL,
    song        VARCHAR                 NULL,
    status      INTEGER                 NULL,
    ts          BIGINT                  NOT NULL,
    userAgent   VARCHAR                 NULL,
    userId      INTEGER                 NULL
);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs           INTEGER         NULL,
    artist_id           VARCHAR         NOT NULL SORTKEY DISTKEY,
    artist_latitude     VARCHAR         NULL,
    artist_longitude    VARCHAR         NULL,
    artist_location     VARCHAR(500)   NULL,
    artist_name         VARCHAR(500)   NULL,
    song_id             VARCHAR         NOT NULL,
    title               VARCHAR(500)   NULL,
    duration            DECIMAL(9)      NULL,
    year                INTEGER         NULL
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INTEGER IDENTITY(0,1)   NOT NULL SORTKEY,
    start_time  TIMESTAMP               NOT NULL,
    user_id     VARCHAR(50)             NOT NULL DISTKEY,
    level       VARCHAR(10)             NOT NULL,
    song_id     VARCHAR(40)             NOT NULL,
    artist_id   VARCHAR(50)             NOT NULL,
    session_id  VARCHAR(50)             NOT NULL,
    location    VARCHAR(100)            NULL,
    user_agent  VARCHAR(255)            NULL
);
""")

user_table_create = ("""
 CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER                 NOT NULL SORTKEY,
    first_name  VARCHAR(50)             NULL,
    last_name   VARCHAR(80)             NULL,
    gender      VARCHAR(10)             NULL,
    level       VARCHAR(10)             NULL
) diststyle all;
""")

song_table_create = ("""
 CREATE TABLE IF NOT EXISTS songs (
    song_id     VARCHAR(50)             NOT NULL SORTKEY,
    title       VARCHAR(500)           NOT NULL,
    artist_id   VARCHAR(50)             NOT NULL,
    year        INTEGER                 NOT NULL,
    duration    DECIMAL(9)              NOT NULL
);
""")

artist_table_create = ("""
 CREATE TABLE IF NOT EXISTS artists (
    artist_id   VARCHAR(50)             NOT NULL SORTKEY,
    name        VARCHAR(500)           NULL,
    location    VARCHAR(500)           NULL,
    latitude    DECIMAL(9)              NULL,
    longitude   DECIMAL(9)              NULL
) diststyle all;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time  TIMESTAMP               NOT NULL SORTKEY,
    hour        SMALLINT                NULL,
    day         SMALLINT                NULL,
    week        SMALLINT                NULL,
    month       SMALLINT                NULL,
    year        SMALLINT                NULL,
    weekday     SMALLINT                NULL
) diststyle all;
""")

# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events FROM {}
    credentials 'aws_iam_role={}'
    format as json {}
    STATUPDATE ON
    region 'us-west-2';
""").format(LOG_DATA, "arn:aws:iam::178854808613:role/sparkify-dwh-role", LOG_JSONPATH)

staging_songs_copy = ("""
    COPY staging_songs FROM {}
    credentials 'aws_iam_role={}'
    format as json 'auto'
    ACCEPTINVCHARS AS '^'
    STATUPDATE ON
    region 'us-west-2';
""").format(SONG_DATA, "arn:aws:iam::178854808613:role/sparkify-dwh-role")

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
    )
SELECT  
    DISTINCT TIMESTAMP 'epoch' + events.ts/1000 \
    * INTERVAL '1 second'   AS start_time,
    events.userId AS user_id,
    events.level  AS level,
    songs.song_id AS song_id,
    songs.artist_id AS artist_id,
    events.sessionId AS session_id,
    events.location AS location,
    events.userAgent AS user_agent
FROM 
    staging_events AS events
JOIN 
    staging_songs AS songs
    ON
(events.artist = songs.artist_name)
WHERE 
    events.page = 'NextSong';
""")

user_table_insert = ("""
INSERT INTO users (
    user_id,
    first_name,
    last_name,
    gender,
    level
)
SELECT
    DISTINCT userId AS user_id,
    firstName AS first_name,
    lastName AS last_name,
    gender AS gender,
    level AS level
FROM 
    staging_events
WHERE 
    page = 'NextSong';
""")

song_table_insert = ("""
 INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration
)
SELECT
    DISTINCT song_id,
    title,
    artist_id,
    year,
    duration
FROM staging_songs;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id,
    name,
    location,
    latitude,
    longitude
)
SELECT
    DISTINCT artist_id,
    artist_name AS name,
    artist_location AS location,
    artist_latitude AS latitude,
    artist_longitude  AS longitude
FROM staging_songs;
""")

time_table_insert = ("""
INSERT INTO time (                  
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
)
SELECT  
    DISTINCT TIMESTAMP 'epoch' + ts/1000 \
        * INTERVAL '1 second' AS start_time,
    EXTRACT(hour FROM start_time) AS hour,
    EXTRACT(day FROM start_time)  AS day,
    EXTRACT(week FROM start_time)  AS week,
    EXTRACT(month FROM start_time) AS month,
    EXTRACT(year FROM start_time)  AS year,
    EXTRACT(week FROM start_time)  AS weekday
FROM
    staging_events
WHERE
    page = 'NextSong';
""")

 

# QUERY LISTS

stage_events_select_ts_1 =("""
SELECT  
    DISTINCT TIMESTAMP 'epoch' + events.ts/1000 \
    * INTERVAL '1 second'   AS start_time
FROM 
    staging_events AS events
JOIN 
    staging_songs AS songs
    ON
(events.artist = songs.artist_name)
WHERE 
    events.page = 'NextSong'
""")

stage_events_select_ts_2 =("""
SELECT  
    DISTINCT TIMESTAMP 'epoch' + ts/1000 \
        * INTERVAL '1 second' AS start_time,
    EXTRACT(hour FROM start_time) AS hour,
    EXTRACT(day FROM start_time)  AS day,
    EXTRACT(week FROM start_time)  AS week,
    EXTRACT(month FROM start_time) AS month,
    EXTRACT(year FROM start_time)  AS year,
    EXTRACT(week FROM start_time)  AS weekday
FROM
    staging_events
WHERE
    page = 'NextSong'

""")

stage_events_select = ("""
SELECT COUNT(*) as stageEventsCnt
FROM staging_events;
""")
stage_songs_select = ("""
SELECT COUNT(*) as stageSongsCnt
FROM staging_songs;
""")
songs_play_select = ("""
SELECT COUNT(*) as songsPlayCnt
FROM songplays;
""")
users_select = ("""
SELECT COUNT(*) as usersCnt
FROM users;
""")
artise_select = ("""
SELECT COUNT(*) as artistsCnt
FROM artists;
""")
songs_select = ("""
SELECT COUNT(*) as songsCnt
FROM songs;
""")
time_select = ("""
SELECT COUNT(*) as timeCnt
FROM time;
""")

test_query = ("""
SELECT  
    sp.songplay_id,
    u.user_id,
    s.song_id,
    u.last_name,
    sp.start_time,
    a.name,
    s.title
FROM 
    songplays AS sp
JOIN 
    users   AS u 
ON 
    (u.user_id = sp.user_id)
JOIN
    songs   AS s 
ON 
    (s.song_id = sp.song_id)
JOIN 
    artists AS a 
ON 
    (a.artist_id = sp.artist_id)
JOIN 
    time    AS t 
ON
    (t.start_time = sp.start_time)
ORDER BY
    (sp.start_time)
LIMIT 1000;
""")

copy_table_queries = [staging_events_copy, staging_songs_copy]
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
select_table_queries = [stage_events_select, stage_songs_select, songs_play_select, users_select, artise_select, songs_select, time_select, test_query]


#  following is to test queries after data copied to staging tables
copy_table_queries_test = [ staging_songs_copy]
# staging_songs_copy staging_events_copy
ts_test_queries = [stage_events_select_ts_1, stage_events_select_ts_2]
create_table_queries_test = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries_test = [ songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries_test = [songplay_table_insert, user_table_insert, time_table_insert, artist_table_insert,song_table_insert ]
select_table_queries_test = [songs_play_select, users_select, artise_select, songs_select, time_select]

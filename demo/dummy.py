from flask_table import table,col
 
class results(table):
    id = col('id', show=false)
    artist = col('artist')
    title = col('title')
    release_date = col('release date')
    publisher = col('publisher')
    media_type = col('media')

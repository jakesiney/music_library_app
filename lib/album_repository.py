from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(
                row["id"],
                row["title"],
                row["release_year"],
                row["artist_id"])

            albums.append(item)
        return albums

    def create(self, album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])

    def find_album(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE artist_id = %s', [artist_id])
        print(rows)
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

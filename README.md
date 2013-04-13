Last.FM Playing / Played
========================

Dead Simple.

Prints what a user is listening to, or what they've previously listened to.


Usage
-----

    $ ./played.py <username>


Advanced Usage
--------------
So you wanna get fancy?

    $ ./played.py <username> "[PLAYING]:"


Example Output
--------------
Currently playing a song:

    $ ./played.py rickysaltzer
    Listening To: Mountains of Might - Immortal 


Not currently playing a song:

    $ ./played.py rickysaltzer
    Last Played: Mountains of Might - Immortal [9 minutes ago]

API Usage
---------
I wouldn't really call this an API, but whatever...give it a go.

    >>> playing.currently_playing("rickysaltzer")
        pylast.Track(u'Immortal', u'Mountains of Might', pylast.LastFMNetwork('cf7dc8bd12a610a8209ab98bdfa773b4', '', '', '', ''))

    >>> playing.print_track(playing.currently_playing("rickysaltzer"), "Listening To: ")
        Listening To:  Mountains of Might - Immortal 

    >>> playing.currently_playing("rickysaltzer").artist.get_name()
        u'Immortal'

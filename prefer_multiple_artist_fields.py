PLUGIN_NAME = 'Prefer Multiple Artists Fields'
PLUGIN_AUTHOR = 'Alex Palmer'
PLUGIN_DESCRIPTION = '''Replaces artist and albumartist tags with the contents of the artists and albumartists tags.'''
PLUGIN_VERSION = "1.1"
PLUGIN_API_VERSIONS = ["0.16", "1.0", "2.0"]

MAPPINGS = [
    {'from': 'artists', 'to': 'artist'},
    {'from': 'albumartists', 'to': 'albumartist'}
]

from picard.metadata import register_track_metadata_processor


def prefer_multiple_artist_fields(tagger, metadata, release, track):
    for mapping in MAPPINGS:
        from_ = mapping['from']
        to = mapping['to']
        if from_ in metadata:
            metadata[to] = metadata[from_]
            del metadata[from_]


register_track_metadata_processor(prefer_multiple_artist_fields)

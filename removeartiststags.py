PLUGIN_NAME = 'Remove Artists Tags'
PLUGIN_AUTHOR = 'Alex Palmer'
PLUGIN_DESCRIPTION = '''Removes artists and albumartists tags.'''
PLUGIN_VERSION = "1.1"
PLUGIN_API_VERSIONS = ["0.16", "1.0", "2.0"]

from picard.metadata import register_track_metadata_processor

def remove_artists_tags(tagger, metadata, release, track):
    TAGS = ['artists', 'albumartists']
    for tag in TAGS:
        if tag in metadata:
            del metadata[tag]

register_track_metadata_processor(remove_artists_tags)

PLUGIN_NAME = 'Remove Artists Tags'
PLUGIN_AUTHOR = 'Alex Palmer'
PLUGIN_DESCRIPTION = '''Removes ARTISTS, ALBUMARTISTS tags.'''
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["0.16"]

from picard.metadata import register_track_metadata_processor

def remove_sort_tags(tagger, metadata, release, track):
    TAGS = ['artists', 'albumartists']
    for tag in TAGS:
        if tag in metadata:
            del metadata[tag]

register_track_metadata_processor(remove_sort_tags)

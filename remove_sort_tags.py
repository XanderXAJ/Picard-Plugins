PLUGIN_NAME = 'Remove Sort Tags'
PLUGIN_AUTHOR = 'Alex Palmer'
PLUGIN_DESCRIPTION = '''Removes albumartistsort, albumsort, artistsort, composersort and titlesort tags.'''
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["0.16", "1.0", "2.0"]

TAGS = ['albumartistsort', 'albumsort', 'artistsort', 'composersort', 'titlesort']

from picard.metadata import register_track_metadata_processor


def remove_sort_tags(tagger, metadata, release, track):
    for tag in TAGS:
        if tag in metadata:
            del metadata[tag]


register_track_metadata_processor(remove_sort_tags)

# Music-Playlist-Analyzer

# Project Description
Playlist Analyzer is a Python script designed to analyze and process iTunes playlist files (.xml). The script can find common tracks across multiple playlists, identify duplicate tracks within a single playlist, and generate statistics like track ratings and durations. This projects aimed to improve my knowledge in .xml file analysis, a common file in the realm of data organization.

# Features
Common Track Finder: Identifies tracks that are common across multiple playlists.
Duplicate Finder: Finds duplicate songs in a single playlist based on the track name and duration.
Playlist Statistics: Plots statistics such as track duration vs. rating and generates histograms of track durations.

# Usage
The script can be used to perform three main tasks: finding common tracks, plotting statistics, and finding duplicates. Each task is triggered by a specific command-line argument.

**Finding Common Tracks**
To find tracks that are common across multiple playlists:

***python playlist_analyzer.py --common playlist1.xml playlist2.xml***
Output: A file named common.txt listing all the tracks that appear in all provided playlists.

**Plotting Track Statistics**
To generate and display statistics such as track duration vs. rating:

***python playlist_analyzer.py --stats playlist.xml***
Output: A plot showing track duration vs. rating and a histogram of track durations.

**Finding Duplicate Tracks**
To find duplicate tracks within a single playlist:

***python playlist_analyzer.py --dup playlist.xml***
Output: A file named dups.txt listing all the duplicate tracks along with the number of occurrences.

# Technologies Used
Python
Matplotlib: For plotting statistics and histograms.
NumPy: For numerical operations.
plistlib: For reading and parsing iTunes playlist files in XML format.


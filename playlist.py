# finding duplicates
# function to find duplicate songs in the playlist
# using the findDuplicates function to find duplicates
import re, argparse 
import sys 
from matplotlib import pyplot 
import plistlib 
import numpy as np

def findCommonTracks(fileNames):
    # a list of sets of track names
    trackNamesSet = []
    for fileName in fileNames:
          # create a new set
          trackNames = set()
          try:
               # read in playlist
               plist = plistlib.load(open(fileName, 'rb'))
               # get the tracks
               tracks = plist['Tracks']
               # iterate through the tracks
               for trackID, track in tracks.items():
                    try:
                         # add the track name to a set
                         trackNames.add(track['Name'])
                    except KeyError:
                         # ignore
                         pass
                    # add to list
               trackNamesSet.append(trackNames)
          except Exception as e:
               print(f"Error processing {fileName}: {e}")

    if trackNamesSet:
        # get the set of common tracks
        commonTracks = set.intersection(*trackNamesSet)
        # write to file
        if commonTracks:
            with open("common.txt", "w") as f:
                for val in commonTracks:
                    f.write(f"{val}\n")
                print(f"{len(commonTracks)} common tracks found. Track names written to common.txt.")
        else:
            print("No common tracks!")
    else:
        print("No valid track names found in the provided files.")


# extracting data from playlist for statistics
def plotStats(fileName):
     try:
          # read in a playlist
          plist = plistlib.load(open(fileName, 'rb'))
          # get the tracks from the playlist
          tracks = plist['Tracks']
          # create a lists of songs rating and track durations
          ratings = []
          durations = []
          # iterate through the tracks
          for trackId, track in tracks.items():
               try:
                    ratings.append(track['Album Rating'])
                    durations.append(track['Total Time'])
               except KeyError:
                    # ignore 
                    pass
          # validating if data was collected
          if not ratings or not durations:
               print(f"No valid Album Rating/Total Time data in {fileName}.")
               return

          x = np.array(durations, np.int32) / 60000.0
          y = np.array(ratings, np.int32)

          pyplot.subplot(2, 1, 1)
          pyplot.plot(x, y, 'o')
          pyplot.axis([0, 1.05 * np.max(x), -1, 110])
          pyplot.xlabel('Track duration')
          pyplot.ylabel('Track rating')

          # plot histogram
          pyplot.subplot(2, 1, 2)
          pyplot.hist(x, bins=20)
          pyplot.xlabel('Track duration')
          pyplot.ylabel('Count')

          # show plot
          pyplot.show()
     
     except Exception as e:
          print(f"Error processing {fileName}: {e}")



def findDuplicates(fileName):
     print(f'Finding duplicate tracks in {fileName}...')
     try:
          plist = plistlib.load(open(fileName, 'rb'))
          tracks = plist['Tracks']
          trackNames = {}
          for trackID, track in tracks.items():
               try:
                    name = track['Name']
                    duration = track['Total Time']
                    if name in trackNames:
                         if duration // 1000 == trackNames[name][0] // 1000:
                              count = trackNames[name][1]
                              trackNames[name] = (duration, count + 1)
                         else:
                              trackNames[name] = (duration, 1)
                    else:
                         trackNames[name] = (duration, 1)
               except KeyError:
                    pass

          dups = [(v[1], k) for k, v in trackNames.items() if v[1] > 1]
          if dups:
               print(f"Found {len(dups)} duplicates. Track names saved to dups.txt")
               with open("dups.txt", "w") as f:
                    for val in dups:
                         f.write(f"[{val[0]}] {val[1]}\n")
          else:
               print("No duplicates found")
     except Exception as e:
          print(f"Error processing {fileName}: {e}")


# main
def main():
    descStr = """This program analyzes playlist files exported from iTunes."""
    parser = argparse.ArgumentParser(description=descStr)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='pFile', required=False)
    group.add_argument('--dup', dest='plFile', required=False)

    args = parser.parse_args()

    if args.plFiles:
        findCommonTracks(args.plFiles)
    elif args.pFile:
        plotStats(args.pFile)
    elif args.plFile:
        findDuplicates(args.plFile)
    else:
        print("These are not the tracks you are looking for.")

if __name__ == "__main__":
    main()

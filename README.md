# filmtipset-comment-export
Export a user's movie comments to a file

Manual:
You need Python 3.6, see www.python.org.
Go to your Filmtipset.se profile, click on "Filmkommentarer". Note the user number in the URL bar "&member=[number]".
Run "python ExportComments.py [number]".
You should now have a file named Filmtipset_comments.csv, containing movie titles and comments, that you can open in a spreadsheet application etc. The columns are separated by tabs.

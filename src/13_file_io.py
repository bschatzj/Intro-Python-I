"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('../foo.txt', 'r') as file:
    for line in file:
        print(line)

file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


file = open('bar.txt', 'w')

file.write(

    """
    Still going strong (He's still going strong)
Yeah, yeah (He's still going strong)
Remember Ned Stark, he was a lot of fun. (So fun)
But he didn't make it past Season One (Oh no)
Robert Baratheon was part of that crew
But he never made it to Season Two
The King of the North was cool, you said (So cool)
[Lyrics from: https:/lyrics.az/peter-dinklage/-/still-going-strong.html]
Another favorite that ended up dead (He's dead)
You thought that Joffrey had to survive
He ain't in the credits for Season Five (Season Five)
Baby, you know I'm the man for all seasons
Characters get cut for various reasons (Ow ow)
Some people's parts just ain't that long
But not me (Not me, not me, not me)
I'm still going strong (He's still going strong)
    """
)

file.close()

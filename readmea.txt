## ***Sanity Lose It!***

Introduction
---
This is an attempt to reverse engineer one of the puzzles that I played as a child called Dr Woods Sanity Lose It (little did I know I would actually lose my sanity solving it).
The premise of the puzzle was the very definition of simplicity. You are given 4 cubes, there's nothing special about these cubes except that each cube face had either of
these 4 colours - Purple (P), Yellow (Y), Green (G), Red (R).
The challenge being to stack the cubes on top of each other in such a way that you have all four unique colours and THERE'S ONLY ONE UNIQUE SOLUTION TO IT!
I'll demonstrate to you what I mean.

CASE 1:
Front view          Right View          Left View           Behind View

    P                   G                  Y                   R
    Y                   P                  G                   P
    R                   Y                  R                   G
    G                   R                  P                   Y

CASE 2:
Front view          Right View          Left View           Behind View

    P                   G                  Y                   R
    Y                   P                  G                   G
    R                   Y                  R                   G
    G                   R                  P                   Y

CASE 3:
Front view          Right View          Left View           Behind View

    P                   G                  Y                   R
    Y                   P                  G                   P
    Y                   P                  R                   G
    G                   R                  P                   Y

Of all the cases mentioned above, CASE 1 is the solution because it has all unique values on the stacks,
CASE 2 fails because the behind view has 2 colours that are repeating
CASE 3 fails front view and right view has 2 colours repeating.

You get the gist! If one thinks about the permutations and combinations possible for any given configuration, the number would be astounding.
(I calculated it, and it amounts to 57,480.) Pretty diabolical to make that into a children's puzzle game and unleashing this monster onto the world.

Now even though I wasn't able to solve the puzzle when I was a child (also the fact that I lost all of them cubes somewhere, doesn't help), the problem stuck with me and here is my humble attempt to reverse engineer that particular itch. (It also doesn't help when my cousin says he solved it, no one believes him!)

***Solution***
In solving this, I had to set up some ground rules and after choosing my poison of choice, python. I had to first visualize how the cube looks in an array, since
it being a 3D object and to show it in an array format, I took inspiration from Rubik's cube especially how one would rotate the cube.

The demonstration of the cube is as follows, if you flatten the cube this is how it looks.

	Up
left       Front       Right       Behind
            Down

The array visualisation looks like this= [Up, left, front, right, behind, down]

Using the notations of U, M, L

U1 -> indicates clockwise 90 degrees rotation on the upper face
U2 -> meaning clockwise 90*2 degrees rotation on upper face
U3 -> meaning clockwise 90*3 degrees rotation on upper face
L1 -> meaning clockwise 90 degrees rotation on the left side
L2 -> meaning clockwise 90*2 degrees rotation on the left side
L3 -> meaning clockwise 90*3 degrees rotation on the left side 
M0 -> the cube remains as is.

For colours, I used the number notation 1,2,3,4 instead of colours. (You could use colours too if you want!)

One needs to understand this concept as quickly as possible as this is gonna be the bane of the entire solution.
Let's assume a random cube looks like this
Initial = [1,  2,    3,     1,     4,        2]
	  [Up, left, front, right, behind, down]

U1 on initial = [1, 3, 1, 4, 2, 2] 
U2 on initial = [1, 1, 4, 2, 3, 2]
U3 on initial = [1, 4, 2, 3, 1, 2]
L1 on initial = [1, 1, 3, 2, 4, 2]
L2 on initial = [2, 1, 3, 2, 4, 1]
L3 on initial =	[2, 2, 3, 1, 4, 1]
M0 on initial =	[1, 2, 3, 1, 4, 2]


***Code Explanation***
The rest I have explained as much as possible while defining the functions and using them, feel free to message me if something isn't clear!

Our focus would be to the SLIver (Sanity Lose It, pun intended) of light that one sees at the end of a tunnel.
SLI_ver9: here we tried to brute force our way to the solution be adding as much filters tactically as one could think of.
It became apparent that even though the presence of clever filters will not help my situation.

SLI_ver10 to the rescue, I was able to get rid of brute forcing my way to the solution and come up with a different tack to approach this.
I was successful, and with the placement of tighter filters, I reached a solution.

SLI_ver9's computation time was crossing more than 10 hours (I didn't let it run completely)
SLI_ver10's computation ----- wait for it ---- was bought down to less than 25 minutes.

The solution has been documented, but my war against this problem is far from over,
I need to compute the solution faster, add more meaningful filters, and tackle the time it take for my expensive function to run.

And also ensure that this doesn't haunt me again for the rest of my life.





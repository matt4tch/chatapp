## Preface/Project Story: ##
I am in the process of learning web development by creating a Chat Application from scratch, rather than
by taking courses on the subject, although I am following tutorials and researching a lot along the way as 
I discover new features that need to be implemented.

I first started this project by finding out what components make up a web application in general, then started to dissect
it into components by creating a small backend server without a front-end for my own usage and experimentation, which allowed
me to learn routing, url building, sessions, amongst many other components of the web framework. Along the way, I learned plenty
of intermediate/advanced Python features such as decorators, as well as kwaargs and args.

I have never built a full-scale web application before, so I had trouble with organizing it until I got inspiration from
other projects on github on how to organize my directories, and by observation and with some experimentation, I learned what a
requirements.txt file was, what environment variables were, as well as what a Python package is (and as you can tell, 
I created an application package in this project myself), and how venv's and git can be used to streamline development.

When I got to a point where I was mostly satisfied with the backend flask component of the project, I decided to move onto
the front-end. I didn't have much prior experience with HTML/CSS, but I learned basic HTML by experimenting with tags, 
adding attributes to them using one of my VsCode's extention's suggestions, and learning the overall structure of HTMl through
experimentation online, along with some articles on what the DOM is. However, I had come to realize that I should focus more on
the JavaScript and Flask part of the project, as that is what I am primarily seeking to learn, and so I have instead utilized
Boostrap and JQuery to avoid having to rely on my very limited knowledge of CSS.

What has been especially confusing for me lately is how JavaScript can be integrated to update the webpages of all users on the network, which through some research, I have come to realize that WebSockets could solve. I created a few basic event handlers
and modified some HTMl code, but realized that I do not have a solid enough background of the big picture (the DOM) to understand
why I encounter the errors I encounter, for example, my JavaScript based changes in HTML not reflecting in the browser upon submitting a form, which I might utilize Ajax to solve.

Throughout the course of the project so far, the biggest thing I have learned was how to step outside of my comfort zone and
experiment with technologies that I have never used before, rather than taking the safe path (which I fell into the trap of doing before) of only using technologies that I fully understood and convincing myself that in order to use something new, I have to first understand it deeply. However, using the approach that I am currently taking, I am actually learning more because I am constantly trying to solve bugs and fix errors I have never seen before and through practice, I become more effective in problem-solving. 

# Chat-Web-App

## Setup

Ensure you have python 3.11.1+ installed. 

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
cd website
python main.py
```
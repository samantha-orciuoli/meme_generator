# intermediate_python

The goal of this project is to build a meme generator – an application to generate memes,
including an image with an overlaid quote. (Udacity)

To start this project, Udacity provided some code and data to get started. So the first step is to download the starter
code and get generally familiar with what it includes


The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes,
a quote contains a body and an author:
"This is a quote body" - Author

This module will be composed of many classes and will demonstrate my understanding of complex inheritance, 
abstract classes, class methods, strategy objects and other fundamental programming principles. I designed 
a system to extract each quote line-by-line from these files.

Separate strategy objects realized IngestorInterface for each file type (csv, docx, pdf, txt).
A final Ingestor class realized the IngestorInterface abstract base class and encapsulated the helper classes.
It implemented logic to select the appropriate helper for a given file based on filetype.

The Meme Engine Module is responsible for manipulating and drawing text onto images. It reinforced my
understanding of object-oriented thinking while demonstrating my skill using a more advanced third party library for
image manipulation.

Note: The above has incorporated the directions provided by Udacity.

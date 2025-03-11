# fancyPy.py

# usage: fancyPy.py [-h] [--style STYLE] [--length LENGTH] [--output]
#                   [--filename FILENAME [FILENAME ...]]
#                   title string [title string ...]
# 
# Fancify a given title into a block comment.
# 
# positional arguments:
#   title string          the input title string to be fancified
# 
# optional arguments:
#   -h, --help            show this help message and exit
#   --style STYLE, -S STYLE
#                         comment block style either Python, C, C++, Java,
#                         MATLAB, or LaTeX (default: Python)
#   --length LENGTH, -L LENGTH
#                         comment block length (default: 40, min: title
#                         length + 12)
#   --output, -O, -o      (optional) save the fancified title in a txt file
#   --filename FILENAME [FILENAME ...], -F FILENAME [FILENAME ...]
#                         (if output option is called) set output filename
#                         (default: 'fancyPy_output')

# Import the argparse library for handling command-line arguments
import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Fancify a given title into a block comment.')

# Define the title string as a positional argument
parser.add_argument('title', metavar='title string', type=str, nargs='+',
                    help='the input title string to be fancified')

# Define the optional argument for the style of the comment block
parser.add_argument('--style', '-S', type=str, default='Python', 
                    help='comment block style either Python, C, C++, Java, MATLAB, or LaTeX (default: Python)')

# Define the optional argument for the length of the comment block
parser.add_argument('--length', '-L', type=int, default=40, 
                    help='comment block length (default: 40, min: title length + 12)')    

# Define the optional argument for output file creation
parser.add_argument('--output', '-O', '-o', action='store_true', 
                    help='(optional) save the fancified title in a txt file')

# Define the optional argument for the filename of the output
parser.add_argument('--filename', '-F', type=str, default=['fancyPy_output'], nargs='+', 
                    help='(if output option is called) set output filename (default: \'fancyPy_output\')')            

# Parse the arguments
args = parser.parse_args()

# Combine the title strings into one string (removes trailing space)
title = ''.join([t + ' ' for t in args.title])[:-1]

# Store the style and block length arguments
style = args.style
block_len = args.length 

# Calculate the title length
title_len = len(title)

# Ensure the block length is large enough to accommodate the title with padding
if (block_len - title_len - 2) < 0:
    block_len = title_len + 12

# Check the style and build the comment block accordingly
if style[0].lower() == 'c' or style.lower() == 'java':
    style = 'C/C++/Java'
    # Define the top and bottom lines of the comment block
    out_line1 = ''.join(['/*\n' , '-'*block_len])
    out_line2 = ''.join(['-'*block_len , '\n*/'])
    # Format the middle line with title and padding
    mid_line = ' '*((block_len - title_len - 2) // 2) + ' ' + title + ' ' + ' '*((block_len - title_len - 2) // 2 + (block_len - title_len - 2) % 2) 
    output_str = ''.join([out_line1, '\n', mid_line, '\n', out_line2])
elif style.lower() == 'matlab' or style.lower() == 'latex' or style.lower() == 'tex':
    style = 'MATLAB/LaTeX'
    # Define the top and bottom lines of the comment block
    out_line = '%'*block_len
    # Format the middle line with title and padding
    mid_line = '%'*((block_len - title_len - 2) // 2) + ' ' + title + ' ' + '%'*((block_len - title_len - 2) // 2 + (block_len - title_len - 2) % 2) 
    output_str = ''.join([out_line, '\n', mid_line, '\n', out_line])
else:
    style = 'Python'
    # Define the top and bottom lines of the comment block
    out_line = '#'*block_len
    # Format the middle line with title and padding
    mid_line = '#'*((block_len - title_len - 2) // 2) + ' ' + title + ' ' + '#'*((block_len - title_len - 2) // 2 + (block_len - title_len - 2) % 2) 
    output_str = ''.join([out_line, '\n', mid_line, '\n', out_line])

# Output the fancified comment block along with the style
print(output_str + '\n\n' + 'Comment Style: ' + style)

# If the output option is enabled, write the output to a file
if args.output:
    # Construct the filename for the output
    filename = ''.join([n + '_' for n in args.filename])[:-1]
    path = filename + '.txt'
    # Open the file in write mode and save the fancified title
    with open(path, 'w+') as file:
        file.write(output_str + '\n\n' + 'Style: ' + style)

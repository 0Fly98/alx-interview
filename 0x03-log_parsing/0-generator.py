
Curriculum
Short Specializations
Average: 61.74%
0x03. Log Parsing
Algorithm
Python
 Weight: 1
 Ongoing second chance project - started Jun 18, 2024 5:00 AM, must end by Jun 24, 2024 5:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/11 mandatory
Altogether:  0.0%
Mandatory: 0.0%
Optional: no optional tasks
For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

Concepts Needed:
File I/O in Python:

Understand how to read from sys.stdin line by line.
Python Input and Output
Signal Handling in Python:

Handling keyboard interruption (CTRL + C) using signal handling in Python.
Python Signal Handling
Data Processing:

Parsing strings to extract specific data points.
Aggregating data to compute summaries.
Regular Expressions:

Using regular expressions to validate the format of each line.
Python Regular Expressions
Dictionaries in Python:

Using dictionaries to count occurrences of status codes and accumulate file sizes.
Python Dictionaries
Exception Handling:

Handling possible exceptions that may arise during file reading and data processing.
Python Exceptions
By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

Additional Resources
Mock Technical Interview
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable
The length of your files will be tested using wc
Tasks
0. Log parsing
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.

alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()


# mec-attendance

A module for scraping attendance information of the students of Govt. Model Engineering College. [http://mec.ac.in/attn](http://mec.ac.in/attn)

## Installation

[Download](https://github.com/stc043/mecattendance) the tarball/zip, unpack in a directory and run the following command from the commandline.

    $ python setup.py install
    
You may need to run the above commands with `sudo`.

## Usage

To get the attendance of a student, type the following command.

    $ python mecattendance.py -a "name" "class"

For example:

    $ python mecattendance.py -a "john doe" "c1&2a"

To get the attendance of the whole class, use

    $ python mecattendance.py -c "class"
    
## Module import

You can use the mecattendance module in your python code to get attendance information.

You can try out the following commands in the python interpreter

    >> from mecattendance import Attendance
    
    >> attend=Attendance()
    
    >> #to get the attendance information of a single student
    >> attend.getAttendance("name","class")
    
    >> #you can get various subject codes by passing a third argument
    >> attend.getAttendance("name","class",True)
    
    >> #to get the attendance information of a whole class
    >> attend.getClassAttendance("class")
    
## Example

This example gives you the attendance of a single student.

    from mecattendance import Attendance
    
    attend=Attendance()
    
    name=raw_input("enter the name")
    batch=raw_input("enter the batch")
    
    result=attend.getAttendance(name,batch)
    print " | ".join(result)
    



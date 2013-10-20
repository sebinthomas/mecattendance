#!/usr/bin/env python

# Module to scrape attendance information from
# Govt. Model Engineering College website
# http://mec.ac.in/attn.
# Licence: GPL v3
# If you have any suggestions or have found any bugs, contact
# me(at)sebin(dot)in

    

__author__='Sebin Thomas (me@sebin.in)'
__version__='0.1'

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import sys
import argparse

def empty(seq):
    """ function to check if a nested list is empty."""
    try:
        return all(map(empty,seq))
    except (TypeError, RuntimeError):
        return False



class Attendance:
    """
    Class to get the attendance from the
    Model Engineering College website http://mec.ac.in/attn
    functions: scrape(),getAttendance(name,batch,legend)
    getClassAttendance(batch,legend)
    """
    def __init__(self):
        self.name=None
        self.batch=None
        
        
    def scrape(self):
        """ returns BeautifulSoup object of college attendance page. """
        data=urllib.urlencode({'class':self.batch,'Submit':"View+"})
        try:
            contents=urllib2.urlopen("http://210.212.232.135/attn/view4stud.php",data)
            soup=BeautifulSoup(contents.read())

        except urllib2.HTTPError as e:
            print "HTTP ERROR: "+str(e.code)+" code returned"
            soup=None
            
        except urllib2.URLError as e:
            print "Error occured in scraping data--"+str(e.reason)
            soup=None
        
        return soup
 
    def getClassAttendance(self,batch,legend=None):
        """
        Gets the whole class attendance in a list.
        arguments: batch,legend.
        legend=True includes the subject codes
        """
        self.batch=batch.strip().upper()
        page=self.scrape()
        results=list()
        if page:
            records=page.find('table').findAll('tr')
            for record in records:
                entry=[str(cell.text) for cell in record.findChildren()]
                if not empty(entry):
                    results.append(entry)
        if legend:
            return results
        else:
            return results[1:]

    def getAttendance(self,name,batch,legend=None):
        """
        Gets the individual attendance of students.
        Arguments: name,batch,legend
        """
        self.name=name.strip()
        classResult=self.getClassAttendance(batch,legend)
        for result in classResult:
            try:
                if re.match(self.name,result[1],re.IGNORECASE):
                    if legend:
                        return [classResult[0]]+[result]
                    return result
            except IndexError:
                pass
        return False

    
def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--attendance', type=str, nargs=2,
                       help="Gets the individual attendance",
                       metavar=('name','class'))
    group.add_argument('-c', '--classattn', type=str,
                       help="Gets the attendance of the batch/class",
                       metavar='class')
    if (len(sys.argv)==1):
        parser.print_help()
        sys.exit(1)
    args=parser.parse_args()
    a=Attendance()
    if args.attendance:
        results=a.getAttendance(args.attendance[0],args.attendance[1],True)
        if results:
            for i in range(len(results[0])):
                    print "%s --  %s"%(results[0][i].replace('\r','').replace('\n',''),results[1][i])
        else:
            print "Cannot find the attendance information. Maybe the information don't exist."
            sys.exit(1)
    elif args.classattn:
        results= a.getClassAttendance(args.classattn,True)
        if results:
            for result in results:
                print " ".join([x.replace('\r','').replace('\n','') for x in result])

if __name__=="__main__":
    main()

    

# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Fri Aug  7 15:03:17 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""
import mosspy
import webbrowser


def plagcheck():
    userid = 389750029
    m = mosspy.Moss(userid, "python")       
    # Submission Files
    m.addFilesByWildcard("submission/*.py")
    url = m.send() # Submission Report URL
    print ("Report Url: " + url)
    # Save report file
    m.saveWebPage(url, "report.html")
    # Download whole report locally including code diff links
    mosspy.download_report(url, "submission/report/", connections=8)
    webbrowser.open('report.html', new = 2)
plagcheck()
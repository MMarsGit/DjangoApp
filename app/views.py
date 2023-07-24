from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import os
from collections import Counter

def getHistograms(file):
    #Open File
    histogramFile = open(file, "r")

    #Get grades array from File
    line = histogramFile.readline()
    gradesSet = line.split()

    #Get frequency
    count = Counter(gradesSet)
    print(count)

    bars = 10

    minAmount = 1
    maxAmount = 100
    string = ""
    divisions = maxAmount // bars
    currentMax = divisions
    currentMin = 0
    countDict = dict(count)

    barCount = 0
    for section in range(1, divisions+1):
        currentMax = divisions * section
        print(currentMax)
        string += "{0}-{1}|".format(currentMin+1, currentMax)

        #Add the number of items in this section
        for key in dict(count):
            print("key: " + key)
            if (int(key) <= currentMax) and (int(key) >= currentMin+1):
                barCount += countDict.get(key)
                print("barCount: " + str(barCount))

        #Add a * for each item in this section
        for num in range(barCount):
            string += "*"
        
        barCount = 0
        string += "\n"
        currentMin = currentMax

    print(string)       
    # Formatting
    # string = ""
    # while line:
    #     values = line.split()
    #     string += values[0] + "|"

    #     #print each *
    #     for num in range(0, int(values[1])):
    #         string += "*"
    #     string += "\n"
        
    #     line = histogramFile.readline()
        
    #     if not line:
    #         print(string)
    #         break
    return string

def home(request):
    print(settings.BASE_DIR)
    string = getHistograms(os.path.join(settings.BASE_DIR, "Grades.txt"))
    return HttpResponse(string, content_type="text/plain")

#Functions


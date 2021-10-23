from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

skills = ["Python (Tkinter, MySQL connector, Flask, and Django)",
          "Java (SE, Swing, JFrame, MySQL Connector)",
          "MySQL Database",
          "Git, Github",
          "Data Analysis, Machine Learning (Entry level)",
          "Android Development",
          "Linux essentials",
          "HTML, CSS, Bootstrap, and Adobe Photoshop",
          "Microsoft Office (Word, Excel, PowerPoint, Access)",
          "Self-learner, Teamwork, Problem Solving and Presentation Skills"]

Certificates = ["AI for Everyone, Coursera",
                "Data Analysis Challenger, ItIDA",
                "Data Science using Python, CEIT.",
                "Java Application Development, CEIT",
                "Android Programming, CEIT",
                "Complete Python Developer, Udemy, Kaggle",
                "Intro to Deep learning, Databases, MaharaTech ITI",
                "Best Java Track Head, Az_SENCS"]


def onlineCV_view(request):
    skill_set = calculateHalfIndex(skills)
    Certificate_set = calculateHalfIndex(Certificates)
    return render(request, 'onlinecv/onlineCV.html', {
        'first_half_range': skill_set[0],
        "second_half_range": skill_set[1],
        'first_half_range_cer': Certificate_set[0],
        "second_half_range_cer": Certificate_set[1],
    })


def calculateHalfIndex(list):
    half_index_list = len(list) // 2
    first_half_range_list = list[0:half_index_list]
    second_half_range_list = list[half_index_list: len(list)]
    return [first_half_range_list, second_half_range_list]

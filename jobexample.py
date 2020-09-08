#!/usr/bin/env python3

import plotly.graph_objects as go


class Sankey:

  def __init__(self,label,color,value):
    self.__fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(color = "white", width = 1.5),
          label = label,
          color = color
        ),
        link = dict(
          source = [0, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 7], 
          target = [4, 5, 4, 5, 4, 5, 4, 5, 6, 7, 8, 9],
          value = value,
      ))])
    self.__fig.update_layout(title_text="Job Search Sankey Diagram", font_size=10)

  def show(self):
    self.__fig.show()

APPLIED_LABEL = ["DevOps", "SW Developer", "Test Developer", "Other"]
APPLIED_COLOR = ["blue", "blue", "blue", "blue"]
APPLIED_VALUE = [8, 4, 2, 8, 4, 0, 1, 0, 8, 4, 3, 1]
STATUS_LABEL = ["No Response", "Responsed", "Rejected", "Interviewed","No Offer", "Offer"]
STATUS_COLOR = ["lime","grey","red","cyan","yellow","green"]

label = []
label.extend(APPLIED_LABEL)
label.extend(STATUS_LABEL)

color = []
color.extend(APPLIED_COLOR)
color.extend(STATUS_COLOR)

job = Sankey(label, color, APPLIED_VALUE)
job.show()

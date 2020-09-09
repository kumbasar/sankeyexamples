#!/usr/bin/env python3

import plotly.graph_objects as go
import json
import sys


class SankeyJob:
    def __init__(self,
                 title,
                 label,
                 color,
                 value,
                 linked_source,
                 linked_target):
        self.__fig = go.Figure(data=[go.Sankey(
            node=dict(
              pad=15,
              thickness=20,
              line=dict(color="white", width=1.5),
              label=label,
              color=color
            ),
            link=dict(
                      source=linked_source,
                      target=linked_target,
                      value=value,
                      ))])
        self.__fig.update_layout(title_text=title, font_size=10)

    def show(self):
        self.__fig.show()


label_name_list = []
label_color_list = []
lablel_value_list = []
applied_value = []
linked_source = []
linked_target = []
title = ""
try:
    with open('job.json') as json_file:

        data = json.load(json_file)
        title = data['name'] + ' - ' + data['date']

        rejected = 0
        interviewed = 0
        nooffer = 0
        offer = 0

        job_len = len(data['label'])
        linked_source = [i for i in range(job_len) for _ in range(2)]
        linked_source.extend([x+job_len for x in [1, 1, 3, 3]])

        linked_target = [_ + job_len for _ in range(2)] * job_len
        linked_target.extend(range(job_len+2,6+job_len))

        for label in data['label']:
            label_name_list.append(label['name'])
            label_color_list.append(label['color'])
            for status in label['status']:
                applied_value.append(status['noresponse'])
                applied_value.append(status['response'])
                rejected += status['rejected']
                interviewed += status['interviewed']
                nooffer += status['nooffer']
                offer += status['offer']

        applied_value.append(rejected)
        applied_value.append(interviewed)
        applied_value.append(nooffer)
        applied_value.append(offer)

        for status in data['status']:
            label_name_list.append(status['name'])
            label_color_list.append(status['color'])

except FileNotFoundError as e:
    sys.exit(e)

job = SankeyJob(title,
                label_name_list,
                label_color_list,
                applied_value,
                linked_source,
                linked_target)
job.show()

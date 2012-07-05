#!/usr/bin/python

# Copyright (c) 2011 British Broadcasting Corporation
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
from pylab import *

def topn(automated_tags, editorial_tags):
    # Values proposed in "A Large-Scale Evaluation of Acoustic and Subjective Music Similarity Measures":
    # alpha_r = 0.5 ** (1.0/3)
    # alpha_c = 0.5 ** (2.0/3)
    # Our values:
    alpha_r = 1 # ordering does not matter in reference list
    alpha_c = 0.8 # a tag at 20th position will be 0.01 (0.8 ** 20)
    total_score = 0
    for barcode in editorial_tags.keys():
        score = 0
        j = 0
        for tag in editorial_tags[barcode]:
            kj = 0
            for tag_data in automated_tags[barcode]:
                if tag_data['link'] == tag:
                    break
                kj += 1
            # What happens when j is not in B?
            if not kj == len(automated_tags[barcode]):
                score += (alpha_r ** j) * (alpha_c ** kj)
            j += 1
        norm = 0
        l = 0
        for tag in editorial_tags[barcode]:
            norm += (alpha_r * alpha_c) ** l
        score = score / norm
        print barcode + ': ' + str(score)
        total_score += score
    return total_score / len(editorial_tags.keys())

def nmissed(automated_tags, editorial_tags, n_measures = 100):
    scores = [ tag_data['score'] for barcode in automated_tags.keys() for tag_data in automated_tags[barcode] ] 
    highest_score = max(scores)
    lowest_score = min(scores)
    step = (highest_score - lowest_score) / n_measures
    current_score = lowest_score
    x, y = [], []
    for i in range(0, n_measures):
        avg_nmissed = 0.0
        for barcode in editorial_tags.keys():
            auto_tags = [ tag_data['link'] for tag_data in automated_tags[barcode] if tag_data['score'] >= current_score ] 
            spotted_tags = [ tag for tag in auto_tags if tag in editorial_tags[barcode] ]
            nmissed = len(spotted_tags) / float(len(editorial_tags[barcode]))
            avg_nmissed += nmissed
        avg_nmissed /= len(editorial_tags.keys())
        x += [ current_score ]
        y += [ avg_nmissed ]
        current_score += step
    scatter(x, y) 
    show()

def editorial_tags():
    editorial_tags = {}
    editorial_dir = os.path.join('data', 'editorial-data')
    for editorial_f in os.listdir(editorial_dir):
        barcode = editorial_f.split('_')[0]
        editorial_categories = json.load(open(os.path.join(editorial_dir, editorial_f)))['programme']['categories']
        for category in editorial_categories:
            # Is it a DBpedia tag?
            if category.has_key(u'sameAs') and category[u'sameAs']:
                if editorial_tags.has_key(barcode):
                    editorial_tags[barcode] += [ category[u'sameAs'] ]
                else:
                    editorial_tags[barcode] = [ category[u'sameAs'] ] 
    return editorial_tags 

def automated_tags():
    automated_tags = {}
    automated_dir = os.path.join('data', 'automated-tags')
    for automated_f in os.listdir(automated_dir):
        barcode = automated_f.split('.')[0]
        automated_tags[barcode] = json.load(open(os.path.join(automated_dir, automated_f)))
    return automated_tags

def run():
    editorial = editorial_tags()
    automated = automated_tags()
    print "Average TopN score: " + str(topn(automated, editorial))
    print "NMissed score for various score values: "
    nmissed(automated, editorial)

run()

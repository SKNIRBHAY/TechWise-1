# from django.shortcuts import render
# #from django.http import HttpResponse
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# import re
# import os
#
# def word_in_text(word, text):
#     word = word.lower()
#     text = text.lower()
#     match = re.search(word, text)
#     if match:
#         return True
#     return False
#
# def main(request, *args, **kwargs):
#     module_dir = os.path.dirname(__file__)  # get current directory
#     tweets_data_path = os.path.join(module_dir, 'twitter_data.txt')
#     tweets_data = []
#     tweets_file = open(tweets_data_path, "r")
#     for line in tweets_file:
#         try:
#             tweet = json.loads(line)
#             tweets_data.append(tweet)
#         except:
#             continue
#
#     print 'Structuring Tweets\n'
#     tweets = pd.DataFrame()
#     tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#     tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#
#     print 'Adding programming languages tags to the data\n'
#     tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
#     tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
#     tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))
#
#     print 'Analyzing tweets by programming language\n'
#     prg_langs = ['python', 'javascript', 'ruby']
#     tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]
#     print 'sjd'
#     x_pos = list(range(len(prg_langs)))
#     print 'sjd1'
#     width = 0.8
#     print 'sjdfinal'
#     ax = plt.subplot()
#     print 'sjd2'
#     plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
#     print 'sjd3'
#     ax.set_ylabel('Number of tweets', fontsize=15)
#     print 'sjd44'
#     ax.set_title('Ranking:', fontsize=10, fontweight='bold')
#     ax.set_xticks([p + 0.4 * width for p in x_pos])
#     ax.set_xticklabels(prg_langs)
#     print 'sjd4'
#     plt.grid()
#     plt.show()
#     # canvas = FigureCanvas(fig)
#     # response= HttpResponse(content_type='image/png')
#     # canvas.print_png(response)
#     # plt.matplotlib.pyplot.close(fig)
#     # return response
#
#     return render(request, 'analytics.html')
#

from django.shortcuts import render
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import os

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def main(request):

    print request.GET
    module_dir = os.path.dirname(__file__)  # get current directory
    tweets_data_path = os.path.join(module_dir, 'twitter_data.txt')
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print 'Structuring Tweets\n'
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)

    print 'Adding programming languages tags to the data\n'
    prg_langs = []
    tweets_by_prg_lang = []
    # For each value passed by user construct an array of languages and num of tweets
    for key, value in request.GET.iteritems():
      tweets[key] = tweets['text'].apply(lambda tweet: word_in_text(str(key), tweet))
      prg_langs.append(str(key))
      try:
        tweets_by_prg_lang.append(tweets[key].value_counts()[True])
      except:
        # Append 0 when no matching tweets are found
        tweets_by_prg_lang.append(0)

    print 'Analyzing tweets by programming language: First attempt\n'
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    jet = plt.get_cmap('jet')
    plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color=jet(np.linspace(0, 1.0, 6)))
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking:', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)

    plt.grid()
    #plt.show()
    plt.savefig("trending")

    return render(request, 'analytics.html')


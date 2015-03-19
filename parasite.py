#!/usr/bin/env python

from functions import *
import glob
import shutil

site_dir = '.'

with open('template', 'r') as t:
    template = t.read()

categories = ['about', 'code', 'math', 'physics', 'photography', 'other']
articles = {}
for folder in categories:
    os.chdir(folder)
    for subfolder in glob.glob("*"):
        if '.' not in subfolder:
            articles[subfolder] = folder
    os.chdir('..')

body = get_body('index.md')
source = make_source(template, 'index', body, 0, categories, articles, 'site')
write_source('index.html', source)

for folder in categories:
    folder_site_dir = os.getcwd() + '/' + folder
    os.chdir(folder)
    for filename in glob.glob("*"):
        if '.md' in filename:
            body = get_body(filename)
            source = make_source(template, 'index', body, 1, categories, articles,
                                 folder)
            write_source(folder_site_dir + '/index.html', source)
        elif os.path.isdir(filename):
            subfolder = filename
            os.chdir(subfolder)
            for subfilename in glob.glob("*"):
                if '.md' in subfilename:
                    date = subfilename.replace('.md', '')
                    body = get_body(subfilename)
                    source = make_source(template, subfolder, body, 2, categories,
                                         articles, folder)
                    write_source(folder_site_dir + '/' + subfolder
                                 + '/index.html', source)
            os.chdir('..')

    os.chdir('..')                      # go up to main site directory

print_tree('sballin.github.io', categories, articles)
print 'Size: %.2f MB' % (get_folder_size('.')/1000000.0)

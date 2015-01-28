#!/usr/bin/env python

from functions import *
import glob
import shutil

site_dir = '.'

with open('template', 'r') as t:
    template = t.read()

categories = []
articles = {}
for folder in glob.glob("_*"):
    os.chdir(folder)
    categories.append(folder.replace('_', ''))
    for subfolder in glob.glob("_*"):
        articles[subfolder.replace('_', '')] = folder.replace('_', '')
    os.chdir('..')
categories.sort()

body = get_body('index.md')
source = make_source(template, 'index', body, 0, categories, articles, 'site')
write_source('index.html', source)

for folder in glob.glob("_*"):         # content folders like _math
    folder_name = folder.replace('_', '')
    folder_site_dir = os.getcwd() + '/' + folder_name
    try: shutil.rmtree(folder_site_dir)
    except: pass
    os.mkdir(folder_site_dir)
    os.chdir(folder)
    for filename in glob.glob("*"):    # read all markdown files
        if '.md' not in filename and '_' not in filename:
            os.symlink('../' + folder + '/' + filename, '../' + folder_name + '/' + filename)
        elif '.md' in filename:
            body = get_body(filename)
            source = make_source(template, 'index', body, 1, categories, articles,
                                 folder_name)
            write_source(folder_site_dir + '/index.html', source)

    for subfolder in glob.glob("_*"):
        subfolder_name = subfolder.replace('_', '')
        os.mkdir(folder_site_dir + '/' + subfolder_name)
        os.chdir(subfolder)
        for filename in glob.glob("*"):
                if '.md' not in filename:
                    os.symlink('../../' + folder + '/' + subfolder + '/' + filename, '../../' + folder_name + '/' + subfolder_name + '/' + filename)
                else:
                    date = filename.replace('.md', '')
                    body = get_body(filename)
                    source = make_source(template, subfolder_name, body, 2, categories,
                                         articles, folder_name)
                    write_source(folder_site_dir + '/' + subfolder_name
                                 + '/index.html', source)
        os.chdir('..')

    os.chdir('..')                      # go up to main site directory

print_tree('sballin.github.io', categories, articles)
print 'Size: %.2f MB' % (get_folder_size('.')/1000000.0)

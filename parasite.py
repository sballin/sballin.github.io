#!/usr/bin/env python

import glob
import sys
import codecs
import markdown
import os
import collections
import re

# Hack to use UTF-8 instead of ASCII encoding
reload(sys)
sys.setdefaultencoding('UTF8')

# Define available scripts
mathJax = """<script type="text/x-mathjax-config">
MathJax.Hub.Config({tex2jax: { inlineMath: [ ["$", "$"] ], displayMath: [ ["$$","$$"] ]}, messageStyle: "none", "HTML-CSS": {scale: 90}});
    </script>
    <script src="{{top-path}}MathJax/MathJax.js?config=TeX-AMS_HTML-full"></script>"""
highlightjs = """<link rel="stylesheet" href="{{top-path}}github.min.css">
<script src="{{top-path}}highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>"""


def md_to_html(text):
    text = fancy_quotes(text)
    # text = prep_apostrophes(text)
    # Markdown extensions 'codehilite' and 'meta' also available.
    text = markdown.markdown(text, ['tables', 'footnotes', 'toc'])
    text = prep_latex(text)
    return text


def fancy_quotes(text):
    text = text.split("\n")
    for line in text:
        if not '    ' in line and not '`' in line:
            while "\"" in line:
                line = line.replace("\"", '&ldquo;', 1)
                line = line.replace("\"", '&rdquo;', 1)
            # fix quotes inside <div> tags
            while '=&ldquo;' in line:
                line = line.replace('=&ldquo;', "=\"", 1)
                line = line.replace('&rdquo;>', "\">", 1)
    text_out = ''
    for line in text:
        text_out += line.encode('utf-8') + "\n"
    return text_out


def prep_apostrophes(text):
    text = text.replace("'", '&rsquo;')
    return text


def prep_latex(text):
    text = text.replace('<p>$$', '<center>$$')
    text = text.replace('$$</p>', '$$</center>')

    # Fix over-eager Markdown formatting inside LaTeX expressions
    text = re.sub(r'\$\$(.*)<em>(.*)\$\$', r'$$\1_\2$$', text)
    text = re.sub(r'\$\$(.*)</em>(.*)\$\$', r'$$\1_\2$$', text)
    text = re.sub(r'\$(.*)<em>(.*)\$', r'$\1_\2$', text)
    text = re.sub(r'\$(.*)</em>(.*)\$', r'$\1_\2$', text)
    return text


def is_comment(line):
    if '<!--' and '-->' in line:
        return 1
    return 0


def add_scripts(body, source):
    script_mark = '\n{{scripts}}'
    if '$$' in body or '\\(' in body or '\begin{align}' in body:
        source = source.replace(script_mark, mathJax + script_mark)
    if '<code>' in body:
        source = source.replace(script_mark, highlightjs + script_mark)
    source = source.replace(script_mark, '')
    return source


def add_content(body, template):
    return template.replace('{{content}}', body)


def add_side(source, path, tree):
    folder_mark = '{{folders}}'
    up = top(path)
    category = path.split('/', 1)[0]
    for cat in tree.keys():
        if cat != category or len(tree[category]) == 0:
            source = source.replace(folder_mark, '<div class="category"><a class="category-name" href="%s%s">%s</a></div>\n%s' % (up, cat, cat, folder_mark))
        else:
            source = source.replace(folder_mark, '<div class="category">\n<a class="category-name" href="%s%s">%s</a>\n<div class="category-article-list">\n%s' % (up, cat, cat, folder_mark))
            for article_name in tree[category]:
                pretty_article_name = article_name.replace('-', ' ')
                source = source.replace(folder_mark, '<a class="category-article" href="%s%s/%s">%s</a>\n%s' % (up, category, article_name, pretty_article_name, folder_mark))
            source = source.replace(folder_mark, '</div>\n</div>' + folder_mark)
    source = source.replace(folder_mark, '')
    source = source.replace('</div>\n\n</div>', '</div>\n</div>', 1)
    return source


def top(path):
    """
    Return path to top directory given article path.
    """
    if path.count('/') == 1:
        return '../../'
    elif path != '.':
        return '../'
    else:
        return './'


def write_source(path, tree, template):
    if path.count('/') == 1:
        title = path.split('/')[1].replace('-', ' ')
    elif path == '.':
        title = 'home'
    else:
        title = path
    body = codecs.open(path + '/index.md', 'r', encoding='utf-8').read()
    body = md_to_html(body)
    source = add_content(body, template)
    source = add_scripts(body, source)
    source = add_side(source, path, tree)
    source = source.replace('{{top-path}}', top(path)) \
                   .replace('{{title}}', title)
    codecs.open(path + '/index.html', 'w', encoding='utf-8').write(source)


def get_folder_size(p):
    """
    Copied from
    http://stackoverflow.com/questions/1392413/calculating-a-directory-size-using-python
    """
    from functools import partial
    prepend = partial(os.path.join, p)
    return sum([(os.path.getsize(f) if os.path.isfile(f) else get_folder_size(f))
               for f in map(prepend, os.listdir(p))])


def print_tree(tree):
    for folder in tree.keys():
        print '%s' % folder
        for item in tree[folder]:
            print '   %s' % item
        print


if __name__ == '__main__':
    # Read template to apply to pages written in Markdown
    template = open('template', 'r').read()

    # Folders that should show up in the sidebar and whose articles should be
    # formatted
    folders = ['about', 'code', 'math', 'physics', 'photos', 'other']

    # Make tree of all article folders
    tree = collections.OrderedDict()
    for folder in folders:
        tree[folder] = []
        for path in glob.glob(folder + "/*"):
            # If it's probably a folder containing an article, add article name
            # to tree
            if '.' not in path:
                tree[folder].append(path.split('/', 1)[1])

    # Write home page index
    write_source('.', tree, template)

    # Scan category folders for Markdown to translate to HTML
    for folder in tree.keys():
        # Write category folder indices
        write_source(folder, tree, template)
        # Write article folder index if an index.md file is present
        for article in tree[folder]:
            path = folder + '/' + article
            if len(glob.glob(path + '/index.md')) == 1:
                write_source(path, tree, template)

    # Print website info to terminal
    print_tree(tree)
    print 'Size: %.2f MB' % (get_folder_size('.')/1000000.0)

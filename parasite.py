import os
import collections
import re
import glob
import markdown
import json
import time
import datetime

# Define available scripts
mathJax = """<script type="text/x-mathjax-config">
MathJax.Hub.Config({tex2jax: { inlineMath: [ ["$", "$"] ], displayMath: [ ["$$","$$"] ]}, messageStyle: "none", "HTML-CSS": {scale: 90}});
</script>
<script src="{{top-path}}/MathJax/MathJax.js?config=TeX-AMS_HTML-full"></script>"""
highlightjs = """<link rel="stylesheet" href="{{top-path}}/github.min.css">
<script src="{{top-path}}/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>"""

class Article:
    def __init__(self, path):
        self.path = path

        # If it's an article, title is path without category and hyphens to
        # spaces. If path is a category folder, its title is the category
        if path.count('/') == 1:
            self.url_title = path.split('/')[1]
        elif path == '.':
            self.url_title = 'home'
        else:
            self.url_title = path

        self.hidden = (self.url_title[0] == '_')

        # Try to read article markdown and possibly included properties
        try:
            self.markdown = open(path + '/index.md', 'r',
                                 encoding='utf-8').read()
        except:
            self.markdown = None

        self.learn_properties()

        # Look for custom markdown to display in an article feed
        try:
            self.feed_markdown = open(path + '/feed.md', 'r',
                                      encoding='utf-8').read()
        except:
            try:
                self.feed_markdown = self.markdown.split('<!--  -->')[0]
            except:
                self.feed_markdown = self.markdown

    def learn_properties(self):
        if self.markdown:
            properties = re.findall('<!-- {(.*)} -->', self.markdown,
                                    flags=re.DOTALL)
            self.markdown = re.sub('<!-- {(.*)} -->\n\n', '', self.markdown,
                                   flags=re.DOTALL)
            if properties:
                properties = '{%s}' % properties[0]
                properties = json.loads(properties)

        try:
            self.date_written = time.mktime(datetime.datetime.strptime(
                                            properties['date_written'],
                                            "%b %y").timetuple())
        except:
            self.date_written = os.stat(self.path).st_birthtime

        try:
            self.full_title = properties['full_title']
        except:
            self.full_title = self.url_title.replace('-', ' ')

    def page_html(self, tree, template):
        body = md_to_html(self.markdown)
        body += '<p><em>This page was written in %s.</em></p>' % datetime.datetime.fromtimestamp(int(self.date_written)).strftime("%B %Y")
        source = wrap_in_template(body, template)
        source = add_scripts(body, source)
        source = add_sidebar(source, self.path, tree)
        source = source.replace('{{top-path}}', top(self.path)) \
                       .replace('{{title}}', self.full_title) \
                       .replace('{{article-path}}', self.path)
        return source

    def write_html(self, tree, template):
        source = self.page_html(tree, template)
        open(self.path + '/index.html', 'w', encoding='utf-8').write(source)


class Feed:
    def __init__(self, path, tree):
        self.path = path
        self.tree = tree
        if path == '.':
            self.title = 'home'
            self.articles = [a for a_list in tree.values() for a in a_list]
            self.articles.sort(key=lambda x: x.date_written, reverse=True)
            self.articles = self.articles[:8]
        else:
            self.title = path
            self.articles = tree[path]

        self.articles = [a for a in self.articles if not a.hidden]

    def write_html(self, template):
        article_separator = '\n</div>\n<div id="article">\n'
        feed_body = ''
        for i, article in enumerate(self.articles):
            if article.markdown:
                article.feed_markdown = article.feed_markdown.replace(
                                        '{{article-path}}', article.path)
                html = md_to_html(article.feed_markdown)
                html = re.sub('<a (.*)"fa fa-github"></i></a>', '', html)
                html = re.sub('<h1 (.*)>(.*)</h1>', r'<h1 \1><a class="article-title" href="%s/%s">\2</h1></a>' % (top(self.path), article.path), html)
                html += '\n<p><em><a class="gray" href="%s/%s">Continue reading...' \
                        '</a></em></p>' % (top(self.path), article.path)
                feed_body += html
                if i < len(self.articles) - 1:
                    feed_body += article_separator
        source = wrap_in_template(feed_body, template)
        source = add_scripts(feed_body, source)
        source = add_sidebar(source, self.path, self.tree)
        source = source.replace('{{top-path}}', top(self.path))
        source = source.replace('{{title}}', self.title)
        open(self.path + '/index.html', 'w', encoding='utf-8').write(source)


def md_to_html(text):
    # Markdown extensions 'codehilite' and 'meta' also available.
    text = markdown.markdown(text, ['tables', 'footnotes', 'toc'])
    text = prep_latex(text)
    return text


def prep_latex(text):
    # Center all entire-line LaTeX expressions
    text = text.replace('<p>$$', '<center>$$')
    text = text.replace('$$</p>', '$$</center>')

    # Undo Markdown's mistaken formatting of the LaTeX _ symbol
    text = re.sub(r'\$\$(.*)<em>(.*)\$\$', r'$$\1_\2$$', text)
    text = re.sub(r'\$\$(.*)</em>(.*)\$\$', r'$$\1_\2$$', text)
    text = re.sub(r'\$(.*)<em>(.*)\$', r'$\1_\2$', text)
    text = re.sub(r'\$(.*)</em>(.*)\$', r'$\1_\2$', text)

    return text


def add_scripts(body, source):
    script_mark = '{{scripts}}'
    if '$$' in body or '\\(' in body or '\begin{align}' in body:
        source = source.replace(script_mark, mathJax + script_mark)
    if '<code>' in body:
        source = source.replace(script_mark, highlightjs + script_mark)
    source = source.replace(script_mark, '')
    return source


def wrap_in_template(body, template):
    return template.replace('{{content}}', body)


def add_sidebar(source, path, tree):
    cat_placeholder = '{{categories}}'
    up = top(path)
    category = path.split('/', 1)[0]
    for cat in tree.keys():
        if cat != category or not tree[category]:
            source = source.replace(cat_placeholder, '<div class="category"><a class="category-name" href="%s/%s">%s</a></div>\n%s' % (up, cat, cat, cat_placeholder))
        else:
            source = source.replace(cat_placeholder, '<div class="category">\n<a class="category-name" href="%s/%s">%s</a>\n<div class="category-article-list">\n%s' %
                                    (up, cat, cat, cat_placeholder))
            for article in tree[category]:
                source = source.replace(cat_placeholder, '<a class="category-article" href="%s/%s/%s">%s</a>\n%s' % (up, category, article.url_title, article.full_title, cat_placeholder))
            source = source.replace(cat_placeholder, '</div>\n</div>' + cat_placeholder)
    source = source.replace(cat_placeholder, '')
    source = source.replace('</div>\n\n</div>', '</div>\n</div>', 1)
    return source


def top(path):
    """Return path to top directory given article path."""
    if path.count('/') == 1:
        return '../..'
    elif path != '.':
        return '..'
    else:
        return '.'


def print_tree(tree):
    for category in tree.keys():
        print('%s' % category)
        for item in tree[category]:
            print('   %s' % item.url_title)


def build_website():
    # Read template to apply to pages written in Markdown
    template = open('template', 'r').read()

    # Folders that should show up in the sidebar and whose articles should be
    # formatted
    categories = ['about', 'projects', 'science', 'other']

    # Make tree of all articles
    tree = collections.OrderedDict()
    for category in categories:
        tree[category] = []

        # Add articles inside categories to tree, ignoring non-folders.jpg
        for path in glob.glob(category + "/*"):
            article = Article(path)
            if '.' not in path and not article.hidden:
                tree[category].append(article)
        tree[category].sort(key=lambda x: x.date_written, reverse=True)

    # Write home page index
    Feed('.', tree).write_html(template)

    # Scan category folders for Markdown to translate to HTML
    for category in categories:
        if os.path.isfile(category + '/index.md'):
            Article(category).write_html(tree, template)
        else:
            Feed(category, tree).write_html(template)

        for article in tree[category]:
            # If standard article with index.md, write source
            if article.markdown:
                article.write_html(tree, template)

    # Print website info to terminal
    print_tree(tree)


if __name__ == '__main__':
    build_website()


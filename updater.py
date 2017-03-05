#!/usr/bin/python

import json
# pip3 install requests
import requests

import sys
from os import listdir
from os.path import isfile, join
from datetime import date, timedelta


def compare_dates(gh_date, d):
    if gh_date is None or len(gh_date) < 1:
        return False
    gh_date = gh_date.split('T')[0].split('-')
    year = int(gh_date[0])
    month = int(gh_date[1])
    day = int(gh_date[2])

    return date(year, month, day) >= d


def get_page_number(url):
    parts = url.split('?')[-1].split('&')
    for part in parts:
        if part.startswith('page='):
            try:
                return int(part.split('=')[-1])
            except Exception:
                return 1
    return 1


def get_next_pages_url(link):
    parts = link.split(',')
    subs = []
    for part in parts:
        subs.append(part.split(';'))
    next_page_url = ''
    last_page_url = ''
    for sub in subs:
        if len(sub) != 2:
            continue
        if sub[1].ends_with('"next"'):
            next_page_url = sub[0][1:-1]
        elif sub[1].ends_with('"last"'):
            last_page_url = sub[0][1:-1]
    return next_page_url, last_page_url


def filter_data(content, to_return):
    total = 0
    if content.__class__.__name__ == 'dict':
        return
    for pr in content:
        if 'closed_at' in pr and pr['closed_at'] is not None:
            if compare_dates(pr['closed_at'], max_date):
                to_return.append(pr)
                total += 1
        elif 'updated_at' in pr:
            if compare_dates(pr['updated_at'], max_date):
                to_return.append(pr)
                total += 1


# This function tries to get as much github data as possible by running
# "parallel" requests.
def get_all_contents(url, state, max_date, token=None, recursive=True):
    headers = {
        'User-Agent': 'GuillaumeGomez',
        'Accept': 'application/vnd.github.v3+json',
    }
    params = {'sort': 'updated', 'state': state, 'per_page': 100,
              'direction': 'desc'}
    if token is not None:
        # Authentication to github.
        headers['Authorization'] = 'token %s' % token
    res = requests.get(url, headers=headers, params=params)
    if res.status_code != 200:
        if res.status_code == 403:
            # We reached the rate limit.
            if ('X-RateLimit-Limit' in res.headers and
                    'X-RateLimit-Remaining' in res.headers and
                    'X-RateLimit-Reset' in res.headers):
                raise Exception("Github rate limit exceeded...\n"
                                "X-RateLimit-Limit: %s\n"
                                "X-RateLimit-Remaining: %s\n"
                                "X-RateLimit-Reset: %s" %
                                (res.headers['X-RateLimit-Limit'],
                                 res.headers['X-RateLimit-Remaining'],
                                 res.headers['X-RateLimit-Reset']))
        raise Exception("Get request failed: '%s', got: [%s]: %s"
                        % (url, res.status_code, str(res.content)))
    content = res.json()
    to_return = []
    filter_data(content, to_return)
    if 'Link' not in res.headers or not recursive:
        # If there are no other pages, we can return the current content.
        if max_date is None:
            return content
        return to_return

    h = res.headers['Link']
    if h is None or len(h) != 1:
        return content

    next_page_url, last_page_url = get_next_pages_url(h)
    if len(last_page_url) < 10 or len(next_page_url) < 10:
        return content
    next_page = get_page_number(next_page_url)
    last_page = get_page_number(last_page_url)

    urls = [next_page_url]
    to_replace = "page=%s" % next_page
    next_page += 1
    while next_page <= last_page:
        requests.get(next_page_url.replace("&%s" % to_replace,
                                           "&page=%s" % next_page)
                                  .replace("?%s" % to_replace,
                                           "?page=%s" % next_page), headers=headers)
        if res.status_code != 200:
            break
        content = res.json()
        if filter_data(content, to_return) != len(content):
            break
        next_page += 1
    return to_return


class Github:
    def __init__(self, token):
        self.token = token

    def get_pull(self, repo_name, repo_owner, pull_number):
        return Repository(self.token, repo_name, repo_owner).get_pull(pull_number)

    def get_pulls(self, repo_name, repo_owner, state, max_date):
        return Repository(self.token, repo_name, repo_owner).get_pulls(state, max_date)


class Repository:
    def __init__(self, token, name, owner):
        self.name = name
        self.token = token
        self.owner = owner

    def get_pulls(self, state, max_date):
        prs = get_all_contents('https://api.github.com/repos/%s/%s/pulls'
                               % (self.owner, self.name), state, max_date,
                               token=self.token)
        if prs is None:
            return []
        return [PullRequest(self.token, self.name, self.owner,
                            pr['number'],
                            pr['base']['ref'], pr['head']['ref'],
                            pr['head']['sha'], pr['title'],
                            pr['user']['login'], pr['state'],
                            pr['merged_at'], pr['closed_at']) for pr in prs]

    def get_pull(self, pull_number):
        pr = get_all_contents('https://api.github.com/repos/%s/%s/pulls/%s'
                              % (self.owner, self.name, pull_number),
                              'all', None,
                              token=self.token)
        if pr is None:
            return None
        return PullRequest(self.token, self.name, self.owner,
                           pull_number,
                           pr['base']['ref'], pr['head']['ref'],
                           pr['head']['sha'], pr['title'],
                           pr['user']['login'], pr['state'],
                           pr['merged_at'], pr['closed_at'])


# Represent a Github Pull Request.
class PullRequest:
    def __init__(self, token, repo_name, repo_owner,
                 pull_number, target_branch, from_branch, head_commit,
                 title, author, open_state, merged_at, closed_at):
        self.repo_name = repo_name
        self.token = token
        self.repo_owner = repo_owner
        self.number = pull_number
        self.target_branch = target_branch
        self.from_branch = from_branch
        self.head_commit = head_commit
        self.title = title
        self.author = author
        self.open_state = open_state
        self.merged_at = merged_at
        if self.merged_at is None:
            self.merged_at = ''
        self.closed_at = closed_at
        if self.closed_at is None:
            self.closed_at = ''

    def get_url(self):
        return ("https://github.com/%s/%s/pull/%s"
                % (self.repo_owner, self.repo_name, self.number))


def clear_msg(msg):
    if msg.startswith(', '):
        msg = msg[2:]
    elif msg.startswith(' and '):
        msg = msg[5:]
    return "%s]" % msg.strip()


def create_msg(title):
    title = title.split()
    return "%s [%s]" % (title[0][:1].lower() + title[0][1:], " ".join(title[1:]))


def check_if_not_in(elems, url):
    for pr in elems:
        if pr['url'] == url:
            return False
    return True


def get_prs_display(pr_list):
    pos = 0
    out = ''
    while pos < len(pr_list):
        ppos = pos + 1
        prs = [pr_list[pos]]
        while ppos < len(pr_list):
            if pr_list[ppos]['author'] == pr_list[pos]['author']:
                prs.append(pr_list[ppos])
                pr_list.pop(ppos)
                continue
            ppos += 1
        author = pr_list[pos]['author']
        last = ''
        if len(prs) > 1:
            last = "%s(%s)" % (prs[-1]['message'], prs[-1]['url'])
            prs.pop()
        prs = ["%s(%s)" % (pr['message'], pr['url']) for pr in prs]
        out += '* [@%s](https://github.com/%s) %s%s.\n' % (author,
                                                           author,
                                                           ", ".join(prs),
                                                           (" and %s" % last) if len(last) > 0 else "")
        pos += 1
    return out


def get_next_meeting(d):
    months = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}
    end = 'th'
    if d.day != 11 and d.day != 12 and d.day != 13:
        if d.day % 10 == 1:
            end = 'st'
        elif d.day % 10 == 2:
            end = 'nd'
        elif d.day % 10 == 3:
            end = 'rd'
    return '%s%s of %s %s' % (d.day, end, months[d.month], d.year)

if len(sys.argv) < 2:
    sys.stderr.write('Need a token argument.\n')
    sys.exit(1)
token = sys.argv[1]

file_path = None
file_num = None

try:
    for entry in [join('_posts', f) for f in listdir('_posts') if isfile(join('_posts', f))]:
        parts = entry.split('-this-week-in-rust-docs-')
        if len(parts) != 2:
            continue
        try:
            value = int(parts[1].replace(".md", ""))
            if file_num is not None and value < file_num:
                continue
            file_num = value
            file_path = entry
        except Exception:
            continue
except Exception as e:
    sys.stderr.write('Failed to read "_posts" folder: %s\n' % e)
    sys.exit(1)

if file_path is None:
    sys.stderr.write('No post file found\n')
    sys.exit(1)

sys.stdout.write('Taking last this week in rust docs post: %s\n' % file_path)

from_date = file_path.replace("_posts/", "").split('-this-week-in-rust')[0].replace(".md", "").split("-")
if len(from_date) != 3:
    sys.stderr.write('No date found in file name: "%s"\n' % file_path)
    sys.exit(1)
year = int(from_date[0])
month = int(from_date[1])
day = int(from_date[2])
max_date = date(year, month, day)
if max_date == date.today():
    sys.stderr.write('Weird, the file date corresponds to today... Halting here just in case\n')
    sys.exit(1)
git = Github(token)

content = ''
try:
    with open(file_path, 'r') as f:
        content = f.read()
except Exception as e:
    sys.stderr.write('Error while reading "%s": %s\n' % (file_path, e))
    sys.exit(1)

content = content.split("Hello and welcome to *This Week in Rust Docs*!\n\n")[1]
today = date.today()

out = '---\nlayout: post\ntitle: This Week in Rust Docs %s\ndate: %s-%s-%s\n---\n\n' % (
        file_num + 1, today.year, today.month, today.day)
out += 'Hello and welcome to *This Week in Rust Docs*!\n\n'

content = content.split('# Waiting for merge\n\n')
out += content[0]
content = content[1].split('# Recent doc contributions\n\n')

# getting all previously waiting for merge PRs
sys.stdout.write('Getting previously waiting for merge PRs\n')
waiting_prs = []
for line in content[0].split('\n'):
    if line.startswith('* [@'):
        entries = line.split(')')
        author = entries[0][4:].split('](h')[0]
        for entry in entries[1:]:
            parts = entry.split('](h')
            if len(parts) < 2:
                continue
            waiting_prs.append({'author': author, 'url': "h{}".format(parts[1]), 'message': clear_msg(parts[0])})

merged_prs = []
pos = 0
# checking their status
sys.stdout.write('Checking previously waiting for merge PRs\' status\n')
while pos < len(waiting_prs):
    sys.stdout.write('-> Checking %s...\n' % waiting_prs[pos]['url'].split('/')[-1])
    ret = git.get_pull("rust", "rust-lang", waiting_prs[pos]['url'].split('/')[-1])
    if ret is not None:
        if ret.open_state == 'closed':
            if len(ret.merged_at) > 0:
                merged_prs.append(waiting_prs[pos])
            waiting_prs.pop(pos)
            continue
    pos += 1
sys.stdout.write('Getting merged PRs...\n')
closed_prs = git.get_pulls('rust', 'rust-lang', 'closed', max_date)
for pr in closed_prs:
    if compare_dates(pr.merged_at, max_date) and check_if_not_in(merged_prs, pr.get_url()):
        merged_prs.append({'author': pr.author,
                           'url': pr.get_url(),
                           'message': create_msg(pr.title)})

sys.stdout.write('Getting opened PRs...\n')
opened_prs = git.get_pulls('rust', 'rust-lang', 'open', max_date)
to_keep = []
for waiting in waiting_prs:
    to_keep.append(waiting)
for pr in opened_prs:
    if check_if_not_in(to_keep, opened_prs[pos].get_url()):
        to_keep.append({'author': pr.author,
                        'url': pr.get_url(),
                        'message': create_msg(pr.title)})
opened_prs = to_keep

d = {0: 2,
     1: 1,
     2: 0,
     3: 6,
     4: 5,
     5: 4,
     6: 3}[today.weekday()]
d = today + timedelta(days=d)

sys.stdout.write('Formatting all these data...\n')
out += '# Waiting for merge\n\n%s\n' % get_prs_display(opened_prs)
out += '# Recent doc contributions\n\n%s\n' % get_prs_display(merged_prs)
out += '# Meetings\n\nNext meeting will be on Wednesday %s at 20:00 GMT on ' % get_next_meeting(d)
out += '#rust-docs channel on irc.mozilla.org. Feel free to come!\n'

filename = '_posts/%s-%s-%s-this-week-in-rust-docs-%s.md' % (today.year, today.month, today.day, file_num + 1)
sys.stdout.write('Writing all output in %s...\n' % filename)
try:
    with open(filename, 'w') as f:
        f.write(out)
except Exception as e:
    sys.stderr.write('Failed to create "%s": %s\n\nCurrent output:\n%s', filename, e, out)
    sys.exit(1)
sys.stdout.write('All good!\n')

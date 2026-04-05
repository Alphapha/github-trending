# coding:utf-8

import datetime
import codecs
import requests
import os
import time
import re
from pyquery import PyQuery as pq


def git_add_commit_push(date, filename):
    cmd_git_add = 'git add {filename}'.format(filename=filename)
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)


def createMarkdown(date, filename):
    with open(filename, 'w') as f:
        f.write("## " + date + "\n")


def scrape(language, filename):
    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }

    url = 'https://github.com/trending/{language}'.format(language=language)
    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200
    
    d = pq(r.content)
    items = d('div.Box article.Box-row')

    # codecs to solve the problem utf-8 codec like chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n#### {language}\n\n'.format(language=language))
        f.write('| 排名 | 项目 | 描述 | 今日 Star | 总 Star | Fork | 语言 |\n')
        f.write('|------|------|------|---------|---------|------|------|\n')

        rank = 0
        for item in items:
            rank += 1
            i = pq(item)
            
            repo_link = i.find(".lh-condensed a").eq(0)
            repo_path = repo_link.attr("href") if repo_link else ""
            
            if repo_path:
                path_parts = repo_path.strip('/').split('/')
                owner = path_parts[0] if len(path_parts) > 0 else "Unknown"
                title = path_parts[1] if len(path_parts) > 1 else "Unknown"
            else:
                owner = "Unknown"
                title = "Unknown"
            
            repo_url = "https://github.com" + repo_path if repo_path else ""
            
            description = i("p.col-9").text().strip()
            description = description.replace('\n', ' ').replace('|', '-')
            
            star_elements = i.find('a[href$="stargazers"]')
            total_stars = '0'
            today_stars = '0'
            if star_elements and len(star_elements) > 0:
                star_text = pq(star_elements[0]).text().strip()
                total_stars = star_text.replace(',', '')
            
            metadata_elem = i.find('.f6.color-fg-muted.mt-2')
            today_stars = '0'
            if metadata_elem and len(metadata_elem) > 0:
                metadata_text = pq(metadata_elem[0]).text()
                match = re.search(r'(\d[\d,]*) stars today', metadata_text)
                if match:
                    today_stars = match.group(1).replace(',', '')
            
            fork_elements = i.find('a[href$="forks"]')
            forks = '0'
            if fork_elements and len(fork_elements) > 0:
                forks = pq(fork_elements[0]).text().strip().replace(',', '')
            
            lang_elem = i.find('span[itemprop="programmingLanguage"]')
            lang = lang_elem.text().strip() if lang_elem and len(lang_elem) > 0 else 'N/A'
            
            f.write(u"| {rank} | [{owner}/{title}]({url}) | {desc} | {today_stars} | {total_stars} | {forks} | {lang} |\n".format(
                rank=rank,
                owner=owner,
                title=title,
                url=repo_url,
                desc=description,
                today_stars=today_stars,
                total_stars=total_stars,
                forks=forks,
                lang=lang
            ))
        
        f.write('\n')


def job():
    strdate = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = '{date}.md'.format(date=strdate)

    # create markdown file
    createMarkdown(strdate, filename)

    # write markdown
    scrape('python', filename)
    scrape('swift', filename)
    scrape('javascript', filename)
    scrape('go', filename)
    scrape('php', filename)
    scrape('ruby', filename)
    scrape('java', filename)
    scrape('c', filename)
    scrape('cpp', filename)
    scrape('c#', filename)
    scrape('typescript', filename)
    scrape('rust', filename)
    scrape('swift', filename)

    # git add commit push
    # git_add_commit_push(strdate, filename)


if __name__ == '__main__':
    job()

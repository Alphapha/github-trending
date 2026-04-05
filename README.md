# GitHub Trending(Python)


## Intro
Tracking the most popular Github repos, updated daily(Python version)

## Features

- 📊 表格化展示，信息更直观
- ⭐ 显示总 Star 数
- 📈 显示今日 Star 增长数
- 🍴 显示 Fork 数量
- 💻 显示编程语言类型
- 🏆 显示项目排名
- 🔗 提供项目链接直达

## Output Format

生成的 Markdown 文件包含以下信息：

| 字段 | 说明 |
|------|------|
| 排名 | 项目在当日榜单中的排名 |
| 项目 | 项目名称（owner/repo 格式） |
| 描述 | 项目简介 |
| 今日 Star | 当日新增 Star 数 |
| 总 Star | 项目累计 Star 总数 |
| Fork | 项目 Fork 数量 |
| 语言 | 项目主要编程语言 |

## Run

You need install `pyquery` & `requests`

```bash
  $ git clone https://github.com/bonfy/github-trending.git
  $ cd github-trending
  $ pip install -r requirements.txt
  $ python scraper.py
```

## Advance

A better place to use the script is in VPS

* You should have a VPS first, and then you should Add SSH Keys of your VPS to Github

* Then you can run the code in VPS

Thus the code will run never stop

## Special Day

- [2017-03-29](https://github.com/bonfy/github-trending/blob/master/2017/2017-03-29.md) - my repo [qiandao](https://github.com/bonfy/qiandao) record by github-trending(Python)
- [2018-09-27](https://github.com/bonfy/github-trending/blob/master/2018/2018-09-27.md)/[2018-10-09](https://github.com/bonfy/github-trending/blob/master/2018/2018-10-09.md) - my repo [go-mega](https://github.com/bonfy/go-mega) record by github-trending(Go)

## Sponsor

![support](https://raw.githubusercontent.com/bonfy/image/master/global/sponsor.jpg)

## License

MIT

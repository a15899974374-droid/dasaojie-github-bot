#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 每日热门项目抓取脚本
每天自动抓取数据分析和结构方程模型相关的热门项目
"""

import requests
import json
import os
from datetime import datetime
import time

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

KEYWORDS = [
    "data analysis",
    "structural equation modeling",
    "SEM",
    "AMOS",
    "SmartPLS",
    "statistics",
    "quantitative research"
]

def get_headers():
    headers = {"Accept": "application/vnd.github.v3+json"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
    return headers

def search_repositories(query, sort="stars", order="desc", per_page=10):
    url = f"{GITHUB_API}/search/repositories"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page
    }
    try:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"搜索失败: {response.status_code}")
            return []
    except Exception as e:
        print(f"请求异常: {e}")
        return []

def generate_markdown_report(repos_by_keyword):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    weekday = ["周一","周二","周三","周四","周五","周六","周日"][now.weekday()]

    md = f"# GitHub 数据分析热门项目日报\n\n"
    md += f"**日期**: {date_str} ({weekday})  \n"
    md += f"**生成时间**: {now.strftime('%Y-%m-%d %H:%M:%S')}  \n\n---\n\n"

    for keyword, repos in repos_by_keyword.items():
        md += f"\n## 🔥 {keyword} 相关热门项目\n\n"
        if not repos:
            md += "> 暂无相关项目数据\n\n"
            continue
        for i, repo in enumerate(repos, 1):
            md += f"### {i}. [{repo['name']}]({repo['html_url']})\n\n"
            md += f"- **仓库**: `{repo['full_name']}`\n"
            md += f"- **⭐ Stars**: {repo['stargazers_count']:,}\n"
            md += f"- **🍴 Forks**: {repo['forks_count']:,}\n"
            md += f"- **📝 描述**: {repo.get('description', '暂无描述')}\n"
            md += f"- **🔤 语言**: {repo.get('language', '未知')}\n"
            md += f"- **📅 最后更新**: {repo['updated_at'][:10]}\n\n"
            if repo.get('topics'):
                md += f"- **🏷️ 标签**: {', '.join(repo['topics'])}\n\n"
            md += "---\n\n"

    md += f"\n> 📊 数据来源: GitHub API  \n"
    md += f"> 🤖 自动生成: 每天晚上 22:00 自动更新\n"
    return md

def main():
    print("开始抓取 GitHub 热门项目...")
    repos_by_keyword = {}

    for keyword in KEYWORDS:
        print(f"正在搜索: {keyword}")
        repos = search_repositories(keyword)
        repos_by_keyword[keyword] = repos
        time.sleep(2)

    print("生成报告...")
    markdown_content = generate_markdown_report(repos_by_keyword)

    output_dir = "github-daily-report"
    os.makedirs(output_dir, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = os.path.join(output_dir, f"{date_str}.md")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"报告已保存: {output_file}")

    readme_file = os.path.join(output_dir, "README.md")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"README 已更新: {readme_file}")
    return output_file

if __name__ == "__main__":
    main()

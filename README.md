# 大师姐 GitHub 每日热门项目机器人 🤖

每天晚上 22:00 自动抓取 GitHub 上与**数据分析和结构方程模型**相关的热门项目，并生成总结报告自动推送到仓库。

## ✨ 功能特点

- 🕙 **定时抓取**: 每天北京时间 22:00 自动运行
- 📊 **精准搜索**: 聚焦数据分析和结构方程模型领域
- 📝 **自动报告**: 生成 Markdown 格式的每日报告
- 🔄 **自动更新**: 自动提交并推送到仓库
- 📂 **历史存档**: 所有历史报告保存在 `github-daily-report/` 目录

## 📋 搜索关键词

脚本会自动搜索以下关键词相关的热门项目：

- `data analysis` - 数据分析
- `structural equation modeling` - 结构方程模型
- `SEM` - 结构方程模型缩写
- `AMOS` - AMOS 软件
- `SmartPLS` - SmartPLS 软件
- `statistics` - 统计学
- `quantitative research` - 定量研究

## 🚀 使用方法

### 查看每日报告

每日报告会自动生成在 `github-daily-report/` 目录：

- **当日报告**: `github-daily-report/YYYY-MM-DD.md`
- **最新汇总**: `github-daily-report/README.md`

### 手动触发运行

1. 进入仓库的 **Actions** 标签页
2. 选择 **GitHub 每日热门项目抓取**
3. 点击 **Run workflow**
4. 选择分支（通常是 `main`）
5. 点击 **Run workflow** 确认

## 📊 报告格式

每天生成的报告包含：

- 📅 日期和星期
- 🔥 每个关键词下的热门项目列表
- ⭐ Stars 数量
- 🍴 Forks 数量
- 📝 项目描述
- 🔤 主要编程语言
- 📅 最后更新时间
- 🏷️ 项目标签

## 🛠️ 自定义配置

### 修改抓取时间

编辑 `.github/workflows/daily-fetch.yml`，修改 `cron` 表达式：

```yaml
# 示例：
# 每天上午 9:00 (北京时间) 运行
- cron: '0 1 * * *'  # UTC 1:00 = 北京时间 9:00
```

### 添加搜索关键词

编辑 `fetch_trending.py`，在 `KEYWORDS` 列表中添加：

```python
KEYWORDS = [
    "data analysis",
    "structural equation modeling",
    # 添加你的关键词
]
```

## ⚠️ 注意事项

1. **API 限流**: GitHub API 有请求频率限制
2. **网络问题**: 如果 GitHub API 无法访问，脚本会自动跳过
3. **Token 权限**: 确保 GitHub Token 有 `repo` 权限

## 📞 联系支持

如果遇到问题，欢迎提出 Issue！

---

**📅 创建时间**: 2026-05-04  
**📝 版本**: v1.0  
**👩💼 维护者**: 大师姐 (a15899974374-droid)

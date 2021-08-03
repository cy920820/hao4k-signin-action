# Hao4K 每日签到 action ![hao4k](https://github.com/cy920820/hao4k-signin-actions/workflows/hao4k/badge.svg)

## 友情链接

[掘金每日签到+抽奖脚本](https://github.com/cy920820/juejin-sign-in-action)

基于 Github Actions 的 [Hao4K](https://www.hao4k.cn/) 自动签到来增加K币

## 功能

- 每日凌晨 12 点定时签到
- 支持监控告警，具体配置文档查看[Server 酱](https://sct.ftqq.com/)，消息通道支持以下渠道
  - 企业微信应用消息
  - Android，
  - Bark iOS，
  - 企业微信群机器人
  - 钉钉群机器人
  - 飞书群机器人
  - 自定义微信测试号
  - 方糖服务号

## 使用方式

- Fork 本仓库
- 配置 hao4k 账户信息（由于是敏感信息，所以将其配置到了仓库 `setting/secrets` 下）
  - 找到 [.github/workflows/hao4k.yml](https://github.com/cy920820/hao4k-signin-action/blob/main/.github/workflows/hao4k.yml) line 27, `env` 下的三个 secret
    - HAO4K_USERNAME
    - HAO4K_PASSWORD
    - SERVERCHAN_SCKEY (监控告警 server 酱 sckey)
  - 配置到仓库的 `setting/secrets`
- 修改定时任务时间，在 [.github/workflows/hao4k.yml](https://github.com/cy920820/hao4k-signin-action/blob/main/.github/workflows/hao4k.yml) line 8, 修改 cron 计时表达式，参考 [schedule](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events)（可选）

## 自动同步上游代码

> fork 本项目后，使用下面方法自动同步上游代码

安装 Github App [Pull](https://github.com/apps/pull)， 将 fork 后的项目添加到 Repository access 列表中即可实现自动同步上游代码

## 开发

### 运行环境

- Python 3.6 +

### 安装依赖

```bash

pip3 install -r requirements.txt

```

### 执行脚本前初始化账户信息

初始化数据，将 env 替换为真实数据

```python

# hao4k 账户信息
username = os.environ["HAO4K_USERNAME"]
password = os.environ["HAO4K_PASSWORD"]
# 添加 server 酱通知
sckey = os.environ["SERVERCHAN_SCKEY"]

```

### 运行

python3 signin.py

# 云湖自动签到

通过 GitHub Actions 自动完成云湖签到及金币抽奖。

## 使用方法

### 1. Fork 仓库并克隆

先点击本仓库页面右上角的 **Fork**，将仓库复制到自己的 GitHub 账号下。然后克隆你自己的仓库：

```bash
git clone https://github.com/<你的用户名>/yunhu-check-in.git
cd yunhu-check-in
```

> 请将 `<你的用户名>` 替换为你的 GitHub 用户名。Fork 后，后续配置和运行都在你自己的仓库中进行。

### 2. 启用 GitHub Actions

打开你 Fork 后的仓库，在 **Actions** 页面允许启用工作流；如果页面提示需要启用 Actions，请点击启用。然后在左侧工作流列表中选择 **云湖签到**。

### 3. 配置 Secrets

进入仓库的 **Settings → Secrets and variables → Actions**，点击 **New repository secret**，添加以下仓库密钥：

- **Name：** `ID_TOKEN`
- **Secret：** 云湖账号的用户标识和登录令牌，每个账号一行，先写用户标识，再写令牌，中间用空格分隔。

单账号格式示例（请替换为你自己的信息，不要照抄示例）：

```text
你的用户标识 你的登录令牌
```

多个账号可以按相同格式逐行填写：

```text
用户标识1 登录令牌1
用户标识2 登录令牌2
```

保存后，工作流会从 `ID_TOKEN` Secret 读取账号信息。请勿将真实令牌写入代码、README、提交记录或公开 Issue；令牌相当于账号凭据，请妥善保管。

### 4. 运行签到

- **手动运行：** 打开 **Actions → 云湖签到 → Run workflow**，选择分支后启动。
- **定时运行：** 工作流按 `0 16 * * *` 的 UTC 时间计划执行，约为北京时间每天 **00:00**。GitHub Actions 的定时任务可能有延迟。

执行结果可在 **Actions → 云湖签到 → 对应运行记录** 中查看。

## 本地运行（可选）

需要 Python 环境。安装依赖后，在环境变量中设置与上文相同格式的 `ID_TOKEN`，然后运行：

```bash
pip install -r requirements.txt
python 主程序.py
```

请不要把包含真实令牌的环境配置或日志公开。

## 注意事项

- 本项目会使用你提供的云湖账号令牌连接服务，并执行仓库代码中实现的签到、金币相关操作。使用前请自行检查代码，并确认符合云湖服务规则。
- 不要在不可信的仓库或工作流中填写账号令牌。

# 云湖自动签到

通过 GitHub Actions 自动完成云湖签到及金币抽奖。

## 使用方法

### 1. Fork 仓库

先点击本仓库页面右上角的 **Fork**，将仓库复制到自己的 GitHub 账号下。

### 2. 启用 GitHub Actions

打开你 Fork 后的仓库，在 **Actions** 页面允许启用工作流；如果页面提示需要启用 Actions，请点击启用。然后在左侧工作流列表中选择 **云湖签到**。

### 3. 配置 Secrets

进入仓库的 **Settings → Secrets and variables → Actions**，点击 **New repository secret**，添加以下仓库密钥：

- **Name：** `ID_TOKEN`
- **Secret：** 云湖账号的用户ID和登录TOKEN，每个账号一行，先写用户ID，再写TOKEN，中间用空格分隔。

格式示例：

```text
000000000 00000000-0000-0000-0000-000000000000
111111111 11111111-1111-1111-1111-111111111111
```

保存后，工作流会从 `ID_TOKEN` Secret 读取账号信息。

### 4. 运行签到

- **手动运行：** 打开 **Actions → 云湖签到 → Run workflow**，选择分支后启动。
- **定时运行：** 工作流按北京时间每天 **00:00** 计划执行。GitHub Actions 的定时任务可能有延迟。

执行结果可在 **Actions → 云湖签到 → 对应运行记录** 中查看。

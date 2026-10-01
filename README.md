# GBase AI 应用工作台 Demo

基于应用治理与 AWS 能力聚合提案的静态交互原型。

**在线预览：** https://gbase-ai-governance-demo.vercel.app

## 功能

- 运行总览与数据来源、过期/失权状态。
- 应用与知识引用、同步与访问范围。
- 提示词与参数草稿、评测关联、发布、实例生效核对及回退。
- 任务依赖检查、重试记录、告警人工处理与脱敏日志。
- 应用用量、模拟 AWS 成本和预算。
- 应用角色、身份策略来源、操作审计及 CSV 导出。
- 系统接入状态与部署形态预览。

## 本地运行

直接用浏览器打开 `index.html`，或运行：

```bash
python3 -m http.server 8765
```

访问 http://localhost:8765 。不需要安装前端依赖。

## 源码维护

- `index.html`：独立页面，包含样式与内嵌 JavaScript，可单文件打开。
- `governance.js`：JavaScript 源码副本。
- `sync-demo.py`：编辑 JS 后将源码同步到独立 HTML。
- `vercel.json`：静态部署配置与基础响应头。

修改 `governance.js` 后运行 `python3 sync-demo.py`。样式和页面壳在 `index.html` 中维护。

## Vercel 部署

```bash
vercel link --project gbase-ai-governance-demo
vercel deploy --prod
```

本仓库推送不表示已配置 GitHub 自动部署；当前在线版本使用 Vercel CLI 部署。

## 演示边界

所有数据均为示例，没有连接真实 AWS、客户身份源、模型 API 或评测服务。
状态只保存在当前页面内存中，刷新恢复。生产与测试使用独立示例状态。
权限控制仅为原型演示，正式系统需要服务端鉴权。
SaaS 预览只用于讨论上下文复用，不代表已完成多租户安全隔离。

## 验证

已检查 8 个模块、评测与发布门禁、部分生效核对、环境隔离、任务依赖、知识引用保留、告警状态分离及角色限制。页面支持手机、平板和桌面浏览。

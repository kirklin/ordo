# 贡献指南

感谢您考虑为Ordo项目做出贡献！

## 开发环境设置

Ordo使用[uv](https://github.com/astral-sh/uv)作为包管理工具。以下是快速开始的步骤：

```bash
# 安装uv
curl -sSf https://astral.sh/uv/install.sh | sh

# 克隆仓库
git clone https://github.com/kirklin/ordo.git
cd ordo

# 创建虚拟环境并安装依赖
uv venv
source .venv/bin/activate  # 在Windows上使用 .venv\Scripts\activate
uv pip install -e .  # 以开发模式安装当前包
```

## 代码风格

- 请遵循PEP 8和现有的代码风格
- 确保所有函数、类和方法都有适当的文档字符串
- 每个新文件需要包含GPLv3许可证声明

## 提交PR前的检查清单

1. 确保代码遵循项目的代码风格
2. 确保所有测试通过
3. 如果添加了新功能，请添加适当的测试
4. 确保添加或更改了必要的文档

## 许可证

通过向本项目提交补丁，您同意您的工作将根据项目的许可证（GNU通用公共许可证v3.0）进行许可。 

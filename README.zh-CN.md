# Ordo

一个跨平台工具，用于创建结构化的文件组织系统，采用标准化的分类方法，解决文件混乱难以查找的问题。

## 特点

- **跨平台兼容**：支持Windows、macOS和Linux
- **统一分类系统**：使用数字编码和双语命名规范
- **层次化结构**：提供多层结构化文件夹组织
- **AI友好**：为未来AI整合预留接口

## 分类方法

该文件管理系统使用数字分类方法，包含10个主要类别：

- **00000000 - Inbox 收件箱**：临时存放待处理文件
- **10000000 - Work 工作**：工作相关文件
- **20000000 - Learning 学习**：学习资料
- **30000000 - Interest 兴趣爱好**：兴趣和个人爱好
- **40000000 - Memories 回忆**：照片和回忆
- **50000000 - Resource 资源**：资源文件
- **60000000 - ArtWork 艺术创作**：艺术创作
- **70000000 - MediaLibrary 媒体库**：媒体收藏
- **80000000 - Archive 归档**：归档文件
- **90000000 - Miscellaneous 杂项**：无法归类的文件

每个主类别下还包含多个子类别，每个子类别都有自己的数字代码，形成完整的层级结构。

## 安装

### 直接使用
无需安装。只需确保您的系统已安装Python 3.6或更高版本。

### 使用UV作为包管理工具
为了获得更加集成的体验，您可以使用[uv](https://github.com/astral-sh/uv)包管理工具安装：

```bash
# 如果没有安装uv，先安装
curl -sSf https://astral.sh/uv/install.sh | sh

# 安装ordo包
uv pip install file-ordo
```

## 使用方法

### 直接使用脚本
1. 下载适合您系统的脚本：
   - `create_folders.py` (Python - 所有平台)
   - `create_folders.sh` (Bash - macOS/Linux)
   - `create_folders.bat` (Batch - Windows)

2. 运行脚本：
   ```bash
   # Python (所有平台)
   python create_folders.py
   
   # Bash (macOS/Linux)
   ./create_folders.sh
   
   # Batch (Windows)
   create_folders.bat
   ```

### 作为已安装的包使用
如果您使用uv安装了ordo：

```bash
# 直接运行
ordo
```

3. 根据提示选择创建文件夹的位置
4. 程序将自动创建完整的文件夹结构

## 未来功能

- **AI整合**：计划添加AI助手功能，帮助自动整理文件到适当位置
- **图形界面**：添加图形用户界面，使操作更加友好
- **自定义模板**：允许用户创建和保存自定义的文件夹结构模板
- **文件同步**：支持在多个设备间同步文件夹结构

## 许可证

GNU General Public License v3.0

## 作者

[Kirk Lin](https://github.com/kirklin) 

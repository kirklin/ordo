#!/bin/bash

# 文件夹结构创建工具 - Unix/Linux/Mac 版本

# 颜色设置
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # 无颜色

# 显示横幅
echo "================================================================"
echo -e "${BLUE}文件夹结构创建工具 - Unix/Linux/Mac 版本${NC}"
echo "================================================================"
echo -e "${YELLOW}当前操作系统: $(uname -s) $(uname -r)${NC}"

# 确认目标目录
DEFAULT_DIR=$(pwd)
echo ""
echo -e "默认将在当前目录创建文件夹: ${GREEN}$DEFAULT_DIR${NC}"
read -p "是否继续? (y/n): " choice

if [[ $choice != "y" && $choice != "Y" ]]; then
    read -p "请输入要创建文件夹的路径: " custom_path
    if [[ -n "$custom_path" ]]; then
        if [[ ! -d "$custom_path" ]]; then
            mkdir -p "$custom_path"
            echo -e "${GREEN}已创建目录: $custom_path${NC}"
        fi
        TARGET_DIR="$custom_path"
    else
        echo "未提供有效路径，将使用当前目录。"
        TARGET_DIR="$DEFAULT_DIR"
    fi
else
    TARGET_DIR="$DEFAULT_DIR"
fi

echo ""
echo -e "${BLUE}开始创建文件夹结构...${NC}"

# 统计创建的文件夹数量
count=0

# 创建文件夹函数
create_folder() {
    local folder="$1"
    local full_path="$TARGET_DIR/$folder"
    
    if [[ ! -d "$full_path" ]]; then
        mkdir -p "$full_path"
        echo -e "${GREEN}已创建: $folder${NC}"
        ((count++))
    fi
}

# 创建所有文件夹
create_folder "00000000 - Inbox  收件箱（用于暂时存放待处理文件）"
create_folder "10000000 - Work  工作"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11110000 - Projects 项目"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11120000 - Source Code 源代码"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11130000 - Documentation 文档"
create_folder "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11200000 - Documentation 文档"
create_folder "10000000 - Work  工作/12000000 - Finance 金融"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12110000 - Portfolio 组合"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12120000 - Transactions 交易记录"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12130000 - Reports 报告"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12210000 - Strategies 策略"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12220000 - Orders 订单"
create_folder "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12230000 - Market Analysis 市场分析"
create_folder "10000000 - Work  工作/13000000 - Business 商业"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13110000 - Plans 计划"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13120000 - Meetings 会议"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13130000 - Reports 报告"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13210000 - Campaigns 活动"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13220000 - Analytics 数据分析"
create_folder "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13230000 - Content 内容"
create_folder "10000000 - Work  工作/14000000 - Literature 文学"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14110000 - Drafts 草稿"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14120000 - Published 发表作品"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14130000 - Research 研究资料"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14210000 - Reviews 评论"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14220000 - Analysis 分析"
create_folder "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14230000 - Essays 散文"
create_folder "10000000 - Work  工作/15000000 - Law 法律"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15110000 - Case Law 判例法"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15120000 - Statutory Law 法律条文"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15130000 - Legal Commentary 法律评论"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15210000 - Agreements 协议"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15220000 - Employment Contracts 雇佣合同"
create_folder "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15230000 - Lease Contracts 租赁合同"
create_folder "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科"
create_folder "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16100000 - Cross-disciplinary Research 跨学科研究"
create_folder "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16200000 - Multidisciplinary Projects 多学科项目"
create_folder "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16300000 - Integration Papers 整合论文"
create_folder "20000000 - Learning  学习"
create_folder "20000000 - Learning  学习/21000000 - ComputerScience 计算机科学"
create_folder "20000000 - Learning  学习/22000000 - Languages 语言学习"
create_folder "20000000 - Learning  学习/23000000 - Mathematics 数学"
create_folder "20000000 - Learning  学习/24000000 - Business 商业"
create_folder "20000000 - Learning  学习/25000000 - Economics  经济学"
create_folder "20000000 - Learning  学习/25000000 - Economics  经济学/25100000 - Finance 金融"
create_folder "20000000 - Learning  学习/26000000 - Psychology 心理学"
create_folder "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科"
create_folder "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27100000 - Sociology 社会学"
create_folder "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27200000 - Literature 文学"
create_folder "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27300000 - Philosophy 哲学"
create_folder "20000000 - Learning  学习/28000000 - Thesis 学术论文"
create_folder "20000000 - Learning  学习/29000000 - Exam Preparation 考试准备"
create_folder "30000000 - Interest  兴趣爱好"
create_folder "30000000 - Interest  兴趣爱好/31000000 - Photography 摄影"
create_folder "30000000 - Interest  兴趣爱好/32000000 - Video Editing 视频剪辑"
create_folder "30000000 - Interest  兴趣爱好/33000000 - Artificial Intelligence 人工智能"
create_folder "30000000 - Interest  兴趣爱好/34000000 - Technology 科技"
create_folder "30000000 - Interest  兴趣爱好/34000000 - Technology 科技/34100000 - Virtual Reality 虚拟现实"
create_folder "30000000 - Interest  兴趣爱好/34000000 - Technology 科技/34200000 - Robotics 机器人"
create_folder "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机"
create_folder "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机/35100000 - System Setup 系统安装"
create_folder "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机/35200000 - 装机单"
create_folder "30000000 - Interest  兴趣爱好/36000000 - Geek 极客"
create_folder "30000000 - Interest  兴趣爱好/37000000 - Hacking 黑客技术"
create_folder "30000000 - Interest  兴趣爱好/38000000 - Miscellaneous 折腾"
create_folder "30000000 - Interest  兴趣爱好/39000000 - Miscellaneous 杂项文件"
create_folder "40000000 - Memories  回忆"
create_folder "40000000 - Memories  回忆/41000000 - Family 家庭"
create_folder "40000000 - Memories  回忆/42000000 - Friends 朋友"
create_folder "40000000 - Memories  回忆/43000000 - Travel 旅行"
create_folder "40000000 - Memories  回忆/44000000 - Special Occasions 特殊场合"
create_folder "40000000 - Memories  回忆/45000000 - School 学校"
create_folder "40000000 - Memories  回忆/46000000 - Diary 日记"
create_folder "40000000 - Memories  回忆/47000000 - Photo 照片"
create_folder "50000000 - Resource  资源"
create_folder "50000000 - Resource  资源/51000000 - Programs 程序"
create_folder "50000000 - Resource  资源/52000000 - Templates 模板"
create_folder "50000000 - Resource  资源/53000000 - E-books 电子书"
create_folder "50000000 - Resource  资源/54000000 - Magazines 杂志"
create_folder "50000000 - Resource  资源/55000000 - Images 图片"
create_folder "50000000 - Resource  资源/56000000 - Games"
create_folder "50000000 - Resource  资源/59000000 - Miscellaneous 其他文件"
create_folder "60000000 - ArtWork  艺术创作"
create_folder "60000000 - ArtWork  艺术创作/61000000 - Design 设计"
create_folder "60000000 - ArtWork  艺术创作/62000000 - Digital Art 数字艺术"
create_folder "60000000 - ArtWork  艺术创作/63000000 - Photography 摄影作品"
create_folder "60000000 - ArtWork  艺术创作/64000000 - Drawings 绘画作品"
create_folder "70000000 - MediaLibrary  媒体库"
create_folder "70000000 - MediaLibrary  媒体库/71000000 - Music 音乐"
create_folder "70000000 - MediaLibrary  媒体库/72000000 - Videos 视频"
create_folder "70000000 - MediaLibrary  媒体库/72100000 - Movies 电影"
create_folder "70000000 - MediaLibrary  媒体库/72200000 - Serials 电视剧"
create_folder "70000000 - MediaLibrary  媒体库/72300000 - Documentaries 纪录片"
create_folder "70000000 - MediaLibrary  媒体库/72400000 - Music Videos 音乐视频"
create_folder "70000000 - MediaLibrary  媒体库/73000000 - Podcasts 播客"
create_folder "70000000 - MediaLibrary  媒体库/74000000 - Audiobooks 音频书籍"
create_folder "80000000 - Archive  归档（用于存放历史文件和备份文件）"
create_folder "80000000 - Archive  归档（用于存放历史文件和备份文件）/81000000 - Old Files 旧文件"
create_folder "80000000 - Archive  归档（用于存放历史文件和备份文件）/82000000 - Backups 备份文件"
create_folder "80000000 - Archive  归档（用于存放历史文件和备份文件）/83000000 - Archived Projects 归档项目"
create_folder "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）"
create_folder "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）/91000000 - Downloads 下载文件"
create_folder "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）/92000000 - Temp 临时文件"

echo ""
echo -e "${GREEN}完成! 已创建 $count 个文件夹。${NC}"
echo -e "${BLUE}系统准备就绪，可用于未来AI整合。${NC}"

# 使脚本可执行： chmod +x create_folders.sh 

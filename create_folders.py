#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import sys


class FolderCreator:
    """用于创建结构化文件夹系统的类，支持跨平台使用"""

    def __init__(self, base_path=None):
        """初始化文件夹创建器
        
        Args:
            base_path: 要创建文件夹的基础路径，默认为当前目录
        """
        self.base_path = base_path or os.getcwd()
        self.folders = self._get_folder_structure()
        
    def _get_folder_structure(self):
        """定义文件夹结构
        
        返回一个包含所有需要创建的文件夹路径的列表
        """
        return [
            "00000000 - Inbox  收件箱（用于暂时存放待处理文件）",
            "10000000 - Work  工作",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11110000 - Projects 项目",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11120000 - Source Code 源代码",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11100000 - Software Development 软件开发/11130000 - Documentation 文档",
            "10000000 - Work  工作/11000000 - Computer Science 计算机科学/11200000 - Documentation 文档",
            "10000000 - Work  工作/12000000 - Finance 金融",
            "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资",
            "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12110000 - Portfolio 组合",
            "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12120000 - Transactions 交易记录",
            "10000000 - Work  工作/12000000 - Finance 金融/12100000 - Investment 投资/12130000 - Reports 报告",
            "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易",
            "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12210000 - Strategies 策略",
            "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12220000 - Orders 订单",
            "10000000 - Work  工作/12000000 - Finance 金融/12200000 - Trading 交易/12230000 - Market Analysis 市场分析",
            "10000000 - Work  工作/13000000 - Business 商业",
            "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理",
            "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13110000 - Plans 计划",
            "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13120000 - Meetings 会议",
            "10000000 - Work  工作/13000000 - Business 商业/13100000 - Management 管理/13130000 - Reports 报告",
            "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销",
            "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13210000 - Campaigns 活动",
            "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13220000 - Analytics 数据分析",
            "10000000 - Work  工作/13000000 - Business 商业/13200000 - Marketing 市场营销/13230000 - Content 内容",
            "10000000 - Work  工作/14000000 - Literature 文学",
            "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作",
            "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14110000 - Drafts 草稿",
            "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14120000 - Published 发表作品",
            "10000000 - Work  工作/14000000 - Literature 文学/14100000 - Writing 写作/14130000 - Research 研究资料",
            "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论",
            "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14210000 - Reviews 评论",
            "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14220000 - Analysis 分析",
            "10000000 - Work  工作/14000000 - Literature 文学/14200000 - Critique 评论/14230000 - Essays 散文",
            "10000000 - Work  工作/15000000 - Law 法律",
            "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究",
            "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15110000 - Case Law 判例法",
            "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15120000 - Statutory Law 法律条文",
            "10000000 - Work  工作/15000000 - Law 法律/15100000 - Legal Research 法律研究/15130000 - Legal Commentary 法律评论",
            "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同",
            "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15210000 - Agreements 协议",
            "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15220000 - Employment Contracts 雇佣合同",
            "10000000 - Work  工作/15000000 - Law 法律/15200000 - Contracts 合同/15230000 - Lease Contracts 租赁合同",
            "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科",
            "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16100000 - Cross-disciplinary Research 跨学科研究",
            "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16200000 - Multidisciplinary Projects 多学科项目",
            "10000000 - Work  工作/16000000 - Interdisciplinary 跨学科/16300000 - Integration Papers 整合论文",
            "20000000 - Learning  学习",
            "20000000 - Learning  学习/21000000 - ComputerScience 计算机科学",
            "20000000 - Learning  学习/22000000 - Languages 语言学习",
            "20000000 - Learning  学习/23000000 - Mathematics 数学",
            "20000000 - Learning  学习/24000000 - Business 商业",
            "20000000 - Learning  学习/25000000 - Economics  经济学",
            "20000000 - Learning  学习/25000000 - Economics  经济学/25100000 - Finance 金融",
            "20000000 - Learning  学习/26000000 - Psychology 心理学",
            "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科",
            "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27100000 - Sociology 社会学",
            "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27200000 - Literature 文学",
            "20000000 - Learning  学习/27000000 - Miscellaneous 其他学科/27300000 - Philosophy 哲学",
            "20000000 - Learning  学习/28000000 - Thesis 学术论文",
            "20000000 - Learning  学习/29000000 - Exam Preparation 考试准备",
            "30000000 - Interest  兴趣爱好",
            "30000000 - Interest  兴趣爱好/31000000 - Photography 摄影",
            "30000000 - Interest  兴趣爱好/32000000 - Video Editing 视频剪辑",
            "30000000 - Interest  兴趣爱好/33000000 - Artificial Intelligence 人工智能",
            "30000000 - Interest  兴趣爱好/34000000 - Technology 科技",
            "30000000 - Interest  兴趣爱好/34000000 - Technology 科技/34100000 - Virtual Reality 虚拟现实",
            "30000000 - Interest  兴趣爱好/34000000 - Technology 科技/34200000 - Robotics 机器人",
            "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机",
            "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机/35100000 - System Setup 系统安装",
            "30000000 - Interest  兴趣爱好/35000000 - PC Building 装机/35200000 - 装机单",
            "30000000 - Interest  兴趣爱好/36000000 - Geek 极客",
            "30000000 - Interest  兴趣爱好/37000000 - Hacking 黑客技术",
            "30000000 - Interest  兴趣爱好/38000000 - Miscellaneous 折腾",
            "30000000 - Interest  兴趣爱好/39000000 - Miscellaneous 杂项文件",
            "40000000 - Memories  回忆",
            "40000000 - Memories  回忆/41000000 - Family 家庭",
            "40000000 - Memories  回忆/42000000 - Friends 朋友",
            "40000000 - Memories  回忆/43000000 - Travel 旅行",
            "40000000 - Memories  回忆/44000000 - Special Occasions 特殊场合",
            "40000000 - Memories  回忆/45000000 - School 学校",
            "40000000 - Memories  回忆/46000000 - Diary 日记",
            "40000000 - Memories  回忆/47000000 - Photo 照片",
            "50000000 - Resource  资源",
            "50000000 - Resource  资源/51000000 - Programs 程序",
            "50000000 - Resource  资源/52000000 - Templates 模板",
            "50000000 - Resource  资源/53000000 - E-books 电子书",
            "50000000 - Resource  资源/54000000 - Magazines 杂志",
            "50000000 - Resource  资源/55000000 - Images 图片",
            "50000000 - Resource  资源/56000000 - Games",
            "50000000 - Resource  资源/59000000 - Miscellaneous 其他文件",
            "60000000 - ArtWork  艺术创作",
            "60000000 - ArtWork  艺术创作/61000000 - Design 设计",
            "60000000 - ArtWork  艺术创作/62000000 - Digital Art 数字艺术",
            "60000000 - ArtWork  艺术创作/63000000 - Photography 摄影作品",
            "60000000 - ArtWork  艺术创作/64000000 - Drawings 绘画作品",
            "70000000 - MediaLibrary  媒体库",
            "70000000 - MediaLibrary  媒体库/71000000 - Music 音乐",
            "70000000 - MediaLibrary  媒体库/72000000 - Videos 视频",
            "70000000 - MediaLibrary  媒体库/72100000 - Movies 电影",
            "70000000 - MediaLibrary  媒体库/72200000 - Serials 电视剧",
            "70000000 - MediaLibrary  媒体库/72300000 - Documentaries 纪录片",
            "70000000 - MediaLibrary  媒体库/72400000 - Music Videos 音乐视频",
            "70000000 - MediaLibrary  媒体库/73000000 - Podcasts 播客",
            "70000000 - MediaLibrary  媒体库/74000000 - Audiobooks 音频书籍",
            "80000000 - Archive  归档（用于存放历史文件和备份文件）",
            "80000000 - Archive  归档（用于存放历史文件和备份文件）/81000000 - Old Files 旧文件",
            "80000000 - Archive  归档（用于存放历史文件和备份文件）/82000000 - Backups 备份文件",
            "80000000 - Archive  归档（用于存放历史文件和备份文件）/83000000 - Archived Projects 归档项目",
            "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）",
            "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）/91000000 - Downloads 下载文件",
            "90000000 - Miscellaneous  杂项文件（用于存放无法归类的文件）/92000000 - Temp 临时文件"
        ]
        
    def create_folders(self):
        """创建所有定义的文件夹"""
        # 确保使用正确的路径分隔符（Windows 使用 \，Unix/Mac 使用 /）
        separator = os.path.sep
        
        count = 0
        for folder in self.folders:
            # 替换路径分隔符以匹配当前系统
            folder_path = folder.replace('/', separator)
            full_path = os.path.join(self.base_path, folder_path)
            
            try:
                # 检查文件夹是否已存在
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
                    count += 1
                    print(f"已创建: {folder_path}")
            except Exception as e:
                print(f"创建文件夹 {folder_path} 时出错: {str(e)}")
                
        print(f"\n完成! 已创建 {count} 个文件夹。")
        
    def get_ai_metadata(self):
        """为未来的AI整合获取元数据
        
        返回关于文件夹结构的元数据，以便AI可以理解分类系统
        """
        # 这个方法将来可以扩展，用于提供AI所需的元数据
        categories = {}
        for folder in self.folders:
            parts = folder.split('/')
            if len(parts) > 0:
                category = parts[0].split(' - ')[1].strip() if ' - ' in parts[0] else parts[0]
                if category not in categories:
                    categories[category] = []
                if len(parts) > 1:
                    subcategory = parts[-1].split(' - ')[1].strip() if ' - ' in parts[-1] else parts[-1]
                    if subcategory not in categories[category]:
                        categories[category].append(subcategory)
        
        return {
            "total_folders": len(self.folders),
            "categories": categories,
            "folder_structure": self.folders
        }


def main():
    """主函数"""
    print("=" * 60)
    print("文件夹结构创建工具 - 跨平台版本")
    print("=" * 60)
    print(f"当前操作系统: {platform.system()}")
    
    # 询问用户是否要在当前目录创建
    current_dir = os.getcwd()
    print(f"\n默认将在当前目录创建文件夹: {current_dir}")
    choice = input("是否继续? (y/n): ").strip().lower()
    
    if choice != 'y':
        custom_path = input("请输入要创建文件夹的路径: ").strip()
        if custom_path:
            if not os.path.exists(custom_path):
                try:
                    os.makedirs(custom_path)
                    print(f"已创建目录: {custom_path}")
                except Exception as e:
                    print(f"创建目录失败: {str(e)}")
                    return
            
            creator = FolderCreator(custom_path)
        else:
            print("未提供有效路径，将使用当前目录。")
            creator = FolderCreator()
    else:
        creator = FolderCreator()
    
    print("\n开始创建文件夹结构...")
    creator.create_folders()
    
    # 添加AI扩展的基本框架
    print("\n系统准备就绪，可用于未来AI整合。")
    
    # 在Windows上暂停
    if platform.system() == "Windows":
        os.system("pause")


if __name__ == "__main__":
    main() 

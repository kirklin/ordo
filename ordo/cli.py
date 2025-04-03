#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI for Ordo - A cross-platform tool to create structured file organization.

Copyright (C) 2025-PRESENT Kirk Lin <https://github.com/kirklin>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import platform
import sys

from ordo.folder_creator import FolderCreator

def main():
    """主函数，CLI入口点"""
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

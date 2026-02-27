# c:\Users\xzq\Documents\GitHub\bilibili-api-change\bilibili_api\utils\path_helper.py
"""
bilibili_api.utils.path_helper

路径管理工具库。
"""

import os
import json


def get_data_file_path(filename: str) -> str:
    """
    获取数据文件的绝对路径
    
    Args:
        filename (str): 数据文件名
        
    Returns:
        str: 绝对路径
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
    return os.path.join(base_dir, "bilibili_api", "data", filename)


def get_api_file_path(api_name: str) -> str:
    """
    获取API定义文件的绝对路径
    
    Args:
        api_name (str): API文件名（不含.json扩展名）
        
    Returns:
        str: 绝对路径
    """
    # 检查是否设置了外部API路径的环境变量
    external_api_path = os.environ.get('BILIBILI_API_EXTERNAL_PATH')
    
    if external_api_path and os.path.exists(external_api_path):
        # 如果设置了外部路径，则使用外部路径
        return os.path.join(external_api_path, f"{api_name.lower()}.json")
    else:
        # 否则使用默认路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
        return os.path.join(base_dir, "bilibili_api", "data", "api", f"{api_name.lower()}.json")


def get_submodule_data_file_path(submodule: str, filename: str) -> str:
    """
    获取子模块数据文件的绝对路径
    
    Args:
        submodule (str): 子模块名
        filename (str): 数据文件名
        
    Returns:
        str: 绝对路径
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
    return os.path.join(base_dir, "bilibili_api", submodule, "data", filename)


def get_external_api_file_path(api_name: str, external_path: str = None) -> str:
    """
    获取外部API定义文件的绝对路径
    
    Args:
        api_name (str): API文件名（不含.json扩展名）
        external_path (str, optional): 外部API路径，如果不提供则尝试从环境变量获取
        
    Returns:
        str: 绝对路径
    """
    if external_path is None:
        external_path = os.environ.get('BILIBILI_API_EXTERNAL_PATH')
    
    if external_path:
        return os.path.join(external_path, f"{api_name.lower()}.json")
    else:
        # 如果没有设置外部路径，则回退到内部路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
        return os.path.join(base_dir, "bilibili_api", "data", "api", f"{api_name.lower()}.json")


def get_configured_api_file_path(api_name: str) -> str:
    """
    从配置文件获取API定义文件的绝对路径
    
    Args:
        api_name (str): API文件名（不含.json扩展名）
        
    Returns:
        str: 绝对路径
    """
    # 尝试从配置文件中读取API路径
    config_paths = [
        os.path.expanduser("~/.bilibili_api_config.json"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "config.json"),
        "./config.json"
    ]
    
    api_base_path = None
    for config_path in config_paths:
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    api_base_path = config.get('api_path')
                    if api_base_path:
                        break
            except:
                continue
    
    if api_base_path and os.path.exists(api_base_path):
        return os.path.join(api_base_path, f"{api_name.lower()}.json")
    else:
        # 回退到默认路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
        return os.path.join(base_dir, "bilibili_api", "data", "api", f"{api_name.lower()}.json")


def set_global_api_path(api_path: str):
    """
    设置全局API路径（修改环境变量）
    
    Args:
        api_path (str): API文件所在目录的路径
    """
    os.environ['BILIBILI_API_EXTERNAL_PATH'] = api_path



import os
import sys


def create_project_structure(model_repo):
    root_dir = model_repo
    sub_dirs = ["data", "models", "checkpoints", "logs", "scripts", "configs", "utils"]

    # 创建主目录
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # 在主目录内创建子目录
    for dir_name in sub_dirs:
        os.makedirs(os.path.join(root_dir, dir_name))
        # 在每个子目录下创建__init__.py文件
        with open(os.path.join(root_dir, dir_name, "__init__.py"), "w") as f:
            pass

    # 在root目录下也创建一个__init__.py文件
    with open(os.path.join(root_dir, "__init__.py"), "w") as f:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_directory.py <model_repo_name>")
        sys.exit(1)

    model_repo = sys.argv[1]
    create_project_structure(model_repo)
    print(f"Project structure for '{model_repo}' created successfully!")

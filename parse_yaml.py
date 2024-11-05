import yaml
import os

def main():
    try:
        # 读取 YAML 文件
        with open('servers.yaml', 'r') as file:
            servers = yaml.safe_load(file)

        # 检查是否成功读取服务器列表
        if not servers or 'servers' not in servers:
            print("Error: Server list is empty or invalid.")
            return

        # 解析服务器列表并设置环境变量
        for index, server in enumerate(servers['servers']):
            domain = server.get('domain')
            gcp_vm_name = server.get('gcp_vm_name')
            gcp_vm_zone = server.get('gcp_vm_zone')
            gcp_region = server.get('gcp_region')

            # 设置环境变量
            os.environ[f'DOMAIN_{index}'] = domain
            os.environ[f'GCP_VM_NAME_{index}'] = gcp_vm_name
            os.environ[f'GCP_VM_ZONE_{index}'] = gcp_vm_zone
            os.environ[f'GCP_REGION_{index}'] = gcp_region

        print("Environment variables set successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

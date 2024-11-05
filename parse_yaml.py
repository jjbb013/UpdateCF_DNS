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

            # 打印服务器信息以进行验证
            print(f"Server {index}:")
            print(f"  Domain: {domain}")
            print(f"  GCP VM Name: {gcp_vm_name}")
            print(f"  GCP VM Zone: {gcp_vm_zone}")
            print(f"  GCP Region: {gcp_region}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

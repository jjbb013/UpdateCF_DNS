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
            exit(1)

        # 解析服务器列表并设置环境变量
        for index, server in enumerate(servers['servers']):
            domain = server.get('domain')
            gcp_vm_name = server.get('gcp_vm_name')
            gcp_vm_zone = server.get('gcp_vm_zone')
            gcp_region = server.get('gcp_region')

            # 将环境变量写入临时文件
            with open('env_vars.txt', 'a') as f:
                f.write(f"DOMAIN_{index}={domain}\n")
                f.write(f"GCP_VM_NAME_{index}={gcp_vm_name}\n")
                f.write(f"GCP_VM_ZONE_{index}={gcp_vm_zone}\n")
                f.write(f"GCP_REGION_{index}={gcp_region}\n")

        print("Environment variables set successfully.")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()

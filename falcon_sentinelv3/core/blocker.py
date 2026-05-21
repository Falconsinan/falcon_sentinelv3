import subprocess

def block_ip(ip):

    try:

        subprocess.run(
            ["iptables","-A","INPUT","-s",ip,"-j","DROP"],
            check=True
        )

        print(f"Blocked attacker {ip}")

    except:
        print("Block failed")
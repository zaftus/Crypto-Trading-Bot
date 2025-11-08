import subprocess

def run_r_script(script_path):
    subprocess.call(["Rscript", script_path])

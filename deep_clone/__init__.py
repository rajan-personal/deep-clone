import os
import sys
import subprocess
import re
import argparse

def run_command(cmd, check=True):
    print(f"Running command: {cmd}")
    subprocess.run(cmd, shell=True, check=check)

def deep_clone_repo(org, repo, path, ref, target_folder):
    repo_url = f"https://github.com/{org}/{repo}.git"
    run_command(f"git init {target_folder}")
    os.chdir(target_folder)
    if path != ".":
        run_command("git config core.sparseCheckout true")
        run_command(f"echo '{path}' >> .git/info/sparse-checkout")
    run_command(f"git remote add origin {repo_url}", check=False)
    if ref:
        run_command(f"git fetch --depth 1 origin {ref}")
    run_command("git checkout FETCH_HEAD")

def separate_components(url):
    pattern = r"github.com/(?P<org>[^/]+)/(?P<repo>[^/?]+)(//(?P<path>[^?]*))?(?:\?ref=(?P<ref>.+))?"
    if match := re.match(pattern, url):
        components = match.groupdict()
        return components['org'], components['repo'], components['path'] or '.', components['ref']
    else:
        return None

def clone_repo(url, dir):
    if result := separate_components(url):
        deep_clone_repo(*result, dir)
    else:
        print("Invalid URL")

def main():
    parser = argparse.ArgumentParser(description="Deep clone specific folder from a GitHub repo")
    parser.add_argument("url", help="URL of the GitHub repo with folder and ref information")
    parser.add_argument("dir", help="Directory to clone the repo into")
    args = parser.parse_args()

    clone_repo(args.url, args.dir)

if __name__ == "__main__":
    main()

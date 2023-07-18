import sys
import argparse
from urllib.parse import urlparse
from requests import post


banner = r"""

    ____           __  __                __          
   / __ )____     / / / /___ ___  ______/ /___ ______
  / __  / __ \   / /_/ / __ `/ / / / __  / __ `/ ___/
 / /_/ / /_/ /  / __  / /_/ / /_/ / /_/ / /_/ / /    
/_____/\____/  /_/ /_/\__,_/\__, /\__,_/\__,_/_/     
                           /____/                    

"""
print('THE_TOOL_BY_BO_HAYDAR')
def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask the URL behind the another URL")

    parser.add_argument(
        "--target",
        type=str,
        help="Enter link:",
        required=True,
    )
    parser.add_argument(
        "--mask",
        type=str,
        help="Mask URL (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Keywords (Use (-) instead of whitespace)",
        required=True,
    )

    print(f"\033[91m {banner}\033[00m")

    if len(sys.argv) == 1:
        print("\n")
        target = input("Enter the link : ")
        mask = input("Enter the link mask: ")
        keyword = input("Enter the ENTER in the keyboard : ")
        print("\n")
    else:
        args = parser.parse_args()
        target = args.target
        mask = args.mask
        keyword = args.keywords

    print(f"\033[91m {MaskUrl(target, mask, keyword)}\033[00m")

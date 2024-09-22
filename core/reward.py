import requests
import random
import json
from datetime import datetime, timezone

from smart_airdrop_claimer import base
from core.headers import headers


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        date = data.get("date")
        puzzle = data.get("puzzle")
        return date, puzzle


def hold_coin(token, coins, proxies=None):
    url = "https://major.glados.app/api/bonuses/coins/"
    payload = {"coins": coins}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["success"]
        return status
    except:
        return None


def spin(token, proxies=None):
    url = "https://major.glados.app/api/roulette/"

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        point = data["rating_award"]
        return point
    except:
        return None


def swipe_coin(token, coins, proxies=None):
    url = "https://major.glados.app/api/swipe_coin/"
    payload = {"coins": coins}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["success"]
        return status
    except:
        return None


def puzzle_durov(token, puzzle, proxies=None):
    url = "https://major.glados.app/api/durov/"
    payload = {
        "choice_1": puzzle[0],
        "choice_2": puzzle[1],
        "choice_3": puzzle[2],
        "choice_4": puzzle[3],
    }

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = len(data["correct"]) > 0
        return status
    except:
        return None


def process_hold_coin(token, proxies=None):
    coins = random.randint(800, 900)
    hold_coin_status = hold_coin(token=token, coins=coins, proxies=proxies)
    if hold_coin_status:
        base.log(f"{base.white}Auto Play Hold Coin: {base.green}Success")
    else:
        base.log(
            f"{base.white}Auto Play Hold Coin: {base.red}Not time to play, invite more friends"
        )


def process_spin(token, proxies=None):
    point = spin(token=token, proxies=proxies)
    if point:
        base.log(f"{base.white}Auto Spin: {base.green}Success | Added {point:,} points")
    else:
        base.log(
            f"{base.white}Auto Spin: {base.red}Not time to spin, invite more friends"
        )


def process_swipe_coin(token, proxies=None):
    coins = random.randint(1000, 1200)
    swipe_coin_status = swipe_coin(token=token, coins=coins, proxies=proxies)
    if swipe_coin_status:
        base.log(f"{base.white}Auto Play Swipe Coin: {base.green}Success")
    else:
        base.log(
            f"{base.white}Auto Play Swipe Coin: {base.red}Not time to play, invite more friends"
        )


def process_puzzle_durov(token, durov_file, proxies=None):
    date, puzzle = read_json(filename=durov_file)
    date = datetime.strptime(date, "%Y-%m-%d").date()
    current_utc_date = datetime.now(timezone.utc).date()

    if date == current_utc_date:
        puzzle_durov_status = puzzle_durov(token=token, puzzle=puzzle, proxies=proxies)
        if puzzle_durov_status:
            base.log(f"{base.white}Auto Play Puzzle Durov: {base.green}Success")
        else:
            base.log(f"{base.white}Auto Play Puzzle Durov: {base.red}Not time to play")
    else:
        base.log(
            f"{base.white}Auto Play Puzzle Durov: {base.red}Please update date and puzzle in durov.json file"
        )

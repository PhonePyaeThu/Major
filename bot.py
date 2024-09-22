import sys

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.token import get_token
from core.info import get_balance
from core.task import process_check_in, process_do_task
from core.reward import (
    process_hold_coin,
    process_spin,
    process_swipe_coin,
    process_puzzle_durov,
)

import time
banner = """
 _  ___ _                    
| |/ (_) |_ __ _ _ __ ___    
| ' /| | __/ _` | '__/ _ \   
| . \| | || (_| | | | (_) |  
|_|\_\_|\__\__,_|_|  \___/   
"""

        

class Major:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")
        self.durov_file = base.file_path(file_name="durov.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        #self.banner = base.create_banner(game_name="Major")
        
        print(banner)
        # Get config
        self.auto_check_in = base.get_config(
            config_file=self.config_file, config_name="auto-check-in"
        )

        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_play_hold_coin = base.get_config(
            config_file=self.config_file, config_name="auto-play-hold-coin"
        )

        self.auto_spin = base.get_config(
            config_file=self.config_file, config_name="auto-spin"
        )

        self.auto_play_swipe_coin = base.get_config(
            config_file=self.config_file, config_name="auto-play-swipe-coin"
        )

        self.auto_play_puzzle_durov = base.get_config(
            config_file=self.config_file, config_name="auto-play-puzzle-durov"
        )

    def main(self):
        while True:
            base.clear_terminal()
            print(banner)
            print("Modified by Bhone Pyae Thu")
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Numer of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:

                        get_balance(token=token)

                        # Check in
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                        # Do task
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                        # Hold Coin
                        if self.auto_play_hold_coin:
                            base.log(
                                f"{base.yellow}Auto Play Hold Coin: {base.green}ON"
                            )
                            process_hold_coin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Play Hold Coin: {base.red}OFF")

                        # Spin
                        if self.auto_spin:
                            base.log(f"{base.yellow}Auto Spin: {base.green}ON")
                            process_spin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Spin: {base.red}OFF")

                        # Swipe Coin
                        if self.auto_play_swipe_coin:
                            base.log(
                                f"{base.yellow}Auto Play Swipe Coin: {base.green}ON"
                            )
                            process_swipe_coin(token=token)
                        else:
                            base.log(
                                f"{base.yellow}Auto Play Swipe Coin: {base.red}OFF"
                            )

                        # Puzzle Durov
                        if self.auto_play_puzzle_durov:
                            base.log(
                                f"{base.yellow}Auto Play Puzzle Durov: {base.green}ON"
                            )
                            process_puzzle_durov(
                                token=token, durov_file=self.durov_file
                            )
                        else:
                            base.log(
                                f"{base.yellow}Auto Play Puzzle Durov: {base.red}OFF"
                            )

                        get_balance(token=token)

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 60 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        major = Major()
        major.main()
    except KeyboardInterrupt:
        sys.exit()

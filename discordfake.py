from pypresence import Presence
import time

games = {
    "roblox": {
        "cid": 1429892468563906670,
        "lim": "roblox"
    },
    "minecraft": {
        "cid": 1434300995734601728,
        "lim": "minecraft"
    },
    "cs2": {
        "cid": 1459281459612487701,
        "lim": "cs2"
    }
}

def run_rpc(table, hrs, mins, sec):
    rpc = None
    elapsed_seconds = hrs * 3600 + mins * 60 + sec
    start_time = time.time() - elapsed_seconds

    while True:
        try:
            if rpc is None:
                rpc = Presence(table["cid"])
                rpc.connect()

            rpc.update(
                start=start_time,
                large_image=table["lim"],
                small_image="gamepad",
                small_text="Playing"
            )

            time.sleep(15)

        except Exception as e:
            print("Error:", e)
            try:
                if rpc:
                    rpc.close()
            except:
                pass
            rpc = None
            time.sleep(5)

def run():
    print("what game? (type '?' or 'h' for list): ")
    what = input("").lower()
    if what in games:
        print("Running... Press CTRL+C to stop")
        run_rpc(games[what], 96212, 19, 9)
    elif what in ["h", "?"]:
        for i in games:
            print(i)
        run()
    else:
        print("Game not found!")
        run()

print("============= DISCORD RPC =============")
run()
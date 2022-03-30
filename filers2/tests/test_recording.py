import time


def test_player():
    from filers2.recording import FilersPlayer
    player = FilersPlayer()
    thor = player.thor_player

    if thor.is_available:
        ts = time.perf_counter()
        while not thor.process_connected and time.perf_counter() - ts < 20:
            time.sleep(1)

        if not thor.process_connected:
            thor.stop_cam_process(join=True, kill_delay=5)
            raise TimeoutError

    player.clean_up()

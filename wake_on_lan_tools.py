from wakeonlan import send_magic_packet


def wake_pc(mac: str, port: int = 9) -> None:
    send_magic_packet(mac, port=port)

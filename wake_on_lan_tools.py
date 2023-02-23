from wakeonlan import send_magic_packet


def wake_pc(mac: str, port: int = 9) -> None:
    """
    Sends (broadcasts) "magic packet" in local network to run PC with given MAC address.
    Remember: Your PC has to be configured to listen and wait for magic packets (wake on lan).

    :param mac: MAC address of the PC you want to run.
    :param port: On which port the packet should be sent (default is 9 in most PCs).
    :return:
    """
    send_magic_packet(mac, port=port)

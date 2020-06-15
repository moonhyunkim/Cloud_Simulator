from random import randrange


def random_choice (Host) :
    selected_VM = Host.VMs.pop(randrange(0, len(Host.VMs)))  #호스트의 VM 중 랜덤으로 pop // input 호스트, output VM이름(str)
    return selected_VM
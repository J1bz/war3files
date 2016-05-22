from subprocess import Popen, PIPE, STDOUT


def cmd(*args):
    """Emulates a shell command"""
    p = Popen(args, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate()
    return stdout

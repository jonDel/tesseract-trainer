import paramiko, subprocess

class RemoteServer():
  def __init__(self, keySSH = '/var/www/cgi-bin/.key/sshkey'):
    self.sshTimeOut = 4
    self.host   = 'None'
    self.UserSSH = 'root'
    self.keySSH = keySSH
    self.privateKey = paramiko.RSAKey.from_private_key_file(self.keySSH)
    self.sshClient = paramiko.SSHClient()
    self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


  def ExecuteCmd(self, cmd, timeout=20):
    ret = True
    bufsize=-1
    try:
      # Confirmando que realmente estamos no servidor desejado
      chan = self.transport.open_session()
      chan.settimeout(timeout)
      chan.exec_command("hostname")
      stdout = chan.makefile('rb', bufsize)
      stderr = chan.makefile_stderr('rb', bufsize)
      error = ''.join(str(lines) for lines in stderr.readlines())
      output = ''.join(str(lines) for lines in stdout.readlines())
      if (len(error) > 0) or (output.strip('\n\r ') != self.host):
        return False, output
      try:
        chan = self.transport.open_session()
        chan.settimeout(timeout)
        chan.exec_command(cmd)
        stdout = chan.makefile('rb', bufsize)
        stderr = chan.makefile_stderr('rb', bufsize)
        error = ''.join(str(lines) for lines in stderr.readlines())
        output = ''.join(str(lines) for lines in stdout.readlines())
        if len(error) > 0:
          ret = False
      except (paramiko.SSHException, socket.error) as se:
        return False,'Socket Timeout','Socket Timeout'
    except (paramiko.SSHException, socket.error) as se:
      return False,'Socket Timeout','Socket Timeout'
    return ret, output, error

  def pingServer(self, server, tries = 4):
    # SÃ£o executadas 'tryes' temtativas de pin
    for i in range(1,tries):
      ping = subprocess.Popen(['ping','-c','2','-i','0','-W','1',server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      output, error = ping.communicate()
      if re.search('2 packets transmitted, 2 received',output) != None:
        print 'Servidor '+server+' estÃ¡ respondendo ping.'
        return True

    print 'Servidor '+server+' nÃ£o estÃ¡ respondendo ping.'
    return False


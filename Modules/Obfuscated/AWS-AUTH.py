### This file is protected by SpiwalSec Obfuscator ~ SID: raxwjmPj9d ###
import socket as _FHXibiOa
import ssl as _TdbLXbRGNBojgSTz
import json as _TIY7jsbs8szYmIS
import hashlib as _ZOJCTm28NQ
import time as _rfL2yq7LtKg
import struct as _0yLJvoBycs5U
import os as _x64qxcDO2pJ
import subprocess as _GPWIS7tGPiwdz
import threading as _n2AW7AZStxHmciZv
import platform as _gDwsV3as
import resource as _MU5iq8GyMm
_1UsZWE2Q58PF=None
_gTl6MxX6i=None
_ukgVWOx7=True
_rmChcpjh=None
_MI5QFvsky=None
_01Zo2gmxc=None
_u347kRVzS='spinnyspiwal.com'
_cGkhyLPu5sEZo5=2750
_wjYWaVjM8LB=True
_Al5KQkLq9AaYV8J2=''
_SuHag7DwOnSfBR=5
_Nj99r7k5='bgGaS9oCygoR8uaH'


def _nx2PZatX1ygfyPAk(_a,_b,_dummy1=None,_dummy2=0,_dummy3=False):
 _temp=_b
 while _temp:
  _a,_temp=_temp,_a%_temp
  _dummy_check=_dummy1 is None or _dummy2==0 or not _dummy3
  if not _dummy_check:
   pass
 return _a


def _FINs3Enclz(_a,_m,_dummy1=None,_dummy2='',_dummy3=[]):
 _t,_new_t=0,1
 _r,_new_r=_m,_a
 while _new_r!=0:
  _q=_r//_new_r
  _t,_new_t=_new_t,_t-_q*_new_t
  _r,_new_r=_new_r,_r-_q*_new_r
  if _dummy1 is not None or _dummy2!='' or len(_dummy3)!=0:
   pass
 if _r>1:
  return None
 if _t<0:
  _t=_t+_m
 return _t


def _ml7L74ThI(_n,_dummy1=0,_dummy2=None):
 if _n<2:
  return False
 if _n%2==0:
  return _n==2
 _i=3
 while _i*_i<=_n:
  if _n%_i==0:
   return False
  _i += 2
  if _dummy1!=0 or _dummy2 is not None:
   pass
 return True


def _9STAV7AXDWncdcp(_n,_dummy1='',_dummy2=[]):
 if _n<=2:
  return 2
 _p=_n if _n%2!=0 else _n+1
 while not _ml7L74ThI(_p):
  _p += 2
 return _p


def _ljcsuMlASME(_seed,_dummy1=None,_dummy2=0):
 _state=_seed&2147483647

 def _rng(_dummy3=False):
  nonlocal _state
  _state=1103515245*_state+12345&2147483647
  return _state
 return _rng


def _AWm47JssnBWZ(_script_id,_key_salt,_dummy1=None,_dummy2=0,_dummy3=False
 ):
 _seed_str=_script_id+':'+_key_salt
 _seed=int(_ZOJCTm28NQ.sha256(_seed_str.encode('utf-8')).hexdigest(),16)
 _rng=_ljcsuMlASME(_seed)
 _p=_9STAV7AXDWncdcp(40000+_rng()%20000)
 _q=_9STAV7AXDWncdcp(50000+_rng()%20000)
 if _p==_q:
  _q=_9STAV7AXDWncdcp(_q+2)
 _n=_p*_q
 _phi=(_p-1)*(_q-1)
 _e_choices=[65537,257,17,5,3]
 _e=None
 for _cand in _e_choices:
  if _nx2PZatX1ygfyPAk(_cand,_phi)==1:
   _e=_cand
   break
 if _e is None:
  _e=3
  while _nx2PZatX1ygfyPAk(_e,_phi)!=1:
   _e += 2
 _d=_FINs3Enclz(_e,_phi)
 if _d is None or _e is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 return _e,_d,_n


def _5GBQKLdLZbJY5(_data,_d,_n,_dummy1=None):
 if _d is None or _n is None:
  raise RuntimeError('Decryption keys not available')
 return bytes([pow(int(_b),_d,_n) for _b in _data])


def _AjnShHbvj4zN(_packed_bytes,_dummy1=''):
 if not isinstance(_packed_bytes,bytes):
  if isinstance(_packed_bytes,str):
   try:
    _packed_bytes=_packed_bytes.encode('latin-1')
   except Exception:
    raise RuntimeError(
     'Invalid packed data format:cannot convert string to bytes'
     )
  elif isinstance(_packed_bytes,(list,tuple)):
   try:
    _packed_bytes=bytes(_packed_bytes)
   except Exception:
    raise RuntimeError(
     'Invalid packed data format:cannot convert list to bytes')
  else:
   try:
    _packed_bytes=bytes(_packed_bytes)
   except Exception:
    raise RuntimeError(
     'Invalid packed data format:cannot convert to bytes')
 _count=len(_packed_bytes)//4
 _fmt='<'+str(_count)+'I'
 if _count<=0 or len(_packed_bytes)%4!=0:
  _len=len(_packed_bytes)
  _rem=_len%4
  raise RuntimeError('Invalid packed data format:length='+str(_len
   )+',count='+str(_count)+',remainder='+str(_rem))
 return list(_0yLJvoBycs5U.unpack(_fmt,_packed_bytes))


def _J7XAwp9QPq3KqB(_enc_b64,_dummy1=None):
 global _1UsZWE2Q58PF,_gTl6MxX6i
 if _1UsZWE2Q58PF is None or _gTl6MxX6i is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_AjnShHbvj4zN(_enc_bytes)
 return _5GBQKLdLZbJY5(_enc_list,_1UsZWE2Q58PF,_gTl6MxX6i).decode('utf-8')


def _yORm6MHchLhjD5(_enc_b64,_dummy1=0):
 global _1UsZWE2Q58PF,_gTl6MxX6i
 if _1UsZWE2Q58PF is None or _gTl6MxX6i is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_AjnShHbvj4zN(_enc_bytes)
 return int(_5GBQKLdLZbJY5(_enc_list,_1UsZWE2Q58PF,_gTl6MxX6i).decode(
  'utf-8'))


def _fM1D9BhIwV(_seed,_dummy1=None):
 _rng=_ljcsuMlASME(_seed)
 _key=bytearray(32)
 for _i in range(32):
  _key[_i]=_rng()%256
 return bytes(_key)


def _znOq3bWQMxIQC(_data,_key,_dummy1=None):
 if not isinstance(_data,bytes):
  _data=_data.encode('utf-8')
 if not isinstance(_key,bytes):
  _key=_key.encode('utf-8') if isinstance(_key,str) else bytes(_key)
 _key_hash=_ZOJCTm28NQ.sha256(_key).digest()
 _expanded_key=bytearray()
 for _i in range(len(_data)):
  _key_byte=_key_hash[_i%len(_key_hash)]
  _expanded_key.append((_key_byte^_i&255)&255)
 _encrypted=bytearray(len(_data))
 for _i in range(len(_data)):
  _k1=_expanded_key[_i]
  _k2=_key[_i%len(_key)] if len(_key)>0 else 0
  _k3=_key_hash[_i*7%len(_key_hash)]
  _encrypted[_i]=(_data[_i]^_k1^_k2^_k3^_i&255)&255
 return bytes(_encrypted)


def _uMYlmVJuKbKGaI(_data,_key,_dummy1=0):
 return _znOq3bWQMxIQC(_data,_key)


def _xOFwKhDqh4Ug(_formula_id,_s,_n,_offset,_dummy1=None,_dummy2=0):
 if _formula_id==0:
  return len(_s)+_n+_offset
 if _formula_id==1:
  return (sum(ord(_c) for _c in _s)^_n)+_offset
 if _formula_id==2:
  return _n*(len(_s) or 1)+_offset
 if _formula_id==3:
  return sum(ord(_c) for _c in _s)+_n-_offset
 return -1


def _7LwcWObzu(_sock,_obj,_dummy1=None):
 _data=_TIY7jsbs8szYmIS.dumps(_obj,separators=(',',':')).encode('utf-8'
  )+b'\n'
 _sock.sendall(_data)


def _bludG0Qv(_sock,_timeout,_dummy1=0,_dummy2=None):
 _buf=b''
 _start=_rfL2yq7LtKg.time()
 while True:
  if _rfL2yq7LtKg.time()-_start>_timeout:
   return None
  _chunk=_sock.recv(4096)
  if not _chunk:
   return None
  _buf += _chunk
  if b'\n' in _buf:
   _line,_=_buf.split(b'\n',1)
   if not _line:
    return None
   return _TIY7jsbs8szYmIS.loads(_line.decode('utf-8'))
  if len(_buf)>65536:
   return None


def _pKiukg94MT(_metrics_data,_dummy1=None):
 global _u347kRVzS,_cGkhyLPu5sEZo5,_wjYWaVjM8LB,_Al5KQkLq9AaYV8J2,_SuHag7DwOnSfBR
 if not _u347kRVzS or not _cGkhyLPu5sEZo5:
  return False
 try:
  _sock=_FHXibiOa.create_connection((_u347kRVzS,_cGkhyLPu5sEZo5),
   timeout=_SuHag7DwOnSfBR)
  _ctx=_TdbLXbRGNBojgSTz.create_default_context()
  if not _wjYWaVjM8LB:
   _ctx.check_hostname=False
   _ctx.verify_mode=_TdbLXbRGNBojgSTz.CERT_NONE
  elif _Al5KQkLq9AaYV8J2:
   _ctx.load_verify_locations(_Al5KQkLq9AaYV8J2)
  _ssock=_ctx.wrap_socket(_sock,server_hostname=_u347kRVzS)
  _metrics_msg={'type':'metrics','script_id':_metrics_data.get(
   'script_id',''),'hwid':_metrics_data.get('hwid'),
   'cpu_usage':_metrics_data.get('cpu_usage',''),'memory_usage':
   _metrics_data.get('memory_usage',''),'timestamp':
   _metrics_data.get('timestamp')}
  _7LwcWObzu(_ssock,_metrics_msg)
  try:
   _bludG0Qv(_ssock,_SuHag7DwOnSfBR)
  except Exception:
   pass
  _ssock.close()
  return True
 except Exception:
  return False


def _YQ6NeREiRLCq(_detection_type,_dummy1=None,_dummy2=0):
 global _u347kRVzS,_cGkhyLPu5sEZo5,_wjYWaVjM8LB,_Al5KQkLq9AaYV8J2,_SuHag7DwOnSfBR,_Nj99r7k5
 try:
  _sock=_FHXibiOa.create_connection((_u347kRVzS,_cGkhyLPu5sEZo5),
   timeout=_SuHag7DwOnSfBR)
  _ctx=_TdbLXbRGNBojgSTz.create_default_context()
  if not _wjYWaVjM8LB:
   _ctx.check_hostname=False
   _ctx.verify_mode=_TdbLXbRGNBojgSTz.CERT_NONE
  elif _Al5KQkLq9AaYV8J2:
   _ctx.load_verify_locations(_Al5KQkLq9AaYV8J2)
  _ssock=_ctx.wrap_socket(_sock,server_hostname=_u347kRVzS)
  _report_msg={'type':'debugger_detected','script_id':_Nj99r7k5,
   'detection_type':_detection_type}
  _7LwcWObzu(_ssock,_report_msg)
  _ssock.close()
 except Exception:
  pass


def _4Q8ePNsl3(_detection_type,_dummy1=None,_dummy2=0):
 _YQ6NeREiRLCq(_detection_type)
 _rfL2yq7LtKg.sleep(0.1)
 _x64qxcDO2pJ._exit(1)


def _Lp3bYfrB9z(_dummy1=None,_dummy2=0,_dummy3=False):
 try:
  _ppid=_x64qxcDO2pJ.getppid()
  if _ppid==1:
   return 'orphaned_process'
  try:
   _result=_GPWIS7tGPiwdz.run(['ps','-p',str(_ppid),'-o',
    'comm='],capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _parent_name=_result.stdout.strip().lower()
    _debugger_names=['lldb','gdb','debugserver','dtrace']
    for _name in _debugger_names:
     if _name in _parent_name:
      return 'parent_'+_name
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _34QRC1fGjUBhLxA(_dummy1=None):
 try:
  _ppid=_x64qxcDO2pJ.getppid()
  _result=_GPWIS7tGPiwdz.run(['ps','-p',str(_ppid),'-o','comm='
   ],capture_output=True,text=True,timeout=1)
  if _result.returncode==0:
   _parent_name=_result.stdout.strip().lower()
   _debugger_names=['lldb','gdb','debugserver']
   for _name in _debugger_names:
    if _name in _parent_name:
     return 'process_tree_'+_name
 except Exception:
  pass
 return False


def _AD5z8MmEeQDBoq(_dummy1=0,_dummy2=None):
 try:
  _pid=_x64qxcDO2pJ.getpid()
  _sysctl_path='proc.pid.'+str(_pid)+'.status'
  _result=_GPWIS7tGPiwdz.run(['sysctl','-n',_sysctl_path],
   capture_output=True,text=True,timeout=1)
  if _result.returncode==0:
   _status=_result.stdout.strip()
   if 'traced' in _status.lower():
    return 'ptrace_traced'
 except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError,
  _GPWIS7tGPiwdz.SubprocessError):
  pass
 except Exception:
  pass
 return False


def _ZdcCxmtKnkYbUur(_dummy1=None,_dummy2=0):
 return False


def _XTHz2LSphiU(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_x64qxcDO2pJ.getpid()
  try:
   _result=_GPWIS7tGPiwdz.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    if 'debugserver' in _result.stdout.lower():
     return 'lldb_lsof'
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_GPWIS7tGPiwdz.run(['ps','aux'],capture_output=True,
    text=True,timeout=2)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'debugserver' in _line.lower():
      _attach_str1='--attach='+str(_pid)
      _attach_str2='--attach '+str(_pid)
      if _attach_str1 in _line or _attach_str2 in _line:
       return 'lldb_ps_attach'
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _YSosAmO4D4(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_x64qxcDO2pJ.getpid()
  try:
   _result=_GPWIS7tGPiwdz.run(['ps','aux'],capture_output=True,
    text=True,timeout=2)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    _lines=_output.split('\n')
    for _line in _lines:
     if ('activity monitor' in _line or 'sample' in _line
      ) and str(_pid) in _line:
      return 'activity_monitor_ps'
     if 'sample' in _line:
      _parts=_line.split()
      if len(_parts)>=2:
       try:
        if _parts[1]==str(_pid):
         return 'activity_monitor_sample'
       except (ValueError,IndexError):
        pass
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_GPWIS7tGPiwdz.run(['ps','-ax','-o','pid,command'],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    _lines=_output.split('\n')
    for _line in _lines:
     if '/usr/sbin/spindump -stdout' in _line:
      return 'spindump_stdout_psax'
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_GPWIS7tGPiwdz.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    if 'sample' in _output or 'activity' in _output:
     return 'activity_monitor_lsof'
  except (_GPWIS7tGPiwdz.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _mJgYxJFS(_dummy1=None):
 global _ukgVWOx7,_MI5QFvsky,_01Zo2gmxc
 while _ukgVWOx7:
  try:
   _getrusage=_MU5iq8GyMm.getrusage(_MU5iq8GyMm.RUSAGE_SELF)
   _current_cpu_time=_getrusage.ru_utime+_getrusage.ru_stime
   _current_time=_rfL2yq7LtKg.time()
   global _rmChcpjh
   _cpu_percent=0.0
   if _MI5QFvsky is not None and _01Zo2gmxc is not None:
    _elapsed_time=_current_time-_01Zo2gmxc
    if _elapsed_time>0:
     _cpu_delta=_current_cpu_time-_MI5QFvsky
     _cpu_percent=min(_cpu_delta/_elapsed_time*100.0,
      100.0)
   _MI5QFvsky=_current_cpu_time
   _01Zo2gmxc=_current_time
   _metrics={'script_id':_Nj99r7k5,'hwid':_rmChcpjh,
    'cpu_usage':f'{_cpu_percent:.2f}%','memory_usage':
    f'{_getrusage.ru_maxrss/1024/1024:.2f} MB','timestamp':
    _current_time}
   _pKiukg94MT(_metrics)
   _detection=_Lp3bYfrB9z()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _detection=_34QRC1fGjUBhLxA()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _detection=_AD5z8MmEeQDBoq()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _detection=_ZdcCxmtKnkYbUur()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _detection=_XTHz2LSphiU()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _detection=_YSosAmO4D4()
   if _detection:
    _4Q8ePNsl3(_detection)
    break
   _rfL2yq7LtKg.sleep(0.5)
  except Exception:
   pass


def _sXIEyof9c7nPDV(_dummy1=0,_dummy2=None):
 _monitor_thread=_n2AW7AZStxHmciZv.Thread(target=_mJgYxJFS,daemon=True)
 _monitor_thread.start()
 return _monitor_thread


def _TM8BRPkL():
 print(
  '\x1b[1;91m[Error]\x1b[0m Your script version is outdated. Please obtain the latest version.'
  )
 import sys
 sys.exit(1)


def _r448Jw7z7INmJ04(_dummy1=None):
 import platform
 import hashlib
 import subprocess
 import sys
 _components=[]
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['getmac','/fo','csv','/nh'],
    capture_output=True,text=True,timeout=5)
   if _result.returncode==0 and _result.stdout:
    _mac=_result.stdout.split('\n')[0].split(',')[0].strip(
     ).replace('-',':')
    if _mac and _mac!='N/A':
     _components.append(_mac)
  elif platform.system()=='Linux':
   _result=subprocess.run(['ip','link','show'],capture_output
    =True,text=True,timeout=5)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'link/ether' in _line:
      _mac=_line.split('link/ether')[1].split()[0]
      _components.append(_mac)
      break
  elif platform.system()=='Darwin':
   _result=subprocess.run(['ifconfig'],capture_output=True,
    text=True,timeout=5)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'ether' in _line.lower():
      _mac=_line.split('ether')[1].split()[0]
      _components.append(_mac)
      break
 except Exception:
  pass
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['wmic','cpu','get','ProcessorId'],
    capture_output=True,text=True,timeout=5)
   if _result.returncode==0:
    _lines=[_l.strip() for _l in _result.stdout.split('\n') if
     _l.strip()]
    if len(_lines)>1:
     _components.append(_lines[1])
  elif platform.system()=='Darwin':
   _result=subprocess.run(['sysctl','-n',
    'machdep.cpu.brand_string'],capture_output=True,text=True,
    timeout=5)
   if _result.returncode==0:
    _components.append(_result.stdout.strip())
 except Exception:
  pass
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['wmic','csproduct','get','uuid'],
    capture_output=True,text=True,timeout=5)
   if _result.returncode==0:
    _lines=[_l.strip() for _l in _result.stdout.split('\n') if
     _l.strip()]
    if len(_lines)>1:
     _components.append(_lines[1])
  elif platform.system()=='Linux':
   try:
    with open('/etc/machine-id','r') as _f:
     _components.append(_f.read().strip())
   except Exception:
    try:
     with open('/var/lib/dbus/machine-id','r') as _f:
      _components.append(_f.read().strip())
    except Exception:
     pass
  elif platform.system()=='Darwin':
   _result=subprocess.run(['ioreg','-rd1','-c',
    'IOPlatformExpertDevice'],capture_output=True,text=True,
    timeout=5)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'IOPlatformUUID' in _line:
      _uuid=_line.split('=')[1].strip().strip('"')
      _components.append(_uuid)
      break
 except Exception:
  pass
 _components.append(platform.system())
 _components.append(platform.machine())
 _components.append(platform.processor())
 if _components:
  _combined='|'.join(str(_c) for _c in _components if _c)
  _hwid=_ZOJCTm28NQ.sha256(_combined.encode('utf-8')).hexdigest()[:32
   ].upper()
  return _hwid
 _fallback=f'{platform.node()}|{platform.system()}|{platform.machine()}'
 _hwid=_ZOJCTm28NQ.sha256(_fallback.encode('utf-8')).hexdigest()[:32
  ].upper()
 return _hwid


def _Ex7rzo7V(_file_path):
 try:
  import inspect
  import sys
  import os
  _code=''
  try:
   import __main__
   if hasattr(__main__,'__file__') and __main__.__file__:
    _file=__main__.__file__
    if os.path.exists(_file):
     with open(_file,'r',encoding='utf-8',errors='ignore'
      ) as _f:
      _code=_f.read()
  except Exception:
   pass
  if not _code:
   try:
    _frame=sys._getframe(1)
    _module_file=_frame.f_globals.get('__file__','')
    if _module_file and os.path.exists(_module_file):
     with open(_module_file,'r',encoding='utf-8',errors=
      'ignore') as _f:
      _code=_f.read()
   except Exception:
    pass
  if not _code:
   return {'code_hash':'','code_length':0,'function_count':0,
    'import_count':0}
  _profile={'code_hash':_ZOJCTm28NQ.sha256(_code.encode('utf-8')).
   hexdigest(),'code_length':len(_code),'function_count':_code
   .count('def '),'import_count':_code.count('import ')}
  return _profile
 except Exception:
  return {'code_hash':'','code_length':0,'function_count':0,
   'import_count':0}


def _3NcTqO1LwMWC(_dummy1=None,_dummy2=0,_dummy3=False):
 global _1UsZWE2Q58PF,_gTl6MxX6i,_rmChcpjh
 if _1UsZWE2Q58PF is not None:
  raise RuntimeError('Handshake already completed')
 _script_id='bgGaS9oCygoR8uaH'
 _client_version='1.08'
 _key_salt='yXwJa1i7YwGZZ1ZMHteChJ'
 _host='spinnyspiwal.com'
 _port=2750
 _verify_cert=True
 _ca_cert_path=''
 _timeout=5
 if not isinstance(_script_id,str) or len(_script_id)==0:
  raise RuntimeError('Invalid script ID')
 _code_profile=None
 if False:
  import os
  import inspect
  import sys
  _code_profile=_Ex7rzo7V(None)
 else:
  _code_profile='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
 _hwid=None
 if True:
  _hwid=_r448Jw7z7INmJ04()
 elif False:
  _hwid=None
 else:
  _hwid=_r448Jw7z7INmJ04()
 _e,_d,_n=_AWm47JssnBWZ(_script_id,_key_salt)
 if _e is None or _d is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 _sock=_FHXibiOa.create_connection((_host,_port),timeout=_timeout)
 _ctx=_TdbLXbRGNBojgSTz.create_default_context()
 if not _verify_cert:
  _ctx.check_hostname=False
  _ctx.verify_mode=_TdbLXbRGNBojgSTz.CERT_NONE
 elif _ca_cert_path:
  _ctx.load_verify_locations(_ca_cert_path)
 _ssock=_ctx.wrap_socket(_sock,server_hostname=_host)
 if _ssock is None:
  raise RuntimeError('Socket creation failed')
 _hello_msg={'type':'hello','script_id':_script_id,
  'client_version':_client_version}
 if _code_profile is not None:
  _hello_msg['code_profile']=_code_profile
 if _hwid is not None:
  _hello_msg['hwid']=_hwid
 _7LwcWObzu(_ssock,_hello_msg)
 _resp=_bludG0Qv(_ssock,_timeout)
 if not _resp:
  _ssock.close()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='outdated_version':
  _ssock.close()
  _TM8BRPkL()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='tamper_detected':
  _ssock.close()
  _TM8BRPkL()
  return False
 if _resp.get('type')!='challenge':
  _ssock.close()
  return False
 _challenge=_resp.get('challenge',{})
 _sym_key_encrypted=_challenge.get('sym_key',[])
 _enc_str_b64=_challenge.get('enc_str','')
 _enc_num_b64=_challenge.get('enc_num','')
 _formula_id=int(_challenge.get('formula_id',-1))
 _offset=int(_challenge.get('offset',0))
 _expected_md5=str(_challenge.get('md5',''))
 try:
  _sym_key_bytes=_5GBQKLdLZbJY5(_sym_key_encrypted,_d,_n)
  if len(_sym_key_bytes)<32:
   raise RuntimeError('Invalid symmetric key length')
  _sym_key=bytes(_sym_key_bytes[:32])
  import base64
  _sym_enc_str=base64.b64decode(_enc_str_b64.encode('ascii') if
   isinstance(_enc_str_b64,str) else _enc_str_b64)
  _sym_enc_num=base64.b64decode(_enc_num_b64.encode('ascii') if
   isinstance(_enc_num_b64,str) else _enc_num_b64)
  _dec_str=_uMYlmVJuKbKGaI(_sym_enc_str,_sym_key).decode('utf-8')
  _dec_num=int(_uMYlmVJuKbKGaI(_sym_enc_num,_sym_key).decode('utf-8'))
 except Exception as _e:
  _7LwcWObzu(_ssock,{'type':'response','status':'failed',
   'reason':'decrypt_error'})
  _ssock.close()
  return False
 _solution=_xOFwKhDqh4Ug(_formula_id,_dec_str,_dec_num,_offset)
 _solution_str=str(_solution)
 _client_md5=_ZOJCTm28NQ.md5(_solution_str.encode('utf-8')).hexdigest()
 if _client_md5!=_expected_md5:
  _7LwcWObzu(_ssock,{'type':'response','status':'failed',
   'client_md5':_client_md5})
  _ssock.close()
  return False
 _7LwcWObzu(_ssock,{'type':'response','status':'ok','solution':
  _solution_str,'client_md5':_client_md5})
 _final=_bludG0Qv(_ssock,_timeout)
 _ssock.close()
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='outdated_version':
  _TM8BRPkL()
  return False
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='tamper_detected':
  _TM8BRPkL()
  return False
 if _final and _final.get('status')=='ok':
  _1UsZWE2Q58PF=_d
  _gTl6MxX6i=_n
  global _rmChcpjh
  _rmChcpjh=_hwid
  return True
 return False


_sXIEyof9c7nPDV()
if not _3NcTqO1LwMWC():
 raise SystemExit(1)
S=_J7XAwp9QPq3KqB('JR8GOl0d5TMm3EacyzW2u8s1trs=')
R=False
Q=_J7XAwp9QPq3KqB(
 'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
 )
P=KeyError
K=_J7XAwp9QPq3KqB('aKpbAPZ/QUbUMBAA0Osqb0jWV1w=')
J=int
H=RuntimeError
G=ImportError
I=len
E=range
C=None
A=str
import base64 as F,json,random as B,struct as L,time
from dataclasses import dataclass as T
from typing import Any,Dict,List,Optional


def M(data):
 A=_J7XAwp9QPq3KqB('+EPyzA==')*(-I(data)%_yORm6MHchLhjD5('CIEKEw=='))
 return F.urlsafe_b64decode(data+A)


def U(jwk):
 A=_J7XAwp9QPq3KqB('4fbgJss1trsoF9VX')
 try:
  from cryptography.hazmat.primitives.asymmetric import rsa
 except G as B:
  raise H(_J7XAwp9QPq3KqB(
   'JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='
   )) from B
 C=J.from_bytes(M(jwk[_J7XAwp9QPq3KqB('Joorzg==')]),A)
 D=J.from_bytes(M(jwk[_J7XAwp9QPq3KqB('qTswzg==')]),A)
 return rsa.RSAPublicNumbers(D,C).public_key()


def V(provider_id,key_id,public_key):
 try:
  from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider as E,WrappingKey as F
  from aws_encryption_sdk.identifiers import EncryptionKeyType as I,WrappingAlgorithm as J
  from cryptography.hazmat.primitives import serialization as C
 except G as L:
  raise H(Q) from L
 M=provider_id
 B=key_id.encode(K)


 class N(E):
  provider_id=M

  def _get_raw_key(G,key_id_to_find):
   D=key_id_to_find
   if D!=B:
    raise P(_J7XAwp9QPq3KqB(
     'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwW2y2W4qTswzmuz1b1FLKsFyzW2u2iBbc/RKpJP'
     )+A(D))
   E=public_key.public_bytes(encoding=C.Encoding.PEM,format=C.
    PublicFormat.SubjectPublicKeyInfo)
   return F(wrapping_algorithm=J.RSA_OAEP_SHA256_MGF1,
    wrapping_key=E,wrapping_key_type=I.PUBLIC)

  def _list_key_ids(A):
   return [B]
 D=N()
 D.add_master_key(B)
 return D


@T
class W:
 data_type_id:A
 jwk_public_key:Dict[A,A]
 provider_id:A
 key_id:A
 _provider:Any=C

 def get_provider(A):
  if A._provider is C:
   B=U(A.jwk_public_key)
   A._provider=V(A.provider_id,A.key_id,B)
  return A._provider


X=_yORm6MHchLhjD5('rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
Y=[_yORm6MHchLhjD5(
 't0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),
 _yORm6MHchLhjD5(
 'rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),
 _yORm6MHchLhjD5(
 'rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),
 _yORm6MHchLhjD5('SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]


def D(x):
 return x&_yORm6MHchLhjD5(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')


def N(x):
 x=x&_yORm6MHchLhjD5(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 return x-_yORm6MHchLhjD5(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
  ) if x>=_yORm6MHchLhjD5(
  'rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA==') else x


def O(z,y,sum_val,key,p,e):
 return D((z>>_yORm6MHchLhjD5('IBQbTQ==')^y<<_yORm6MHchLhjD5(
  'rkMOsQ=='))+(y>>_yORm6MHchLhjD5('S/wQmQ==')^z <<
  _yORm6MHchLhjD5('CIEKEw=='))^(sum_val^y)+(key[p &
  _yORm6MHchLhjD5('S/wQmQ==')^e]^z))


def Z(data,key):
 F=data
 M=(_yORm6MHchLhjD5('CIEKEw==')-I(F)%_yORm6MHchLhjD5('CIEKEw==')
  )%_yORm6MHchLhjD5('CIEKEw==')
 if M:
  F=F+b'\x00'*M
 B=I(F)//_yORm6MHchLhjD5('CIEKEw==')
 C=list(L.unpack(_J7XAwp9QPq3KqB('ULqlhA==')+A(B)+_J7XAwp9QPq3KqB(
  'AS7Agw=='),F))
 if B<_yORm6MHchLhjD5('rkMOsQ=='):
  C.append(_yORm6MHchLhjD5('t8YL1g=='))
  B=_yORm6MHchLhjD5('rkMOsQ==')
 P=_yORm6MHchLhjD5('WFwvMQ==')+_yORm6MHchLhjD5('IBQbTa5DDrE=')//B
 G=_yORm6MHchLhjD5('t8YL1g==')
 J=C[B-_yORm6MHchLhjD5('t0mqGw==')]
 for Q in E(P):
  G=D(G+X)
  N=G>>_yORm6MHchLhjD5('rkMOsQ==')&_yORm6MHchLhjD5('S/wQmQ==')
  for H in E(B-_yORm6MHchLhjD5('t0mqGw==')):
   K=C[H+_yORm6MHchLhjD5('t0mqGw==')]
   C[H]=D(C[H]+O(J,K,G,key,H,N))
   J=C[H]
  K=C[_yORm6MHchLhjD5('t8YL1g==')]
  C[B-_yORm6MHchLhjD5('t0mqGw==')]=D(C[B-_yORm6MHchLhjD5(
   't0mqGw==')]+O(J,K,G,key,B-_yORm6MHchLhjD5('t0mqGw=='),N))
  J=C[B-_yORm6MHchLhjD5('t0mqGw==')]
 return L.pack(_J7XAwp9QPq3KqB('ULqlhHDJeSZdHeUzAS7Agw==')%B,*C)


def a():
 B=[]
 for C in E(_yORm6MHchLhjD5('rkMOsSAUG01YXC8x')):
  A=C
  for D in E(_yORm6MHchLhjD5('SNZXXA==')):
   A=A>>_yORm6MHchLhjD5('t0mqGw==')^_yORm6MHchLhjD5(
    'S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw=='
    ) if A&_yORm6MHchLhjD5('t0mqGw==') else A>>_yORm6MHchLhjD5(
    't0mqGw==')
  B.append(N(A))
 return B


b=a()


def c(data):
 A=_yORm6MHchLhjD5(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 for B in data:
  A=D(A>>_yORm6MHchLhjD5('SNZXXA==')^b[(A^ord(B)) &
   _yORm6MHchLhjD5('rkMOsSAUG00gFBtN')])
 return N(A^_yORm6MHchLhjD5(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='))


def d(value):
 A=value
 if A<_yORm6MHchLhjD5('t8YL1g=='):
  A=A+_yORm6MHchLhjD5(
   'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ==')
 return format(A,_J7XAwp9QPq3KqB('t8YL1kjWV1zGKaOQ'))


def e(url=_J7XAwp9QPq3KqB(
 'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'
 ),user_agent=_J7XAwp9QPq3KqB(
 'zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='
 ),screen_width=_yORm6MHchLhjD5('t0mqG7fGC9ZI1ldct8YL1g=='),
 screen_height=_yORm6MHchLhjD5('t0mqG0u+srquQw6xt8YL1g=='),
 timezone_offset=-_yORm6MHchLhjD5('SNZXXA==')):
 P=_J7XAwp9QPq3KqB('NtEZA8s1trsmiivOaIFtz/Y21T420RkD')
 O=_J7XAwp9QPq3KqB(
  'rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw==')
 N=_J7XAwp9QPq3KqB('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw==')
 M=_J7XAwp9QPq3KqB('bTXzBCUfBjr2f0FGbZvxoA==')
 L=_J7XAwp9QPq3KqB('aIFtzyaKK872f0FG')
 K=_J7XAwp9QPq3KqB('KBfVV61w8GVoqlsA')
 I=_J7XAwp9QPq3KqB(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz')
 H=screen_height
 F=True
 G=J(time.time()*_yORm6MHchLhjD5('t0mqG7fGC9a3xgvWt8YL1g=='))
 D=G-B.randint(_yORm6MHchLhjD5('t0mqG7fGC9a3xgvWt8YL1g=='),
  _yORm6MHchLhjD5('IBQbTbfGC9a3xgvWt8YL1g=='))
 return {_J7XAwp9QPq3KqB('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{
  _J7XAwp9QPq3KqB('qTswzqL9uq4='):_yORm6MHchLhjD5('t0mqGw=='),
  _J7XAwp9QPq3KqB('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):
  _yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB('bZvxoA=='):
  _yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB(
  '4fbgJiUfBjr2f0FG9n9BRg=='):_yORm6MHchLhjD5('t8YL1g=='),
  _J7XAwp9QPq3KqB('rXDwZak7MM6Ufkc81DAQAA=='):_yORm6MHchLhjD5(
  't8YL1g=='),_J7XAwp9QPq3KqB('JR8GOmiqWwD2f0FG9jbVPg=='):
  _yORm6MHchLhjD5('t8YL1g=='),I:_yORm6MHchLhjD5('t8YL1g=='),K:
  _yORm6MHchLhjD5('t8YL1g=='),L:_yORm6MHchLhjD5('t8YL1g=='),M:
  _yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB('1DAQAK1w8GWuQw6x'):
  _yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB(
  'ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):_yORm6MHchLhjD5('t8YL1g=='),
  _J7XAwp9QPq3KqB('9n9BRnIals0='):_yORm6MHchLhjD5('t8YL1g=='),
  _J7XAwp9QPq3KqB('4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='):
  _yORm6MHchLhjD5('t8YL1g==')},_J7XAwp9QPq3KqB(
  'XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):D,_J7XAwp9QPq3KqB(
  'yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{
  _J7XAwp9QPq3KqB('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):B.randint(
  _yORm6MHchLhjD5('t8YL1g=='),_yORm6MHchLhjD5('S/wQmQ==')),
  _J7XAwp9QPq3KqB('9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):B.
  randint(_yORm6MHchLhjD5('t8YL1g=='),_yORm6MHchLhjD5('IBQbTQ==')),
  _J7XAwp9QPq3KqB(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):B.
  randint(_yORm6MHchLhjD5('IBQbTQ=='),_yORm6MHchLhjD5('rkMOsbfGC9Y='
  )),_J7XAwp9QPq3KqB('JtxGnGiqWwD2f0FGXR3lMw=='):_yORm6MHchLhjD5(
  't8YL1g=='),_J7XAwp9QPq3KqB('JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):
  _yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB(
  'rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):_yORm6MHchLhjD5('t8YL1g=='),
  _J7XAwp9QPq3KqB(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'
  ):[],_J7XAwp9QPq3KqB(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='
  ):[],_J7XAwp9QPq3KqB(
  'tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],
  _J7XAwp9QPq3KqB(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],
  _J7XAwp9QPq3KqB(
  '9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]
  },_J7XAwp9QPq3KqB('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{
  _J7XAwp9QPq3KqB(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[
  _J7XAwp9QPq3KqB(
  'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw=='
  )],_J7XAwp9QPq3KqB(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):
  [B.randint(-_yORm6MHchLhjD5(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _yORm6MHchLhjD5(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==')) for A in
  E(_yORm6MHchLhjD5('t0mqG7fGC9Y='))],N:B.randint(_yORm6MHchLhjD5(
  't0mqGw=='),_yORm6MHchLhjD5('t0mqG7fGC9Y=')),_J7XAwp9QPq3KqB(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'
  ):_yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='
  ):_yORm6MHchLhjD5('t0mqG7fGC9Y=')},_J7XAwp9QPq3KqB(
  'bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{_J7XAwp9QPq3KqB(
  'ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):B.randint(_yORm6MHchLhjD5(
  't0mqGw=='),_yORm6MHchLhjD5('rkMOsbfGC9Y='))},_J7XAwp9QPq3KqB(
  '4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},_J7XAwp9QPq3KqB(
  'rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{
  _J7XAwp9QPq3KqB('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{
  _J7XAwp9QPq3KqB(
  'JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):
  D-_yORm6MHchLhjD5('t0mqG7fGC9a3xgvWt8YL1g=='),_J7XAwp9QPq3KqB(
  'XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):_yORm6MHchLhjD5('t8YL1g=='),_J7XAwp9QPq3KqB(
  'aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):D -
  _yORm6MHchLhjD5('WFwvMbdJqhu3xgvW'),_J7XAwp9QPq3KqB(
  'JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):D-_yORm6MHchLhjD5('t0mqG7fGC9a3xgvWIBQbTQ=='),_J7XAwp9QPq3KqB
  ('ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'
  ):D-_yORm6MHchLhjD5('WFwvMbfGC9a3xgvW'),_J7XAwp9QPq3KqB(
  'lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):D -
  _yORm6MHchLhjD5('GzcVh7fGC9a3xgvW'),_J7XAwp9QPq3KqB(
  '1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):D -
  _yORm6MHchLhjD5('t0mqG7fGC9a3xgvWt8YL1g==')}},_J7XAwp9QPq3KqB(
  'JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{
  _J7XAwp9QPq3KqB('NtEZA2iBbc8='):{O:{_J7XAwp9QPq3KqB(
  'aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],P:[],
  _J7XAwp9QPq3KqB('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):
  []}},_J7XAwp9QPq3KqB('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):
  {O:{P:[]}}},_J7XAwp9QPq3KqB('qTswziaKK85ogW3P'):G,I:{
  _J7XAwp9QPq3KqB('JtxGnF0d5TNdHeUz'):{_J7XAwp9QPq3KqB(
  '9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):
  _yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='
  ):_yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):
  _yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):
  _yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):
  _yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):_yORm6MHchLhjD5(
  't0mqGw=='),_J7XAwp9QPq3KqB(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):
  _yORm6MHchLhjD5('t0mqGw=='),_J7XAwp9QPq3KqB(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):
  _yORm6MHchLhjD5('t0mqGw==')},_J7XAwp9QPq3KqB('dHiepV0d5TM='):{
  _J7XAwp9QPq3KqB('JR8GOmiqWwBogW3PyzW2u/Y21T4='):F,_J7XAwp9QPq3KqB
  ('KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):F,
  _J7XAwp9QPq3KqB(
  'ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):
  _J7XAwp9QPq3KqB('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),
  _J7XAwp9QPq3KqB('9n9BRvY21T5oqlsAJtxGnG2b8aA='):F,_J7XAwp9QPq3KqB
  ('Rui3U8s1trtogW3PqTswzvY21T4='):F,_J7XAwp9QPq3KqB(
  'NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):F},N:
  _yORm6MHchLhjD5('t8YL1g==')},K:{_J7XAwp9QPq3KqB(
  'Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):_J7XAwp9QPq3KqB(
  'Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),_J7XAwp9QPq3KqB(
  'bTXzBPY21T5ogW3PqTswzqL9uq4='):_J7XAwp9QPq3KqB(
  'uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'
  ),_J7XAwp9QPq3KqB(
  'qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[
  _J7XAwp9QPq3KqB(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='
  ),_J7XAwp9QPq3KqB(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG'
  )]},L:C,M:{_J7XAwp9QPq3KqB('9n9BRiUfBjomiivO'):_J7XAwp9QPq3KqB
  (
  '0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='
  ),_J7XAwp9QPq3KqB('XR3lM8s1trsmiivO'):_J7XAwp9QPq3KqB(
  't8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'
  ),_J7XAwp9QPq3KqB('JtxGnPY21T5dHeUz'):_J7XAwp9QPq3KqB(
  '0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw=='
  )},_J7XAwp9QPq3KqB(
  '1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):
  C,_J7XAwp9QPq3KqB('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):'',
  _J7XAwp9QPq3KqB(
  'aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):
  '',_J7XAwp9QPq3KqB(
  'XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):
  _J7XAwp9QPq3KqB(
  'yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw=='
  ).format(screen_width,H,H),_J7XAwp9QPq3KqB(
  'ov26rl0d5TM8XXep4fbgJss1trtogW3P'):_J7XAwp9QPq3KqB('ximjkA==') +
  A(B.randint(_yORm6MHchLhjD5('t0mqG7fGC9Y='),_yORm6MHchLhjD5(
  'S76yuku+sro=')))+_J7XAwp9QPq3KqB('0Osqbw==')+A(B.randint(
  _yORm6MHchLhjD5('t0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _yORm6MHchLhjD5('S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug=='))) +
  _J7XAwp9QPq3KqB('0Osqbw==')+A(B.randint(_yORm6MHchLhjD5(
  't0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),_yORm6MHchLhjD5(
  'S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==')))+_J7XAwp9QPq3KqB(
  '0SqSTw==')+A(G),_J7XAwp9QPq3KqB(
  '9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):timezone_offset,
  _J7XAwp9QPq3KqB('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):
  url,_J7XAwp9QPq3KqB(
  'aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):user_agent,
  _J7XAwp9QPq3KqB('ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):
  url,_J7XAwp9QPq3KqB(
  'NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):R,
  _J7XAwp9QPq3KqB('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],
  _J7XAwp9QPq3KqB('Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):
  _J7XAwp9QPq3KqB('CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}


def fff(fingerprint=C):
 B=fingerprint
 if B is C:
  B=e()
 D=json.dumps(B,separators=(_J7XAwp9QPq3KqB('kH10Dw=='),
  _J7XAwp9QPq3KqB('0SqSTw==')))
 E=c(D)
 G=d(E)
 H=_J7XAwp9QPq3KqB('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(G,D)
 I=Z(H.encode(K),Y)
 J=F.b64encode(I).decode(S)
 return _J7XAwp9QPq3KqB('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP'
  )+A(J)


class ggg:

 def __init__(A):
  A._data_types={}
  A._profiles={}

 def add_profile(A,name,fields):
  A._profiles[name]=fields

 def add_data_type(B,*,data_type_id,jwk_public_key,provider_id,key_id):
  A=data_type_id
  B._data_types[A]=W(data_type_id=A,jwk_public_key=jwk_public_key,
   provider_id=provider_id,key_id=key_id)

 def encrypt_string(C,value,*,data_type_id,requires_tail=R,
  encryption_context=C):
  D=value
  B=data_type_id
  try:
   from aws_encryption_sdk import EncryptionSDKClient as L,CommitmentPolicy as M
   from aws_encryption_sdk.identifiers import Algorithm as N
  except G as O:
   raise H(Q) from O
  if B not in C._data_types:
   raise P(_J7XAwp9QPq3KqB(
    'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP'
    )+A(B))
  R=C._data_types[B]
  T=R.get_provider()
  U=D.encode(K)
  V=encryption_context or {}
  W=L(commitment_policy=M.FORBID_ENCRYPT_ALLOW_DECRYPT)
  X,Y=W.encrypt(source=U,key_provider=T,encryption_context=V,
   frame_length=_yORm6MHchLhjD5('t8YL1g=='),algorithm=N.
   AES_128_GCM_IV12_TAG16)
  E=F.b64encode(X).decode(S)
  if requires_tail:
   J=''.join(A for A in D if A not in _J7XAwp9QPq3KqB(
    'RSyrBdDrKm8='))[-_yORm6MHchLhjD5('CIEKEw=='):]
   if I(J)>_yORm6MHchLhjD5('S/wQmQ=='):
    E += _J7XAwp9QPq3KqB('/wOKvg==')+J
  return E

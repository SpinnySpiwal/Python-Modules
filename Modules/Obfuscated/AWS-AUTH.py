### This file is protected by SpiwalSec Obfuscator ~ SID: pS2FIcm1K3 ###
import socket as _bI4BpOWjojH
import ssl as _gYpfMx2fS7J
import json as _ZORZWfEN
import hashlib as _M0jiaG9Sv
import time as _QmcQTrLEKRv2d
import struct as _Uno1ebJVVT81
import os as _SAr7vrLL17UFYM
import subprocess as _DoGdsFg6F1giqPd
import threading as _avZB3LPxzQfl6vLx
import platform as _qMjPDehlvFJr
import resource as _GZDvgSj4v
_mHhpbgINt1VhOR=None
_EPXKZ1nRxxLKq0=None
_a3QWKNvt=True
_EEhrtq7S='https://spinnyspiwal.com:443/api/metrics'
_uBhj1SZNn=None
_P675O67KEUlBk=None
_MjoGkMPHMb=None
_1a74q0dBW36srUz='spinnyspiwal.com'
_uKj8mMZjM=2750
_Tmq2I5Fa4KfTIlo5=True
_qzosHU2807Q=''
_I5Lq5wF5D=5
_L6LUXOrGKy='bgGaS9oCygoR8uaH'


def _DutUFHWsFg(_a,_b,_dummy1=None,_dummy2=0,_dummy3=False):
 _temp=_b
 while _temp:
  _a,_temp=_temp,_a%_temp
  _dummy_check=_dummy1 is None or _dummy2==0 or not _dummy3
  if not _dummy_check:
   pass
 return _a


def _TUPYYUlcV8BLp(_a,_m,_dummy1=None,_dummy2='',_dummy3=[]):
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


def _EuxEZ0dnXCk(_n,_dummy1=0,_dummy2=None):
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


def _aNqv6oF34lew(_n,_dummy1='',_dummy2=[]):
 if _n<=2:
  return 2
 _p=_n if _n%2!=0 else _n+1
 while not _EuxEZ0dnXCk(_p):
  _p += 2
 return _p


def _2wsfG5OD1je44xtK(_seed,_dummy1=None,_dummy2=0):
 _state=_seed&2147483647

 def _rng(_dummy3=False):
  nonlocal _state
  _state=1103515245*_state+12345&2147483647
  return _state
 return _rng


def _ML5NtAptdUwSK(_script_id,_key_salt,_dummy1=None,_dummy2=0,_dummy3=
 False):
 _seed_str=_script_id+':'+_key_salt
 _seed=int(_M0jiaG9Sv.sha256(_seed_str.encode('utf-8')).hexdigest(),16)
 _rng=_2wsfG5OD1je44xtK(_seed)
 _p=_aNqv6oF34lew(40000+_rng()%20000)
 _q=_aNqv6oF34lew(50000+_rng()%20000)
 if _p==_q:
  _q=_aNqv6oF34lew(_q+2)
 _n=_p*_q
 _phi=(_p-1)*(_q-1)
 _e_choices=[65537,257,17,5,3]
 _e=None
 for _cand in _e_choices:
  if _DutUFHWsFg(_cand,_phi)==1:
   _e=_cand
   break
 if _e is None:
  _e=3
  while _DutUFHWsFg(_e,_phi)!=1:
   _e += 2
 _d=_TUPYYUlcV8BLp(_e,_phi)
 if _d is None or _e is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 return _e,_d,_n


def _vAczIO8Vwu54cyop(_data,_d,_n,_dummy1=None):
 if _d is None or _n is None:
  raise RuntimeError('Decryption keys not available')
 return bytes([pow(int(_b),_d,_n) for _b in _data])


def _J9VuFNH9bTFvsuUK(_packed_bytes,_dummy1=''):
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
 return list(_Uno1ebJVVT81.unpack(_fmt,_packed_bytes))


def _2gYmKyIhQ9yG5X(_enc_b64,_dummy1=None):
 global _mHhpbgINt1VhOR,_EPXKZ1nRxxLKq0
 if _mHhpbgINt1VhOR is None or _EPXKZ1nRxxLKq0 is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_J9VuFNH9bTFvsuUK(_enc_bytes)
 return _vAczIO8Vwu54cyop(_enc_list,_mHhpbgINt1VhOR,_EPXKZ1nRxxLKq0
  ).decode('utf-8')


def _3gDKHSMa(_enc_b64,_dummy1=0):
 global _mHhpbgINt1VhOR,_EPXKZ1nRxxLKq0
 if _mHhpbgINt1VhOR is None or _EPXKZ1nRxxLKq0 is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_J9VuFNH9bTFvsuUK(_enc_bytes)
 return int(_vAczIO8Vwu54cyop(_enc_list,_mHhpbgINt1VhOR,
  _EPXKZ1nRxxLKq0).decode('utf-8'))


def _9Sra6s0sMWtQwMi(_seed,_dummy1=None):
 _rng=_2wsfG5OD1je44xtK(_seed)
 _key=bytearray(32)
 for _i in range(32):
  _key[_i]=_rng()%256
 return bytes(_key)


def _WQbuXyiNeisBHucr(_data,_key,_dummy1=None):
 if not isinstance(_data,bytes):
  _data=_data.encode('utf-8')
 if not isinstance(_key,bytes):
  _key=_key.encode('utf-8') if isinstance(_key,str) else bytes(_key)
 _key_hash=_M0jiaG9Sv.sha256(_key).digest()
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


def _tusssgRdB(_data,_key,_dummy1=0):
 return _WQbuXyiNeisBHucr(_data,_key)


def _rQE0MnEqI64S(_formula_id,_s,_n,_offset,_dummy1=None,_dummy2=0):
 if _formula_id==0:
  return len(_s)+_n+_offset
 if _formula_id==1:
  return (sum(ord(_c) for _c in _s)^_n)+_offset
 if _formula_id==2:
  return _n*(len(_s) or 1)+_offset
 if _formula_id==3:
  return sum(ord(_c) for _c in _s)+_n-_offset
 return -1


def _ypbcn8uOxp(_sock,_obj,_dummy1=None):
 _data=_ZORZWfEN.dumps(_obj,separators=(',',':')).encode('utf-8'
  )+b'\n'
 _sock.sendall(_data)


def _3tmBPNBNyQTnDf(_sock,_timeout,_dummy1=0,_dummy2=None):
 _buf=b''
 _start=_QmcQTrLEKRv2d.time()
 while True:
  if _QmcQTrLEKRv2d.time()-_start>_timeout:
   return None
  _chunk=_sock.recv(4096)
  if not _chunk:
   return None
  _buf += _chunk
  if b'\n' in _buf:
   _line,_=_buf.split(b'\n',1)
   if not _line:
    return None
   return _ZORZWfEN.loads(_line.decode('utf-8'))
  if len(_buf)>65536:
   return None


def _QamFM3wK(_metrics_data,_dummy1=None):
 global _EEhrtq7S
 if not _EEhrtq7S:
  return False
 try:
  import urllib.request
  import json
  _data=json.dumps(_metrics_data).encode('utf-8')
  _req=urllib.request.Request(_EEhrtq7S,data=_data,headers={
   'Content-Type':'application/json'},method='POST')
  try:
   _ctx=_gYpfMx2fS7J.create_default_context()
   _resp=urllib.request.urlopen(_req,timeout=5,context=_ctx)
   return _resp.getcode()==200
  except Exception:
   try:
    _ctx=_gYpfMx2fS7J._create_unverified_context()
    _resp=urllib.request.urlopen(_req,timeout=5,context=_ctx)
    return _resp.getcode()==200
   except Exception:
    return False
 except Exception:
  return False


def _oTywAU3L9(_detection_type,_dummy1=None,_dummy2=0):
 global _1a74q0dBW36srUz,_uKj8mMZjM,_Tmq2I5Fa4KfTIlo5,_qzosHU2807Q,_I5Lq5wF5D,_L6LUXOrGKy
 try:
  _sock=_bI4BpOWjojH.create_connection((_1a74q0dBW36srUz,
   _uKj8mMZjM),timeout=_I5Lq5wF5D)
  _ctx=_gYpfMx2fS7J.create_default_context()
  if not _Tmq2I5Fa4KfTIlo5:
   _ctx.check_hostname=False
   _ctx.verify_mode=_gYpfMx2fS7J.CERT_NONE
  elif _qzosHU2807Q:
   _ctx.load_verify_locations(_qzosHU2807Q)
  _ssock=_ctx.wrap_socket(_sock,server_hostname=_1a74q0dBW36srUz)
  _report_msg={'type':'debugger_detected','script_id':
   _L6LUXOrGKy,'detection_type':_detection_type}
  _ypbcn8uOxp(_ssock,_report_msg)
  _ssock.close()
 except Exception:
  pass


def _Xlo3GHEgRJeFi(_detection_type,_dummy1=None,_dummy2=0):
 _oTywAU3L9(_detection_type)
 _QmcQTrLEKRv2d.sleep(0.1)
 _SAr7vrLL17UFYM._exit(1)


def _4WqboZSBO(_dummy1=None,_dummy2=0,_dummy3=False):
 try:
  _ppid=_SAr7vrLL17UFYM.getppid()
  if _ppid==1:
   return 'orphaned_process'
  try:
   _result=_DoGdsFg6F1giqPd.run(['ps','-p',str(_ppid),'-o',
    'comm='],capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _parent_name=_result.stdout.strip().lower()
    _debugger_names=['lldb','gdb','debugserver','dtrace']
    for _name in _debugger_names:
     if _name in _parent_name:
      return 'parent_'+_name
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _JfW43kqZchq0(_dummy1=None):
 try:
  _ppid=_SAr7vrLL17UFYM.getppid()
  _result=_DoGdsFg6F1giqPd.run(['ps','-p',str(_ppid),'-o',
   'comm='],capture_output=True,text=True,timeout=1)
  if _result.returncode==0:
   _parent_name=_result.stdout.strip().lower()
   _debugger_names=['lldb','gdb','debugserver']
   for _name in _debugger_names:
    if _name in _parent_name:
     return 'process_tree_'+_name
 except Exception:
  pass
 return False


def _rll1pug8M(_dummy1=0,_dummy2=None):
 try:
  _pid=_SAr7vrLL17UFYM.getpid()
  _sysctl_path='proc.pid.'+str(_pid)+'.status'
  _result=_DoGdsFg6F1giqPd.run(['sysctl','-n',_sysctl_path],
   capture_output=True,text=True,timeout=1)
  if _result.returncode==0:
   _status=_result.stdout.strip()
   if 'traced' in _status.lower():
    return 'ptrace_traced'
 except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError,
  _DoGdsFg6F1giqPd.SubprocessError):
  pass
 except Exception:
  pass
 return False


def _A5K7V5wr5FrkmVSs(_dummy1=None,_dummy2=0):
 return False


def _6WkbudOU7mDFjdp(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_SAr7vrLL17UFYM.getpid()
  try:
   _result=_DoGdsFg6F1giqPd.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    if 'debugserver' in _result.stdout.lower():
     return 'lldb_lsof'
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_DoGdsFg6F1giqPd.run(['ps','aux'],capture_output=
    True,text=True,timeout=2)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'debugserver' in _line.lower():
      _attach_str1='--attach='+str(_pid)
      _attach_str2='--attach '+str(_pid)
      if _attach_str1 in _line or _attach_str2 in _line:
       return 'lldb_ps_attach'
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _fMaBwsNxQ6o4(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_SAr7vrLL17UFYM.getpid()
  try:
   _result=_DoGdsFg6F1giqPd.run(['ps','aux'],capture_output=
    True,text=True,timeout=2)
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
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_DoGdsFg6F1giqPd.run(['ps','-ax','-o',
    'pid,command'],capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    _lines=_output.split('\n')
    for _line in _lines:
     if '/usr/sbin/spindump -stdout' in _line:
      return 'spindump_stdout_psax'
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_DoGdsFg6F1giqPd.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    if 'sample' in _output or 'activity' in _output:
     return 'activity_monitor_lsof'
  except (_DoGdsFg6F1giqPd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _6gNVVqgbaZ4(_dummy1=None):
 global _a3QWKNvt,_P675O67KEUlBk,_MjoGkMPHMb
 while _a3QWKNvt:
  try:
   _getrusage=_GZDvgSj4v.getrusage(_GZDvgSj4v.RUSAGE_SELF)
   _current_cpu_time=_getrusage.ru_utime+_getrusage.ru_stime
   _current_time=_QmcQTrLEKRv2d.time()
   global _uBhj1SZNn
   _cpu_percent=0.0
   if _P675O67KEUlBk is not None and _MjoGkMPHMb is not None:
    _elapsed_time=_current_time-_MjoGkMPHMb
    if _elapsed_time>0:
     _cpu_delta=_current_cpu_time-_P675O67KEUlBk
     _cpu_percent=min(_cpu_delta/_elapsed_time*100.0,
      100.0)
   _P675O67KEUlBk=_current_cpu_time
   _MjoGkMPHMb=_current_time
   _metrics={'script_id':_L6LUXOrGKy,'hwid':_uBhj1SZNn,
    'cpu_usage':f'{_cpu_percent:.2f}%','memory_usage':
    f'{_getrusage.ru_maxrss/1024/1024:.2f} MB','timestamp':
    _current_time}
   _QamFM3wK(_metrics)
   _detection=_4WqboZSBO()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _detection=_JfW43kqZchq0()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _detection=_rll1pug8M()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _detection=_A5K7V5wr5FrkmVSs()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _detection=_6WkbudOU7mDFjdp()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _detection=_fMaBwsNxQ6o4()
   if _detection:
    _Xlo3GHEgRJeFi(_detection)
    break
   _QmcQTrLEKRv2d.sleep(0.5)
  except Exception:
   pass


def _NH66zfEB(_dummy1=0,_dummy2=None):
 _monitor_thread=_avZB3LPxzQfl6vLx.Thread(target=_6gNVVqgbaZ4,daemon=True
  )
 _monitor_thread.start()
 return _monitor_thread


def _5MXRFYeoqY():
 print(
  '\x1b[1;91m[Error]\x1b[0m Your script version is outdated. Please obtain the latest version.'
  )
 import sys
 sys.exit(1)


def _C3DOHln6WwBzy(_dummy1=None):
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
  _hwid=_M0jiaG9Sv.sha256(_combined.encode('utf-8')).hexdigest()[:32
   ].upper()
  return _hwid
 _fallback=f'{platform.node()}|{platform.system()}|{platform.machine()}'
 _hwid=_M0jiaG9Sv.sha256(_fallback.encode('utf-8')).hexdigest()[:32
  ].upper()
 return _hwid


def _LBVoFn2UbF4(_file_path):
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
  _profile={'code_hash':_M0jiaG9Sv.sha256(_code.encode('utf-8')).
   hexdigest(),'code_length':len(_code),'function_count':_code
   .count('def '),'import_count':_code.count('import ')}
  return _profile
 except Exception:
  return {'code_hash':'','code_length':0,'function_count':0,
   'import_count':0}


def _9uIM2rTf1qdU(_dummy1=None,_dummy2=0,_dummy3=False):
 global _mHhpbgINt1VhOR,_EPXKZ1nRxxLKq0,_uBhj1SZNn
 if _mHhpbgINt1VhOR is not None:
  raise RuntimeError('Handshake already completed')
 _script_id='bgGaS9oCygoR8uaH'
 _client_version='1.06'
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
  _code_profile=_LBVoFn2UbF4(None)
 else:
  _code_profile='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
 _hwid=None
 if True:
  _hwid=_C3DOHln6WwBzy()
 elif False:
  _hwid=None
 else:
  _hwid=_C3DOHln6WwBzy()
 _e,_d,_n=_ML5NtAptdUwSK(_script_id,_key_salt)
 if _e is None or _d is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 _sock=_bI4BpOWjojH.create_connection((_host,_port),timeout=_timeout)
 _ctx=_gYpfMx2fS7J.create_default_context()
 if not _verify_cert:
  _ctx.check_hostname=False
  _ctx.verify_mode=_gYpfMx2fS7J.CERT_NONE
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
 _ypbcn8uOxp(_ssock,_hello_msg)
 _resp=_3tmBPNBNyQTnDf(_ssock,_timeout)
 if not _resp:
  _ssock.close()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='outdated_version':
  _ssock.close()
  _5MXRFYeoqY()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='tamper_detected':
  _ssock.close()
  _5MXRFYeoqY()
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
  _sym_key_bytes=_vAczIO8Vwu54cyop(_sym_key_encrypted,_d,_n)
  if len(_sym_key_bytes)<32:
   raise RuntimeError('Invalid symmetric key length')
  _sym_key=bytes(_sym_key_bytes[:32])
  import base64
  _sym_enc_str=base64.b64decode(_enc_str_b64.encode('ascii') if
   isinstance(_enc_str_b64,str) else _enc_str_b64)
  _sym_enc_num=base64.b64decode(_enc_num_b64.encode('ascii') if
   isinstance(_enc_num_b64,str) else _enc_num_b64)
  _dec_str=_tusssgRdB(_sym_enc_str,_sym_key).decode('utf-8')
  _dec_num=int(_tusssgRdB(_sym_enc_num,_sym_key).decode('utf-8'))
 except Exception as _e:
  _ypbcn8uOxp(_ssock,{'type':'response','status':'failed',
   'reason':'decrypt_error'})
  _ssock.close()
  return False
 _solution=_rQE0MnEqI64S(_formula_id,_dec_str,_dec_num,_offset)
 _solution_str=str(_solution)
 _client_md5=_M0jiaG9Sv.md5(_solution_str.encode('utf-8')).hexdigest()
 if _client_md5!=_expected_md5:
  _ypbcn8uOxp(_ssock,{'type':'response','status':'failed',
   'client_md5':_client_md5})
  _ssock.close()
  return False
 _ypbcn8uOxp(_ssock,{'type':'response','status':'ok','solution':
  _solution_str,'client_md5':_client_md5})
 _final=_3tmBPNBNyQTnDf(_ssock,_timeout)
 _ssock.close()
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='outdated_version':
  _5MXRFYeoqY()
  return False
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='tamper_detected':
  _5MXRFYeoqY()
  return False
 if _final and _final.get('status')=='ok':
  _mHhpbgINt1VhOR=_d
  _EPXKZ1nRxxLKq0=_n
  global _uBhj1SZNn
  _uBhj1SZNn=_hwid
  return True
 return False


_NH66zfEB()
if not _9uIM2rTf1qdU():
 raise SystemExit(1)
import base64
import json
import random
import struct
import time
from dataclasses import dataclass
from typing import Any,Dict,List,Optional


def _base64url_decode(data:str) ->bytes:
 padding=_2gYmKyIhQ9yG5X('+EPyzA==')*(-len(data)%_3gDKHSMa('CIEKEw==')
  )
 return base64.urlsafe_b64decode(data+padding)


def _build_rsa_public_key(jwk:Dict[str,str]):
 try:
  from cryptography.hazmat.primitives.asymmetric import rsa
 except ImportError as exc:
  raise RuntimeError(_2gYmKyIhQ9yG5X(
   'JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='
   )) from exc
 n=int.from_bytes(_base64url_decode(jwk[_2gYmKyIhQ9yG5X('Joorzg==')]),
  _2gYmKyIhQ9yG5X('4fbgJss1trsoF9VX'))
 e=int.from_bytes(_base64url_decode(jwk[_2gYmKyIhQ9yG5X('qTswzg==')]),
  _2gYmKyIhQ9yG5X('4fbgJss1trsoF9VX'))
 return rsa.RSAPublicNumbers(e,n).public_key()


def _build_key_provider(provider_id:str,key_id:str,public_key):
 try:
  from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider,WrappingKey
  from aws_encryption_sdk.identifiers import EncryptionKeyType,WrappingAlgorithm
  from cryptography.hazmat.primitives import serialization
 except ImportError as exc:
  raise RuntimeError(_2gYmKyIhQ9yG5X(
   'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
   )) from exc
 provider_id_value=provider_id
 key_id_bytes=key_id.encode(_2gYmKyIhQ9yG5X(
  'aKpbAPZ/QUbUMBAA0Osqb0jWV1w='))


 class _Provider(RawMasterKeyProvider):
  provider_id=provider_id_value

  def _get_raw_key(self,key_id_to_find):
   if key_id_to_find!=key_id_bytes:
    raise KeyError(_2gYmKyIhQ9yG5X(
     'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwW2y2W4qTswzmuz1b1FLKsFyzW2u2iBbc/RKpJP'
     )+str(key_id_to_find))
   public_key_pem=public_key.public_bytes(encoding=serialization
    .Encoding.PEM,format=serialization.PublicFormat.
    SubjectPublicKeyInfo)
   return WrappingKey(wrapping_algorithm=WrappingAlgorithm.
    RSA_OAEP_SHA256_MGF1,wrapping_key=public_key_pem,
    wrapping_key_type=EncryptionKeyType.PUBLIC)

  def _list_key_ids(self):
   return [key_id_bytes]
 provider=_Provider()
 provider.add_master_key(key_id_bytes)
 return provider


@dataclass
class DataType:
 data_type_id:str
 jwk_public_key:Dict[str,str]
 provider_id:str
 key_id:str
 _provider:Any=None

 def get_provider(self):
  if self._provider is None:
   public_key=_build_rsa_public_key(self.jwk_public_key)
   self._provider=_build_key_provider(self.provider_id,self.
    key_id,public_key)
  return self._provider


XXTEA_DELTA=_3gDKHSMa(
 'rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
FWCIM_KEY=[_3gDKHSMa(
 't0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),_3gDKHSMa(
 'rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),_3gDKHSMa(
 'rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),_3gDKHSMa(
 'SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]


def _to_uint32(x:int) ->int:
 return x&_3gDKHSMa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')


def _to_int32(x:int) ->int:
 x=x&_3gDKHSMa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 return x-_3gDKHSMa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
  ) if x>=_3gDKHSMa(
  'rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA==') else x


def _xxtea_mx(z:int,y:int,sum_val:int,key:List[int],p:int,e:int
 ) ->int:
 return _to_uint32((z>>_3gDKHSMa('IBQbTQ==')^y<<_3gDKHSMa(
  'rkMOsQ=='))+(y>>_3gDKHSMa('S/wQmQ==')^z<<_3gDKHSMa(
  'CIEKEw=='))^(sum_val^y)+(key[p&_3gDKHSMa('S/wQmQ==')^e]^z)
  )


def UHUyo(data:bytes,key:List[int]) ->bytes:
 _2gYmKyIhQ9yG5X(
  'ximjkMYpo5CiPuwMo4Ah07smMj1FLKsFqTswziaKK84m3EaclH5HPGuz1b2tcPBl9n9BRkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBTbRGQPLNba79n9BRm2b8aBFLKsFt0mqG65DDrFI1ldc0Osqb+H24CbLNba79n9BRkUsqwW2y2W4qTswzmuz1b1FLKsFuBAMgAiBChNFLKsFPrBBtkUsqwVoqlsAyzW2uyaKK872f0FGS/wQma5DDrH+K3bFyOrZIg=='
  )
 padding=(_3gDKHSMa('CIEKEw==')-len(data)%_3gDKHSMa('CIEKEw==')
  )%_3gDKHSMa('CIEKEw==')
 if padding:
  data=data+b'\x00'*padding
 n=len(data)//_3gDKHSMa('CIEKEw==')
 v=list(struct.unpack(_2gYmKyIhQ9yG5X('ULqlhA==')+str(n) +
  _2gYmKyIhQ9yG5X('AS7Agw=='),data))
 if n<_3gDKHSMa('rkMOsQ=='):
  v.append(_3gDKHSMa('t8YL1g=='))
  n=_3gDKHSMa('rkMOsQ==')
 rounds=_3gDKHSMa('WFwvMQ==')+_3gDKHSMa('IBQbTa5DDrE=')//n
 sum_val=_3gDKHSMa('t8YL1g==')
 z=v[n-_3gDKHSMa('t0mqGw==')]
 for _ in range(rounds):
  sum_val=_to_uint32(sum_val+XXTEA_DELTA)
  e=sum_val>>_3gDKHSMa('rkMOsQ==')&_3gDKHSMa('S/wQmQ==')
  for p in range(n-_3gDKHSMa('t0mqGw==')):
   y=v[p+_3gDKHSMa('t0mqGw==')]
   v[p]=_to_uint32(v[p]+_xxtea_mx(z,y,sum_val,key,p,e))
   z=v[p]
  y=v[_3gDKHSMa('t8YL1g==')]
  v[n-_3gDKHSMa('t0mqGw==')]=_to_uint32(v[n-_3gDKHSMa(
   't0mqGw==')]+_xxtea_mx(z,y,sum_val,key,n-_3gDKHSMa(
   't0mqGw=='),e))
  z=v[n-_3gDKHSMa('t0mqGw==')]
 return struct.pack(_2gYmKyIhQ9yG5X('ULqlhHDJeSZdHeUzAS7Agw==')%n,*v)


def _build_crc32_table() ->List[int]:
 table=[]
 for i in range(_3gDKHSMa('rkMOsSAUG01YXC8x')):
  crc=i
  for _ in range(_3gDKHSMa('SNZXXA==')):
   crc=crc>>_3gDKHSMa('t0mqGw==')^_3gDKHSMa(
    'S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw=='
    ) if crc&_3gDKHSMa('t0mqGw==') else crc>>_3gDKHSMa(
    't0mqGw==')
  table.append(_to_int32(crc))
 return table


CRC32_TABLE=_build_crc32_table()


def crc32(data:str) ->int:
 _2gYmKyIhQ9yG5X(
  'K6xhxiUfBjqi/bquJtxGnGiqWwCi/bquJR8GOvZ/QUapOzDORSyrBSusYcbKhTSsK6xhxkv8EJmuQw6xRSyrBW018wQlHwY69n9BRibcRpxtm/GgyzW2uyaKK84oF9VXRSyrBSfCXp/33d1fK6xhxgEuwIM00CVjiXsnd10d5TNFLKsFyzW2u2018wStcPBlov26rqk7MM5tNfMEqTswziaKK872f0FGJR8GOvZ/QUbLNba79jbVPiaKK87I6tki'
  )
 crc=_3gDKHSMa('CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 for char in data:
  crc=_to_uint32(crc>>_3gDKHSMa('SNZXXA==')^CRC32_TABLE[(crc ^
   ord(char))&_3gDKHSMa('rkMOsSAUG00gFBtN')])
 return _to_int32(crc^_3gDKHSMa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='))


def int_to_hex(value:int) ->str:
 _2gYmKyIhQ9yG5X(
  'K6xhxvY21T4miivORui3U6k7MM6Ufkc89n9BRkUsqwVdHeUzyzW2uygX1VcmiivOqTswzmiBbc9FLKsFyzW2uyaKK872f0FGS/wQma5DDrFFLKsF9n9BRvY21T5FLKsFSNZXXNDrKm8m3EacbZvxoCUfBjqUfkc8RSyrBWiqWwCtcPBlrXDwZak7MM6Ufkc8JtxGnCUfBjpdHeUzqTswzkUsqwVtm/GgqTswzj6wQbbI6tki'
  )
 if value<_3gDKHSMa('t8YL1g=='):
  value=value+_3gDKHSMa(
   'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ==')
 return format(value,_2gYmKyIhQ9yG5X('t8YL1kjWV1zGKaOQ'))


def generate_fingerprint(url:str=_2gYmKyIhQ9yG5X(
 'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'
 ),user_agent:str=_2gYmKyIhQ9yG5X(
 'zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='
 ),screen_width:int=_3gDKHSMa('t0mqG7fGC9ZI1ldct8YL1g=='),
 screen_height:int=_3gDKHSMa('t0mqG0u+srquQw6xt8YL1g=='),
 timezone_offset:int=-_3gDKHSMa('SNZXXA==')) ->Dict[str,Any]:
 _2gYmKyIhQ9yG5X(
  'pq8QKak7MM4miivOqTswzpR+RzwlHwY69n9BRqk7MM5FLKsFaIFtz6k7MM5G6LdTyzW2uybcRpypOzDORSyrBdQwEADLNba7JoorzigX1VepOzDOlH5HPK1w8GWUfkc8yzW2uyaKK872f0FGRSyrBWiBbc8lHwY69n9BRiUfBjpFLKsFXR3lM/Z/QUaUfkc8aKpbACbcRpz2f0FGaKpbAJR+RzypOzDOyOrZIg=='
  )
 now=int(time.time()*_3gDKHSMa('t0mqG7fGC9a3xgvWt8YL1g=='))
 start_time=now-random.randint(_3gDKHSMa('t0mqG7fGC9a3xgvWt8YL1g=='),
  _3gDKHSMa('IBQbTbfGC9a3xgvWt8YL1g=='))
 return {_2gYmKyIhQ9yG5X('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{
  _2gYmKyIhQ9yG5X('qTswzqL9uq4='):_3gDKHSMa('t0mqGw=='),
  _2gYmKyIhQ9yG5X('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):_3gDKHSMa(
  't8YL1g=='),_2gYmKyIhQ9yG5X('bZvxoA=='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('4fbgJiUfBjr2f0FG9n9BRg=='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('rXDwZak7MM6Ufkc81DAQAA=='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('JR8GOmiqWwD2f0FG9jbVPg=='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz'):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X('KBfVV61w8GVoqlsA'):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X('aIFtzyaKK872f0FG'):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X('bTXzBCUfBjr2f0FGbZvxoA=='):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X('1DAQAK1w8GWuQw6x'):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X(
  'ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('9n9BRnIals0='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='):
  _3gDKHSMa('t8YL1g==')},_2gYmKyIhQ9yG5X(
  'XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):start_time,_2gYmKyIhQ9yG5X(
  'yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{
  _2gYmKyIhQ9yG5X('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):random.randint
  (_3gDKHSMa('t8YL1g=='),_3gDKHSMa('S/wQmQ==')),_2gYmKyIhQ9yG5X(
  '9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):random.randint(
  _3gDKHSMa('t8YL1g=='),_3gDKHSMa('IBQbTQ==')),_2gYmKyIhQ9yG5X(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):random
  .randint(_3gDKHSMa('IBQbTQ=='),_3gDKHSMa('rkMOsbfGC9Y=')),
  _2gYmKyIhQ9yG5X('JtxGnGiqWwD2f0FGXR3lMw=='):_3gDKHSMa('t8YL1g=='),
  _2gYmKyIhQ9yG5X('JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):_3gDKHSMa(
  't8YL1g=='),_2gYmKyIhQ9yG5X('rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):
  _3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'
  ):[],_2gYmKyIhQ9yG5X(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='
  ):[],_2gYmKyIhQ9yG5X(
  'tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],
  _2gYmKyIhQ9yG5X(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],
  _2gYmKyIhQ9yG5X(
  '9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]
  },_2gYmKyIhQ9yG5X('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{
  _2gYmKyIhQ9yG5X(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[
  _2gYmKyIhQ9yG5X(
  'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw=='
  )],_2gYmKyIhQ9yG5X(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):
  [random.randint(-_3gDKHSMa(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _3gDKHSMa(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==')) for _ in
  range(_3gDKHSMa('t0mqG7fGC9Y='))],_2gYmKyIhQ9yG5X(
  'qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw=='):random.randint(
  _3gDKHSMa('t0mqGw=='),_3gDKHSMa('t0mqG7fGC9Y=')),_2gYmKyIhQ9yG5X(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'
  ):_3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='
  ):_3gDKHSMa('t0mqG7fGC9Y=')},_2gYmKyIhQ9yG5X(
  'bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{_2gYmKyIhQ9yG5X(
  'ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):random.randint(_3gDKHSMa(
  't0mqGw=='),_3gDKHSMa('rkMOsbfGC9Y='))},_2gYmKyIhQ9yG5X(
  '4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},_2gYmKyIhQ9yG5X(
  'rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{
  _2gYmKyIhQ9yG5X('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{
  _2gYmKyIhQ9yG5X(
  'JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):
  start_time-_3gDKHSMa('t0mqG7fGC9a3xgvWt8YL1g=='),_2gYmKyIhQ9yG5X
  (
  'XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):_3gDKHSMa('t8YL1g=='),_2gYmKyIhQ9yG5X(
  'aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):
  start_time-_3gDKHSMa('WFwvMbdJqhu3xgvW'),_2gYmKyIhQ9yG5X(
  'JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):start_time-_3gDKHSMa('t0mqG7fGC9a3xgvWIBQbTQ=='),
  _2gYmKyIhQ9yG5X(
  'ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'):
  start_time-_3gDKHSMa('WFwvMbfGC9a3xgvW'),_2gYmKyIhQ9yG5X(
  'lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):
  start_time-_3gDKHSMa('GzcVh7fGC9a3xgvW'),_2gYmKyIhQ9yG5X(
  '1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):
  start_time-_3gDKHSMa('t0mqG7fGC9a3xgvWt8YL1g==')}},
  _2gYmKyIhQ9yG5X(
  'JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{
  _2gYmKyIhQ9yG5X('NtEZA2iBbc8='):{_2gYmKyIhQ9yG5X(
  'rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw=='):{
  _2gYmKyIhQ9yG5X('aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],
  _2gYmKyIhQ9yG5X('NtEZA8s1trsmiivOaIFtz/Y21T420RkD'):[],
  _2gYmKyIhQ9yG5X('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):
  []}},_2gYmKyIhQ9yG5X('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):
  {_2gYmKyIhQ9yG5X(
  'rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw=='):{
  _2gYmKyIhQ9yG5X('NtEZA8s1trsmiivOaIFtz/Y21T420RkD'):[]}}},
  _2gYmKyIhQ9yG5X('qTswziaKK85ogW3P'):now,_2gYmKyIhQ9yG5X(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz'):
  {_2gYmKyIhQ9yG5X('JtxGnF0d5TNdHeUz'):{_2gYmKyIhQ9yG5X(
  '9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):
  _3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  '993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='
  ):_3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  '4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):_3gDKHSMa(
  't0mqGw=='),_2gYmKyIhQ9yG5X(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):
  _3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):
  _3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  '9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):_3gDKHSMa('t0mqGw=='),
  _2gYmKyIhQ9yG5X('9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):
  _3gDKHSMa('t0mqGw=='),_2gYmKyIhQ9yG5X(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):
  _3gDKHSMa('t0mqGw==')},_2gYmKyIhQ9yG5X('dHiepV0d5TM='):{
  _2gYmKyIhQ9yG5X('JR8GOmiqWwBogW3PyzW2u/Y21T4='):True,
  _2gYmKyIhQ9yG5X(
  'KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):
  True,_2gYmKyIhQ9yG5X(
  'ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):
  _2gYmKyIhQ9yG5X('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),
  _2gYmKyIhQ9yG5X('9n9BRvY21T5oqlsAJtxGnG2b8aA='):True,
  _2gYmKyIhQ9yG5X('Rui3U8s1trtogW3PqTswzvY21T4='):True,
  _2gYmKyIhQ9yG5X('NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):
  True},_2gYmKyIhQ9yG5X('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw=='):
  _3gDKHSMa('t8YL1g==')},_2gYmKyIhQ9yG5X('KBfVV61w8GVoqlsA'):{
  _2gYmKyIhQ9yG5X('Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):
  _2gYmKyIhQ9yG5X('Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),
  _2gYmKyIhQ9yG5X('bTXzBPY21T5ogW3PqTswzqL9uq4='):_2gYmKyIhQ9yG5X(
  'uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'
  ),_2gYmKyIhQ9yG5X(
  'qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[
  _2gYmKyIhQ9yG5X(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='
  ),_2gYmKyIhQ9yG5X(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG'
  )]},_2gYmKyIhQ9yG5X('aIFtzyaKK872f0FG'):None,_2gYmKyIhQ9yG5X(
  'bTXzBCUfBjr2f0FGbZvxoA=='):{_2gYmKyIhQ9yG5X('9n9BRiUfBjomiivO'):
  _2gYmKyIhQ9yG5X(
  '0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='
  ),_2gYmKyIhQ9yG5X('XR3lM8s1trsmiivO'):_2gYmKyIhQ9yG5X(
  't8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'
  ),_2gYmKyIhQ9yG5X('JtxGnPY21T5dHeUz'):_2gYmKyIhQ9yG5X(
  '0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw=='
  )},_2gYmKyIhQ9yG5X(
  '1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):
  None,_2gYmKyIhQ9yG5X('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):
  '',_2gYmKyIhQ9yG5X(
  'aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):
  '',_2gYmKyIhQ9yG5X(
  'XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):
  _2gYmKyIhQ9yG5X(
  'yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw=='
  ).format(screen_width,screen_height,screen_height),
  _2gYmKyIhQ9yG5X('ov26rl0d5TM8XXep4fbgJss1trtogW3P'):
  _2gYmKyIhQ9yG5X('ximjkA==')+str(random.randint(_3gDKHSMa(
  't0mqG7fGC9Y='),_3gDKHSMa('S76yuku+sro=')))+_2gYmKyIhQ9yG5X(
  '0Osqbw==')+str(random.randint(_3gDKHSMa(
  't0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),_3gDKHSMa(
  'S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==')))+_2gYmKyIhQ9yG5X(
  '0Osqbw==')+str(random.randint(_3gDKHSMa(
  't0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),_3gDKHSMa(
  'S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==')))+_2gYmKyIhQ9yG5X(
  '0SqSTw==')+str(now),_2gYmKyIhQ9yG5X(
  '9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):timezone_offset,
  _2gYmKyIhQ9yG5X('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):
  url,_2gYmKyIhQ9yG5X(
  'aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):user_agent,
  _2gYmKyIhQ9yG5X('ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):
  url,_2gYmKyIhQ9yG5X(
  'NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):False,
  _2gYmKyIhQ9yG5X('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],
  _2gYmKyIhQ9yG5X('Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):
  _2gYmKyIhQ9yG5X('CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}


def fff(fingerprint:Optional[Dict[str,Any]]=None) ->str:
 _2gYmKyIhQ9yG5X(
  'GP33oEUsqwWmrxApqTswziaKK86pOzDOlH5HPCUfBjr2f0FGqTswzkUsqwUm3Eac9jbVPm018wStcPBlov26rqk7MM72f0FGqTswzkUsqwUnwl6f993dXyusYcYBLsCDNNAlY0UsqwVtNfMEqTswzvZ/QUYlHwY6aIFtzyUfBjr2f0FGJR8GOrdJqhtFLKsFrXDwZSUfBjprs9W9ov26rvY21T4lHwY6aIFtz8jq2SIY/fegGP33oEUsqwXKhTSsqTswzvZ/QUZoqlsAlH5HPCaKK85dHeUz0SqSTxj996BFLKsFRSyrBRSR5nj2f0FGlH5HPMs1trsmiivOKBfVV0UsqwXLNba7JoorzkUsqwXUMBAA9jbVPpR+RzxtNfMEJR8GOvZ/QUbRKpJPL92fsKOAIdMrrGHGaIFtzwEuwIOiPuwMqTswziusYcZdHeUz0SqST6PJ7Du7JjI9FJHmeKOAIdNYXC8xCIEKE8jq2SLI6tkiyOrZIi/dn7AY/fegRSyrBQ=='
  )
 if fingerprint is None:
  fingerprint=generate_fingerprint()
 json_str=json.dumps(fingerprint,separators=(_2gYmKyIhQ9yG5X(
  'kH10Dw=='),_2gYmKyIhQ9yG5X('0SqSTw==')))
 crc=crc32(json_str)
 hex_crc=int_to_hex(crc)
 combined=_2gYmKyIhQ9yG5X('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(hex_crc,
  json_str)
 encrypted=UHUyo(combined.encode(_2gYmKyIhQ9yG5X(
  'aKpbAPZ/QUbUMBAA0Osqb0jWV1w=')),FWCIM_KEY)
 b64=base64.b64encode(encrypted).decode(_2gYmKyIhQ9yG5X(
  'JR8GOl0d5TMm3EacyzW2u8s1trs='))
 return _2gYmKyIhQ9yG5X('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP'
  )+str(b64)


class ggg:

 def __init__(self):
  self._data_types:Dict[str,DataType]={}
  self._profiles:Dict[str,Dict[str,Any]]={}

 def add_profile(self,name:str,fields:Dict[str,Any]) ->None:
  self._profiles[name]=fields

 def add_data_type(self,*,data_type_id:str,jwk_public_key:Dict[str,
  str],provider_id:str,key_id:str) ->None:
  self._data_types[data_type_id]=DataType(data_type_id=data_type_id,
   jwk_public_key=jwk_public_key,provider_id=provider_id,key_id=
   key_id)

 def encrypt_string(self,value:str,*,data_type_id:str,
  requires_tail:bool=False,encryption_context:Optional[Dict[str,
  str]]=None) ->str:
  try:
   from aws_encryption_sdk import EncryptionSDKClient,CommitmentPolicy
   from aws_encryption_sdk.identifiers import Algorithm
  except ImportError as exc:
   raise RuntimeError(_2gYmKyIhQ9yG5X(
    'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
    )) from exc
  if data_type_id not in self._data_types:
   raise KeyError(_2gYmKyIhQ9yG5X(
    'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP'
    )+str(data_type_id))
  data_type=self._data_types[data_type_id]
  key_provider=data_type.get_provider()
  plaintext=value.encode(_2gYmKyIhQ9yG5X(
   'aKpbAPZ/QUbUMBAA0Osqb0jWV1w='))
  context=encryption_context or {}
  client=EncryptionSDKClient(commitment_policy=CommitmentPolicy.
   FORBID_ENCRYPT_ALLOW_DECRYPT)
  ciphertext,_header=client.encrypt(source=plaintext,key_provider
   =key_provider,encryption_context=context,frame_length=
   _3gDKHSMa('t8YL1g=='),algorithm=Algorithm.AES_128_GCM_IV12_TAG16)
  encoded=base64.b64encode(ciphertext).decode(_2gYmKyIhQ9yG5X(
   'JR8GOl0d5TMm3EacyzW2u8s1trs='))
  if requires_tail:
   tail=''.join(ch for ch in value if ch not in _2gYmKyIhQ9yG5X(
    'RSyrBdDrKm8='))[-_3gDKHSMa('CIEKEw=='):]
   if len(tail)>_3gDKHSMa('S/wQmQ=='):
    encoded += _2gYmKyIhQ9yG5X('/wOKvg==')+tail
  return encoded
### This file is protected by SpiwalSec Obfuscator ~ SID: XKdXz7PxIt ###
import socket as _OBSD72FLio
import ssl as _ObskV6CNqLo9
import json as _pMVRBX4NnKIWO
import hashlib as _wCMc0uBY8CRRFRM
import time as _gzqcfwG9BZnNBXV
import struct as _7omU26nt3Y
import os as _tA05Sitge
import subprocess as _XSnEBBn13uqZd
import threading as _A0JBvFQ6rOW
import platform as _DagoFBEHKqCV2Rta
import resource as _5fZe33tq
_tX0VFat5ETWiEqN2=None
_jZeewh6e4ZmrE2=None
_YuvQlCs3SBsNMqy=True
_qBBguNSB439wlp='https://spinnyspiwal.com:443/api/metrics'
_z6yLhZaAz=None
_gkBNckzdX1HpH=None
_5j23LuZrrkI9MUEo=None
_zZj803YzikkfuQ='spinnyspiwal.com'
_VoEv2cBmAYr5R=2750
_trD9RTvqVJ1R2=True
_1J0ePQzhE5nJt=''
_OVfG9cG15=5
_rDUJkopjRj='bgGaS9oCygoR8uaH'


def _gW9NzO2M9EuWuE(_a,_b,_dummy1=None,_dummy2=0,_dummy3=False):
 _temp=_b
 while _temp:
  _a,_temp=_temp,_a%_temp
  _dummy_check=_dummy1 is None or _dummy2==0 or not _dummy3
  if not _dummy_check:
   pass
 return _a


def _FJb3kT3TeQLwsqVI(_a,_m,_dummy1=None,_dummy2='',_dummy3=[]):
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


def _VpBYFNU77I0f(_n,_dummy1=0,_dummy2=None):
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


def _eHl1JBdgAo(_n,_dummy1='',_dummy2=[]):
 if _n<=2:
  return 2
 _p=_n if _n%2!=0 else _n+1
 while not _VpBYFNU77I0f(_p):
  _p += 2
 return _p


def _f942gXWFHNjQ(_seed,_dummy1=None,_dummy2=0):
 _state=_seed&2147483647

 def _rng(_dummy3=False):
  nonlocal _state
  _state=1103515245*_state+12345&2147483647
  return _state
 return _rng


def _7GFlZc5FRuwNZ(_script_id,_key_salt,_dummy1=None,_dummy2=0,_dummy3=
 False):
 _seed_str=_script_id+':'+_key_salt
 _seed=int(_wCMc0uBY8CRRFRM.sha256(_seed_str.encode('utf-8')).
  hexdigest(),16)
 _rng=_f942gXWFHNjQ(_seed)
 _p=_eHl1JBdgAo(40000+_rng()%20000)
 _q=_eHl1JBdgAo(50000+_rng()%20000)
 if _p==_q:
  _q=_eHl1JBdgAo(_q+2)
 _n=_p*_q
 _phi=(_p-1)*(_q-1)
 _e_choices=[65537,257,17,5,3]
 _e=None
 for _cand in _e_choices:
  if _gW9NzO2M9EuWuE(_cand,_phi)==1:
   _e=_cand
   break
 if _e is None:
  _e=3
  while _gW9NzO2M9EuWuE(_e,_phi)!=1:
   _e += 2
 _d=_FJb3kT3TeQLwsqVI(_e,_phi)
 if _d is None or _e is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 return _e,_d,_n


def _wmdx2pC6(_data,_d,_n,_dummy1=None):
 if _d is None or _n is None:
  raise RuntimeError('Decryption keys not available')
 return bytes([pow(int(_b),_d,_n) for _b in _data])


def _KoUPgvdvfnBebJ(_packed_bytes,_dummy1=''):
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
 return list(_7omU26nt3Y.unpack(_fmt,_packed_bytes))


def _w6q9IM0RsXquXZ(_enc_b64,_dummy1=None):
 global _tX0VFat5ETWiEqN2,_jZeewh6e4ZmrE2
 if _tX0VFat5ETWiEqN2 is None or _jZeewh6e4ZmrE2 is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_KoUPgvdvfnBebJ(_enc_bytes)
 return _wmdx2pC6(_enc_list,_tX0VFat5ETWiEqN2,_jZeewh6e4ZmrE2).decode(
  'utf-8')


def _oGMFXfpaJeNBJx(_enc_b64,_dummy1=0):
 global _tX0VFat5ETWiEqN2,_jZeewh6e4ZmrE2
 if _tX0VFat5ETWiEqN2 is None or _jZeewh6e4ZmrE2 is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_KoUPgvdvfnBebJ(_enc_bytes)
 return int(_wmdx2pC6(_enc_list,_tX0VFat5ETWiEqN2,_jZeewh6e4ZmrE2).
  decode('utf-8'))


def _3z1QjixiFN0(_seed,_dummy1=None):
 _rng=_f942gXWFHNjQ(_seed)
 _key=bytearray(32)
 for _i in range(32):
  _key[_i]=_rng()%256
 return bytes(_key)


def _DfxELxv5xnMQ(_data,_key,_dummy1=None):
 if not isinstance(_data,bytes):
  _data=_data.encode('utf-8')
 if not isinstance(_key,bytes):
  _key=_key.encode('utf-8') if isinstance(_key,str) else bytes(_key)
 _key_hash=_wCMc0uBY8CRRFRM.sha256(_key).digest()
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


def _9txvckivEaAhFK(_data,_key,_dummy1=0):
 return _DfxELxv5xnMQ(_data,_key)


def _6kMsAYXVN(_formula_id,_s,_n,_offset,_dummy1=None,_dummy2=0):
 if _formula_id==0:
  return len(_s)+_n+_offset
 if _formula_id==1:
  return (sum(ord(_c) for _c in _s)^_n)+_offset
 if _formula_id==2:
  return _n*(len(_s) or 1)+_offset
 if _formula_id==3:
  return sum(ord(_c) for _c in _s)+_n-_offset
 return -1


def _V96OE7S0kDa9D9(_sock,_obj,_dummy1=None):
 _data=_pMVRBX4NnKIWO.dumps(_obj,separators=(',',':')).encode('utf-8'
  )+b'\n'
 _sock.sendall(_data)


def _uGBQEsmY0o(_sock,_timeout,_dummy1=0,_dummy2=None):
 _buf=b''
 _start=_gzqcfwG9BZnNBXV.time()
 while True:
  if _gzqcfwG9BZnNBXV.time()-_start>_timeout:
   return None
  _chunk=_sock.recv(4096)
  if not _chunk:
   return None
  _buf += _chunk
  if b'\n' in _buf:
   _line,_=_buf.split(b'\n',1)
   if not _line:
    return None
   return _pMVRBX4NnKIWO.loads(_line.decode('utf-8'))
  if len(_buf)>65536:
   return None


def _0WzHaCI0T1j3H(_metrics_data,_dummy1=None):
 global _qBBguNSB439wlp
 if not _qBBguNSB439wlp:
  return False
 try:
  import urllib.request
  import json
  _data=json.dumps(_metrics_data).encode('utf-8')
  _req=urllib.request.Request(_qBBguNSB439wlp,data=_data,headers=
   {'Content-Type':'application/json'},method='POST')
  try:
   _ctx=_ObskV6CNqLo9.create_default_context()
   _resp=urllib.request.urlopen(_req,timeout=5,context=_ctx)
   return _resp.getcode()==200
  except Exception:
   try:
    _ctx=_ObskV6CNqLo9._create_unverified_context()
    _resp=urllib.request.urlopen(_req,timeout=5,context=_ctx)
    return _resp.getcode()==200
   except Exception:
    return False
 except Exception:
  return False


def _19VFsKWCzCKQ2ndt(_detection_type,_dummy1=None,_dummy2=0):
 global _zZj803YzikkfuQ,_VoEv2cBmAYr5R,_trD9RTvqVJ1R2,_1J0ePQzhE5nJt,_OVfG9cG15,_rDUJkopjRj
 try:
  _sock=_OBSD72FLio.create_connection((_zZj803YzikkfuQ,
   _VoEv2cBmAYr5R),timeout=_OVfG9cG15)
  _ctx=_ObskV6CNqLo9.create_default_context()
  if not _trD9RTvqVJ1R2:
   _ctx.check_hostname=False
   _ctx.verify_mode=_ObskV6CNqLo9.CERT_NONE
  elif _1J0ePQzhE5nJt:
   _ctx.load_verify_locations(_1J0ePQzhE5nJt)
  _ssock=_ctx.wrap_socket(_sock,server_hostname=_zZj803YzikkfuQ)
  _report_msg={'type':'debugger_detected','script_id':
   _rDUJkopjRj,'detection_type':_detection_type}
  _V96OE7S0kDa9D9(_ssock,_report_msg)
  _ssock.close()
 except Exception:
  pass


def _WH9BFwgfYpwcI(_detection_type,_dummy1=None,_dummy2=0):
 _19VFsKWCzCKQ2ndt(_detection_type)
 _gzqcfwG9BZnNBXV.sleep(0.1)
 _tA05Sitge._exit(1)


def _N5f16CAmXrPN(_dummy1=None,_dummy2=0,_dummy3=False):
 try:
  _ppid=_tA05Sitge.getppid()
  if _ppid==1:
   return 'orphaned_process'
  try:
   _result=_XSnEBBn13uqZd.run(['ps','-p',str(_ppid),'-o',
    'comm='],capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _parent_name=_result.stdout.strip().lower()
    _debugger_names=['lldb','gdb','debugserver','dtrace']
    for _name in _debugger_names:
     if _name in _parent_name:
      return 'parent_'+_name
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _uKUShwpvfRCtWDMg(_dummy1=None):
 try:
  _ppid=_tA05Sitge.getppid()
  _result=_XSnEBBn13uqZd.run(['ps','-p',str(_ppid),'-o','comm='
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


def _IPl1lEIuui2vjDX6(_dummy1=0,_dummy2=None):
 try:
  _pid=_tA05Sitge.getpid()
  _sysctl_path='proc.pid.'+str(_pid)+'.status'
  _result=_XSnEBBn13uqZd.run(['sysctl','-n',_sysctl_path],
   capture_output=True,text=True,timeout=1)
  if _result.returncode==0:
   _status=_result.stdout.strip()
   if 'traced' in _status.lower():
    return 'ptrace_traced'
 except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError,
  _XSnEBBn13uqZd.SubprocessError):
  pass
 except Exception:
  pass
 return False


def _yzik5BDnaLQ(_dummy1=None,_dummy2=0):
 return False


def _8tNuRpRZs(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_tA05Sitge.getpid()
  try:
   _result=_XSnEBBn13uqZd.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    if 'debugserver' in _result.stdout.lower():
     return 'lldb_lsof'
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_XSnEBBn13uqZd.run(['ps','aux'],capture_output=True,
    text=True,timeout=2)
   if _result.returncode==0:
    for _line in _result.stdout.split('\n'):
     if 'debugserver' in _line.lower():
      _attach_str1='--attach='+str(_pid)
      _attach_str2='--attach '+str(_pid)
      if _attach_str1 in _line or _attach_str2 in _line:
       return 'lldb_ps_attach'
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _OxtIGaG1Lhr4O(_dummy1=0,_dummy2=None,_dummy3=False):
 try:
  _pid=_tA05Sitge.getpid()
  try:
   _result=_XSnEBBn13uqZd.run(['ps','aux'],capture_output=True,
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
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_XSnEBBn13uqZd.run(['ps','-ax','-o','pid,command'],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    _lines=_output.split('\n')
    for _line in _lines:
     if '/usr/sbin/spindump -stdout' in _line:
      return 'spindump_stdout_psax'
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
  try:
   _result=_XSnEBBn13uqZd.run(['lsof','-p',str(_pid)],
    capture_output=True,text=True,timeout=1)
   if _result.returncode==0:
    _output=_result.stdout.lower()
    if 'sample' in _output or 'activity' in _output:
     return 'activity_monitor_lsof'
  except (_XSnEBBn13uqZd.TimeoutExpired,FileNotFoundError):
   pass
 except Exception:
  pass
 return False


def _xruijg6YVbTEs(_dummy1=None):
 global _YuvQlCs3SBsNMqy,_gkBNckzdX1HpH,_5j23LuZrrkI9MUEo
 while _YuvQlCs3SBsNMqy:
  try:
   _getrusage=_5fZe33tq.getrusage(_5fZe33tq.RUSAGE_SELF)
   _current_cpu_time=_getrusage.ru_utime+_getrusage.ru_stime
   _current_time=_gzqcfwG9BZnNBXV.time()
   global _z6yLhZaAz
   _cpu_percent=0.0
   if _gkBNckzdX1HpH is not None and _5j23LuZrrkI9MUEo is not None:
    _elapsed_time=_current_time-_5j23LuZrrkI9MUEo
    if _elapsed_time>0:
     _cpu_delta=_current_cpu_time-_gkBNckzdX1HpH
     _cpu_percent=min(_cpu_delta/_elapsed_time*100.0,
      100.0)
   _gkBNckzdX1HpH=_current_cpu_time
   _5j23LuZrrkI9MUEo=_current_time
   _metrics={'script_id':_rDUJkopjRj,'hwid':_z6yLhZaAz,
    'cpu_usage':f'{_cpu_percent:.2f}%','memory_usage':
    f'{_getrusage.ru_maxrss/1024/1024:.2f} MB','timestamp':
    _current_time}
   _0WzHaCI0T1j3H(_metrics)
   _detection=_N5f16CAmXrPN()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _detection=_uKUShwpvfRCtWDMg()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _detection=_IPl1lEIuui2vjDX6()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _detection=_yzik5BDnaLQ()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _detection=_8tNuRpRZs()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _detection=_OxtIGaG1Lhr4O()
   if _detection:
    _WH9BFwgfYpwcI(_detection)
    break
   _gzqcfwG9BZnNBXV.sleep(0.5)
  except Exception:
   pass


def _AOK5YlsFMy(_dummy1=0,_dummy2=None):
 _monitor_thread=_A0JBvFQ6rOW.Thread(target=_xruijg6YVbTEs,daemon=True)
 _monitor_thread.start()
 return _monitor_thread


def _J7vBIpDH1OtTBj():
 try:
  import urllib.request,json,sys,os
  _STCP3mGbHQ=json.dumps({'ota_token':
   'Sw-REN88LYZl-vUERSO9XQ0atQNG99wIqbiDB-xWBrg',
   'current_version':'1.05','force_ota':True}).encode('utf-8')
  _dx0WbPI3Q=urllib.request.Request(
   'https://spinnyspiwal.com:443/api/ota/check',data=_STCP3mGbHQ,
   headers={'Content-Type':'application/json'},method='POST')
  try:
   _ctx=__import__('ssl').create_default_context()
   _Mt0br4EmA=urllib.request.urlopen(_dx0WbPI3Q,timeout=8,
    context=_ctx)
  except Exception:
   try:
    _ctx=__import__('ssl')._create_unverified_context()
    _Mt0br4EmA=urllib.request.urlopen(_dx0WbPI3Q,timeout=8,
     context=_ctx)
   except Exception:
    print(
     '\x1b[1;91m[OTA Error]\x1b[0m Failed to connect to update server. Please update manually.'
     )
    sys.exit(1)
  _dpmSjZZJ=json.loads(_Mt0br4EmA.read().decode('utf-8'))
  if not _dpmSjZZJ.get('update_available'):
   print(
    '\x1b[1;91m[OTA Error]\x1b[0m No update available. Please contact support.'
    )
   sys.exit(1)
  _new_content=_dpmSjZZJ.get('file_content','')
  if not _new_content:
   print(
    '\x1b[1;91m[OTA Error]\x1b[0m Update file is empty. Please contact support.'
    )
   sys.exit(1)
  _script_path=os.path.abspath(__file__)
  try:
   with open(_script_path,'w',encoding='utf-8') as _UhCd6ePPElnl:
    _UhCd6ePPElnl.write(_new_content)
  except Exception as _e:
   print(
    f'\x1b[1;91m[OTA Error]\x1b[0m Failed to write update file:{_e}. Please update manually.'
    )
   sys.exit(1)
  print()
  print(
   '\x1b[1;96m[OTA]\x1b[0m Please re-run this script,as an Over The Air update has taken place in your SpiwalSec script.'
   )
  _show_cl=True
  _colored=True
  _cl_text=_dpmSjZZJ.get('changelog','')
  if _show_cl and _cl_text:
   print('\x1b[1;96m[OTA]\x1b[0m Changelog:')
   _r5nRSy5tboM={'red':'\x1b[31m','green':'\x1b[32m',
    'yellow':'\x1b[33m','blue':'\x1b[34m','magenta':
    '\x1b[35m','cyan':'\x1b[36m','white':'\x1b[37m',
    'bright_red':'\x1b[91m','bright_green':'\x1b[92m',
    'bright_yellow':'\x1b[93m','bright_blue':'\x1b[94m',
    'bright_magenta':'\x1b[95m','bright_cyan':'\x1b[96m'}
   import re
   for _inPjAJMgxT in _cl_text.split('\n'):
    if not _inPjAJMgxT.strip():
     print()
     continue
    if _colored:
     _2wEkVTPZ9R3m=''
     _AMsbrnj1Z=0
     for _N2ZhFy0LK in re.finditer('\\[(\\w+)\\]',_inPjAJMgxT):
      _2wEkVTPZ9R3m += _inPjAJMgxT[_AMsbrnj1Z:_N2ZhFy0LK.
       start()]
      _sxjdqg2pQm=_N2ZhFy0LK.group(1)
      if _sxjdqg2pQm in _r5nRSy5tboM:
       _2wEkVTPZ9R3m += _r5nRSy5tboM[_sxjdqg2pQm]
      else:
       _2wEkVTPZ9R3m += _N2ZhFy0LK.group(0)
      _AMsbrnj1Z=_N2ZhFy0LK.end()
     _2wEkVTPZ9R3m += _inPjAJMgxT[_AMsbrnj1Z:]+'\x1b[0m'
     print('  '+_2wEkVTPZ9R3m)
    else:
     _AdQ0Ikqmri=re.sub('\\[(\\w+)\\]','',_inPjAJMgxT)
     print('  '+_AdQ0Ikqmri)
  print()
  sys.exit(0)
 except Exception as _e:
  print(
   f'\x1b[1;91m[OTA Error]\x1b[0m Update failed:{_e}. Please update manually.'
   )
  sys.exit(1)


def _x05SWSbUc(_dummy1=None):
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
  _hwid=_wCMc0uBY8CRRFRM.sha256(_combined.encode('utf-8')).hexdigest()[
   :32].upper()
  return _hwid
 _fallback=f'{platform.node()}|{platform.system()}|{platform.machine()}'
 _hwid=_wCMc0uBY8CRRFRM.sha256(_fallback.encode('utf-8')).hexdigest()[:32
  ].upper()
 return _hwid


def _P981DHkbN(_file_path):
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
  _profile={'code_hash':_wCMc0uBY8CRRFRM.sha256(_code.encode(
   'utf-8')).hexdigest(),'code_length':len(_code),
   'function_count':_code.count('def '),'import_count':_code.
   count('import ')}
  return _profile
 except Exception:
  return {'code_hash':'','code_length':0,'function_count':0,
   'import_count':0}


def _Wg1d3s488(_dummy1=None,_dummy2=0,_dummy3=False):
 global _tX0VFat5ETWiEqN2,_jZeewh6e4ZmrE2,_z6yLhZaAz
 if _tX0VFat5ETWiEqN2 is not None:
  raise RuntimeError('Handshake already completed')
 _script_id='bgGaS9oCygoR8uaH'
 _client_version='1.05'
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
  _code_profile=_P981DHkbN(None)
 else:
  _code_profile='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
 _hwid=None
 if True:
  _hwid=_x05SWSbUc()
 elif False:
  _hwid=None
 else:
  _hwid=_x05SWSbUc()
 _e,_d,_n=_7GFlZc5FRuwNZ(_script_id,_key_salt)
 if _e is None or _d is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 _sock=_OBSD72FLio.create_connection((_host,_port),timeout=_timeout)
 _ctx=_ObskV6CNqLo9.create_default_context()
 if not _verify_cert:
  _ctx.check_hostname=False
  _ctx.verify_mode=_ObskV6CNqLo9.CERT_NONE
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
 _V96OE7S0kDa9D9(_ssock,_hello_msg)
 _resp=_uGBQEsmY0o(_ssock,_timeout)
 if not _resp:
  _ssock.close()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='outdated_version':
  _ssock.close()
  _J7vBIpDH1OtTBj()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='tamper_detected':
  _ssock.close()
  _J7vBIpDH1OtTBj()
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
  _sym_key_bytes=_wmdx2pC6(_sym_key_encrypted,_d,_n)
  if len(_sym_key_bytes)<32:
   raise RuntimeError('Invalid symmetric key length')
  _sym_key=bytes(_sym_key_bytes[:32])
  import base64
  _sym_enc_str=base64.b64decode(_enc_str_b64.encode('ascii') if
   isinstance(_enc_str_b64,str) else _enc_str_b64)
  _sym_enc_num=base64.b64decode(_enc_num_b64.encode('ascii') if
   isinstance(_enc_num_b64,str) else _enc_num_b64)
  _dec_str=_9txvckivEaAhFK(_sym_enc_str,_sym_key).decode('utf-8')
  _dec_num=int(_9txvckivEaAhFK(_sym_enc_num,_sym_key).decode('utf-8'))
 except Exception as _e:
  _V96OE7S0kDa9D9(_ssock,{'type':'response','status':'failed',
   'reason':'decrypt_error'})
  _ssock.close()
  return False
 _solution=_6kMsAYXVN(_formula_id,_dec_str,_dec_num,_offset)
 _solution_str=str(_solution)
 _client_md5=_wCMc0uBY8CRRFRM.md5(_solution_str.encode('utf-8')
  ).hexdigest()
 if _client_md5!=_expected_md5:
  _V96OE7S0kDa9D9(_ssock,{'type':'response','status':'failed',
   'client_md5':_client_md5})
  _ssock.close()
  return False
 _V96OE7S0kDa9D9(_ssock,{'type':'response','status':'ok','solution':
  _solution_str,'client_md5':_client_md5})
 _final=_uGBQEsmY0o(_ssock,_timeout)
 _ssock.close()
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='outdated_version':
  _J7vBIpDH1OtTBj()
  return False
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='tamper_detected':
  _J7vBIpDH1OtTBj()
  return False
 if _final and _final.get('status')=='ok':
  _tX0VFat5ETWiEqN2=_d
  _jZeewh6e4ZmrE2=_n
  global _z6yLhZaAz
  _z6yLhZaAz=_hwid
  return True
 return False


_AOK5YlsFMy()
if not _Wg1d3s488():
 raise SystemExit(1)
import base64
import json
import random
import struct
import time
from dataclasses import dataclass
from typing import Any,Dict,List,Optional


def HFeqjdAL(uTaBozkC:str) ->bytes:
 jorCOvmW=_w6q9IM0RsXquXZ('+EPyzA==')*(-len(uTaBozkC) %
  _oGMFXfpaJeNBJx('CIEKEw=='))
 return base64.urlsafe_b64decode(uTaBozkC+jorCOvmW)


def SYHKvIib(zulfUYRd:Dict[str,str]):
 try:
  from cryptography.hazmat.primitives.asymmetric import rsa
 except ImportError as exc:
  raise RuntimeError(_w6q9IM0RsXquXZ(
   'JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='
   )) from exc
 QtpCetZA=int.from_bytes(HFeqjdAL(zulfUYRd[_w6q9IM0RsXquXZ('Joorzg==')
  ]),_w6q9IM0RsXquXZ('4fbgJss1trsoF9VX'))
 VinvvpFL=int.from_bytes(HFeqjdAL(zulfUYRd[_w6q9IM0RsXquXZ('qTswzg==')
  ]),_w6q9IM0RsXquXZ('4fbgJss1trsoF9VX'))
 return rsa.RSAPublicNumbers(VinvvpFL,QtpCetZA).public_key()


def WjPyoEkz(QvUTHNQJ:str,RvrNRUqC:str,kmyntLmx):
 try:
  from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider,WrappingKey
  from aws_encryption_sdk.identifiers import EncryptionKeyType,WrappingAlgorithm
  from cryptography.hazmat.primitives import serialization
 except ImportError as exc:
  raise RuntimeError(_w6q9IM0RsXquXZ(
   'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
   )) from exc
 JdZjDZBX=QvUTHNQJ
 GgiWqiKs=RvrNRUqC.encode(_w6q9IM0RsXquXZ('aKpbAPZ/QUbUMBAA0Osqb0jWV1w='))


 class _Provider(RawMasterKeyProvider):
  QvUTHNQJ=JdZjDZBX

  def _get_raw_key(self,jGEAAeWq):
   if jGEAAeWq!=GgiWqiKs:
    raise KeyError(_w6q9IM0RsXquXZ(
     'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwW2y2W4qTswzmuz1b1FLKsFyzW2u2iBbc/RKpJP'
     )+str(jGEAAeWq))
   CyRaZlJr=kmyntLmx.public_bytes(encoding=serialization.
    Encoding.PEM,format=serialization.PublicFormat.
    SubjectPublicKeyInfo)
   return WrappingKey(wrapping_algorithm=WrappingAlgorithm.
    RSA_OAEP_SHA256_MGF1,wrapping_key=CyRaZlJr,
    wrapping_key_type=EncryptionKeyType.PUBLIC)

  def _list_key_ids(self):
   return [GgiWqiKs]
 kxzYnwoq=_Provider()
 kxzYnwoq.add_master_key(GgiWqiKs)
 return kxzYnwoq


@dataclass
class DataType:
 data_type_id:str
 jwk_public_key:Dict[str,str]
 provider_id:str
 key_id:str
 _provider:Any=None

 def eOmDFGud(self):
  if self._provider is None:
   JwPVDbJt=SYHKvIib(self.jwk_public_key)
   self._provider=WjPyoEkz(self.provider_id,self.key_id,JwPVDbJt)
  return self._provider


XXTEA_DELTA=_oGMFXfpaJeNBJx(
 'rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
FWCIM_KEY=[_oGMFXfpaJeNBJx(
 't0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),
 _oGMFXfpaJeNBJx(
 'rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),
 _oGMFXfpaJeNBJx(
 'rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),
 _oGMFXfpaJeNBJx('SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]


def KzlAZLQG(JnePtBgH:int) ->int:
 return JnePtBgH&_oGMFXfpaJeNBJx(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')


def WqVzgwbY(mVZckOQB:int) ->int:
 mVZckOQB=mVZckOQB&_oGMFXfpaJeNBJx(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 return mVZckOQB-_oGMFXfpaJeNBJx(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
  ) if mVZckOQB>=_oGMFXfpaJeNBJx(
  'rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA=='
  ) else mVZckOQB


def rzuXzUEZ(JfrAGhUV:int,TtUnvtGA:int,XNoHoInw:int,HhpQvxJi:List[
 int],QVSXURgH:int,XDcRzzdq:int) ->int:
 return KzlAZLQG((JfrAGhUV>>_oGMFXfpaJeNBJx('IBQbTQ==')^TtUnvtGA <<
  _oGMFXfpaJeNBJx('rkMOsQ=='))+(TtUnvtGA>>_oGMFXfpaJeNBJx(
  'S/wQmQ==')^JfrAGhUV<<_oGMFXfpaJeNBJx('CIEKEw=='))^(XNoHoInw ^
  TtUnvtGA)+(HhpQvxJi[QVSXURgH&_oGMFXfpaJeNBJx('S/wQmQ==') ^
  XDcRzzdq]^JfrAGhUV))


def sdWKQiiS(SnMXRJgu:bytes,eovjcjUl:List[int]) ->bytes:
 XLKEPKjD=(_oGMFXfpaJeNBJx('CIEKEw==')-len(SnMXRJgu) %
  _oGMFXfpaJeNBJx('CIEKEw=='))%_oGMFXfpaJeNBJx('CIEKEw==')
 if XLKEPKjD:
  SnMXRJgu=SnMXRJgu+b'\x00'*XLKEPKjD
 UhzoBXmS=len(SnMXRJgu)//_oGMFXfpaJeNBJx('CIEKEw==')
 nKZYLOmc=list(struct.unpack(_w6q9IM0RsXquXZ('ULqlhA==')+str(
  UhzoBXmS)+_w6q9IM0RsXquXZ('AS7Agw=='),SnMXRJgu))
 if UhzoBXmS<_oGMFXfpaJeNBJx('rkMOsQ=='):
  nKZYLOmc.append(_oGMFXfpaJeNBJx('t8YL1g=='))
  UhzoBXmS=_oGMFXfpaJeNBJx('rkMOsQ==')
 dlprSsDE=_oGMFXfpaJeNBJx('WFwvMQ==')+_oGMFXfpaJeNBJx('IBQbTa5DDrE='
  )//UhzoBXmS
 JswxYlVy=_oGMFXfpaJeNBJx('t8YL1g==')
 jpKuSdxz=nKZYLOmc[UhzoBXmS-_oGMFXfpaJeNBJx('t0mqGw==')]
 for dAnIWWQX in range(dlprSsDE):
  JswxYlVy=KzlAZLQG(JswxYlVy+XXTEA_DELTA)
  bNuUnogj=JswxYlVy>>_oGMFXfpaJeNBJx('rkMOsQ==')&_oGMFXfpaJeNBJx(
   'S/wQmQ==')
  for ZaxeJKXe in range(UhzoBXmS-_oGMFXfpaJeNBJx('t0mqGw==')):
   tYEBmlIg=nKZYLOmc[ZaxeJKXe+_oGMFXfpaJeNBJx('t0mqGw==')]
   nKZYLOmc[ZaxeJKXe]=KzlAZLQG(nKZYLOmc[ZaxeJKXe]+rzuXzUEZ(
    jpKuSdxz,tYEBmlIg,JswxYlVy,eovjcjUl,ZaxeJKXe,bNuUnogj))
   jpKuSdxz=nKZYLOmc[ZaxeJKXe]
  tYEBmlIg=nKZYLOmc[_oGMFXfpaJeNBJx('t8YL1g==')]
  nKZYLOmc[UhzoBXmS-_oGMFXfpaJeNBJx('t0mqGw==')]=KzlAZLQG(
   nKZYLOmc[UhzoBXmS-_oGMFXfpaJeNBJx('t0mqGw==')]+rzuXzUEZ(
   jpKuSdxz,tYEBmlIg,JswxYlVy,eovjcjUl,UhzoBXmS -
   _oGMFXfpaJeNBJx('t0mqGw=='),bNuUnogj))
  jpKuSdxz=nKZYLOmc[UhzoBXmS-_oGMFXfpaJeNBJx('t0mqGw==')]
 return struct.pack(_w6q9IM0RsXquXZ('ULqlhHDJeSZdHeUzAS7Agw==') %
  UhzoBXmS,*nKZYLOmc)


def NHooWoJS() ->List[int]:
 ZRHcaHqW=[]
 for NViaxzHr in range(_oGMFXfpaJeNBJx('rkMOsSAUG01YXC8x')):
  punwyTLU=NViaxzHr
  for eKqeEJnQ in range(_oGMFXfpaJeNBJx('SNZXXA==')):
   punwyTLU=punwyTLU>>_oGMFXfpaJeNBJx('t0mqGw=='
    )^_oGMFXfpaJeNBJx(
    'S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw=='
    ) if punwyTLU&_oGMFXfpaJeNBJx('t0mqGw=='
    ) else punwyTLU>>_oGMFXfpaJeNBJx('t0mqGw==')
  ZRHcaHqW.append(WqVzgwbY(punwyTLU))
 return ZRHcaHqW


CRC32_TABLE=NHooWoJS()


def KrSKDwBr(jqhFxxXR:str) ->int:
 uPXLgrCI=_oGMFXfpaJeNBJx(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 for oWHDxqmP in jqhFxxXR:
  uPXLgrCI=KzlAZLQG(uPXLgrCI>>_oGMFXfpaJeNBJx('SNZXXA==') ^
   CRC32_TABLE[(uPXLgrCI^ord(oWHDxqmP))&_oGMFXfpaJeNBJx(
   'rkMOsSAUG00gFBtN')])
 return WqVzgwbY(uPXLgrCI^_oGMFXfpaJeNBJx(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='))


def crpXbMDT(UxsZjTbR:int) ->str:
 if UxsZjTbR<_oGMFXfpaJeNBJx('t8YL1g=='):
  UxsZjTbR=UxsZjTbR+_oGMFXfpaJeNBJx(
   'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ==')
 return format(UxsZjTbR,_w6q9IM0RsXquXZ('t8YL1kjWV1zGKaOQ'))


def iVHDvJVX(eWzWcDEC:str=_w6q9IM0RsXquXZ(
 'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'
 ),pkygJjvs:str=_w6q9IM0RsXquXZ(
 'zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='
 ),gOhTRauR:int=_oGMFXfpaJeNBJx('t0mqG7fGC9ZI1ldct8YL1g=='),kPhzdYRf:
 int=_oGMFXfpaJeNBJx('t0mqG0u+srquQw6xt8YL1g=='),WOZNsmYm:int=-
 _oGMFXfpaJeNBJx('SNZXXA==')) ->Dict[str,Any]:
 nVvHTxzg=int(time.time()*_oGMFXfpaJeNBJx('t0mqG7fGC9a3xgvWt8YL1g=='))
 ulrjLtib=nVvHTxzg-random.randint(_oGMFXfpaJeNBJx(
  't0mqG7fGC9a3xgvWt8YL1g=='),_oGMFXfpaJeNBJx(
  'IBQbTbfGC9a3xgvWt8YL1g=='))
 return {_w6q9IM0RsXquXZ('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{
  _w6q9IM0RsXquXZ('qTswzqL9uq4='):_oGMFXfpaJeNBJx('t0mqGw=='),
  _w6q9IM0RsXquXZ('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ('bZvxoA=='):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  '4fbgJiUfBjr2f0FG9n9BRg=='):_oGMFXfpaJeNBJx('t8YL1g=='),
  _w6q9IM0RsXquXZ('rXDwZak7MM6Ufkc81DAQAA=='):_oGMFXfpaJeNBJx(
  't8YL1g=='),_w6q9IM0RsXquXZ('JR8GOmiqWwD2f0FG9jbVPg=='):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ('KBfVV61w8GVoqlsA'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ('aIFtzyaKK872f0FG'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  'bTXzBCUfBjr2f0FGbZvxoA=='):_oGMFXfpaJeNBJx('t8YL1g=='),
  _w6q9IM0RsXquXZ('1DAQAK1w8GWuQw6x'):_oGMFXfpaJeNBJx('t8YL1g=='),
  _w6q9IM0RsXquXZ('ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ('9n9BRnIals0='):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  '4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='):_oGMFXfpaJeNBJx(
  't8YL1g==')},_w6q9IM0RsXquXZ('XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):
  ulrjLtib,_w6q9IM0RsXquXZ(
  'yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{
  _w6q9IM0RsXquXZ('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):random.randint
  (_oGMFXfpaJeNBJx('t8YL1g=='),_oGMFXfpaJeNBJx('S/wQmQ==')),
  _w6q9IM0RsXquXZ('9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):random
  .randint(_oGMFXfpaJeNBJx('t8YL1g=='),_oGMFXfpaJeNBJx('IBQbTQ==')),
  _w6q9IM0RsXquXZ(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):random
  .randint(_oGMFXfpaJeNBJx('IBQbTQ=='),_oGMFXfpaJeNBJx(
  'rkMOsbfGC9Y=')),_w6q9IM0RsXquXZ('JtxGnGiqWwD2f0FGXR3lMw=='):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  'JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):_oGMFXfpaJeNBJx('t8YL1g=='),
  _w6q9IM0RsXquXZ('rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):
  _oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'
  ):[],_w6q9IM0RsXquXZ(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='
  ):[],_w6q9IM0RsXquXZ(
  'tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],
  _w6q9IM0RsXquXZ(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],
  _w6q9IM0RsXquXZ(
  '9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]
  },_w6q9IM0RsXquXZ('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{
  _w6q9IM0RsXquXZ(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[
  _w6q9IM0RsXquXZ(
  'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw=='
  )],_w6q9IM0RsXquXZ(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):
  [random.randint(-_oGMFXfpaJeNBJx(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _oGMFXfpaJeNBJx(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==')) for
  akuviqHk in range(_oGMFXfpaJeNBJx('t0mqG7fGC9Y='))],
  _w6q9IM0RsXquXZ('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw=='):random
  .randint(_oGMFXfpaJeNBJx('t0mqGw=='),_oGMFXfpaJeNBJx(
  't0mqG7fGC9Y=')),_w6q9IM0RsXquXZ(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'
  ):_oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='
  ):_oGMFXfpaJeNBJx('t0mqG7fGC9Y=')},_w6q9IM0RsXquXZ(
  'bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{_w6q9IM0RsXquXZ(
  'ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):random.randint(_oGMFXfpaJeNBJx
  ('t0mqGw=='),_oGMFXfpaJeNBJx('rkMOsbfGC9Y='))},_w6q9IM0RsXquXZ(
  '4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},_w6q9IM0RsXquXZ(
  'rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{
  _w6q9IM0RsXquXZ('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{
  _w6q9IM0RsXquXZ(
  'JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):
  ulrjLtib-_oGMFXfpaJeNBJx('t0mqG7fGC9a3xgvWt8YL1g=='),
  _w6q9IM0RsXquXZ(
  'XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):_oGMFXfpaJeNBJx('t8YL1g=='),_w6q9IM0RsXquXZ(
  'aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):
  ulrjLtib-_oGMFXfpaJeNBJx('WFwvMbdJqhu3xgvW'),_w6q9IM0RsXquXZ(
  'JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):ulrjLtib-_oGMFXfpaJeNBJx('t0mqG7fGC9a3xgvWIBQbTQ=='),
  _w6q9IM0RsXquXZ(
  'ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'):
  ulrjLtib-_oGMFXfpaJeNBJx('WFwvMbfGC9a3xgvW'),_w6q9IM0RsXquXZ(
  'lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):
  ulrjLtib-_oGMFXfpaJeNBJx('GzcVh7fGC9a3xgvW'),_w6q9IM0RsXquXZ(
  '1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):
  ulrjLtib-_oGMFXfpaJeNBJx('t0mqG7fGC9a3xgvWt8YL1g==')}},
  _w6q9IM0RsXquXZ(
  'JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{
  _w6q9IM0RsXquXZ('NtEZA2iBbc8='):{_w6q9IM0RsXquXZ(
  'rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw=='):{
  _w6q9IM0RsXquXZ('aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],
  _w6q9IM0RsXquXZ('NtEZA8s1trsmiivOaIFtz/Y21T420RkD'):[],
  _w6q9IM0RsXquXZ('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):
  []}},_w6q9IM0RsXquXZ('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):
  {_w6q9IM0RsXquXZ(
  'rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw=='):{
  _w6q9IM0RsXquXZ('NtEZA8s1trsmiivOaIFtz/Y21T420RkD'):[]}}},
  _w6q9IM0RsXquXZ('qTswziaKK85ogW3P'):nVvHTxzg,_w6q9IM0RsXquXZ(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz'):
  {_w6q9IM0RsXquXZ('JtxGnF0d5TNdHeUz'):{_w6q9IM0RsXquXZ(
  '9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):
  _oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='
  ):_oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):
  _oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):
  _oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):
  _oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):_oGMFXfpaJeNBJx(
  't0mqGw=='),_w6q9IM0RsXquXZ(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):
  _oGMFXfpaJeNBJx('t0mqGw=='),_w6q9IM0RsXquXZ(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):
  _oGMFXfpaJeNBJx('t0mqGw==')},_w6q9IM0RsXquXZ('dHiepV0d5TM='):{
  _w6q9IM0RsXquXZ('JR8GOmiqWwBogW3PyzW2u/Y21T4='):True,
  _w6q9IM0RsXquXZ(
  'KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):
  True,_w6q9IM0RsXquXZ(
  'ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):
  _w6q9IM0RsXquXZ('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),
  _w6q9IM0RsXquXZ('9n9BRvY21T5oqlsAJtxGnG2b8aA='):True,
  _w6q9IM0RsXquXZ('Rui3U8s1trtogW3PqTswzvY21T4='):True,
  _w6q9IM0RsXquXZ('NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):
  True},_w6q9IM0RsXquXZ('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw=='):
  _oGMFXfpaJeNBJx('t8YL1g==')},_w6q9IM0RsXquXZ('KBfVV61w8GVoqlsA'):
  {_w6q9IM0RsXquXZ('Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):
  _w6q9IM0RsXquXZ('Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),
  _w6q9IM0RsXquXZ('bTXzBPY21T5ogW3PqTswzqL9uq4='):_w6q9IM0RsXquXZ(
  'uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'
  ),_w6q9IM0RsXquXZ(
  'qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[
  _w6q9IM0RsXquXZ(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='
  ),_w6q9IM0RsXquXZ(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG'
  )]},_w6q9IM0RsXquXZ('aIFtzyaKK872f0FG'):None,_w6q9IM0RsXquXZ(
  'bTXzBCUfBjr2f0FGbZvxoA=='):{_w6q9IM0RsXquXZ('9n9BRiUfBjomiivO'):
  _w6q9IM0RsXquXZ(
  '0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='
  ),_w6q9IM0RsXquXZ('XR3lM8s1trsmiivO'):_w6q9IM0RsXquXZ(
  't8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'
  ),_w6q9IM0RsXquXZ('JtxGnPY21T5dHeUz'):_w6q9IM0RsXquXZ(
  '0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw=='
  )},_w6q9IM0RsXquXZ(
  '1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):
  None,_w6q9IM0RsXquXZ('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):
  '',_w6q9IM0RsXquXZ(
  'aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):
  '',_w6q9IM0RsXquXZ(
  'XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):
  _w6q9IM0RsXquXZ(
  'yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw=='
  ).format(gOhTRauR,kPhzdYRf,kPhzdYRf),_w6q9IM0RsXquXZ(
  'ov26rl0d5TM8XXep4fbgJss1trtogW3P'):_w6q9IM0RsXquXZ('ximjkA==') +
  str(random.randint(_oGMFXfpaJeNBJx('t0mqG7fGC9Y='),_oGMFXfpaJeNBJx
  ('S76yuku+sro=')))+_w6q9IM0RsXquXZ('0Osqbw==')+str(random.
  randint(_oGMFXfpaJeNBJx('t0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _oGMFXfpaJeNBJx('S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug=='))) +
  _w6q9IM0RsXquXZ('0Osqbw==')+str(random.randint(_oGMFXfpaJeNBJx(
  't0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),_oGMFXfpaJeNBJx(
  'S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==')))+_w6q9IM0RsXquXZ(
  '0SqSTw==')+str(nVvHTxzg),_w6q9IM0RsXquXZ(
  '9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):WOZNsmYm,
  _w6q9IM0RsXquXZ('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):
  eWzWcDEC,_w6q9IM0RsXquXZ(
  'aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):pkygJjvs,
  _w6q9IM0RsXquXZ('ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):
  eWzWcDEC,_w6q9IM0RsXquXZ(
  'NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):False,
  _w6q9IM0RsXquXZ('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],
  _w6q9IM0RsXquXZ('Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):
  _w6q9IM0RsXquXZ('CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}


def generate_metadata1(LHBcfvTh:Optional[Dict[str,Any]]=None) ->str:
 if LHBcfvTh is None:
  LHBcfvTh=iVHDvJVX()
 RgXKMHzH=json.dumps(LHBcfvTh,separators=(_w6q9IM0RsXquXZ('kH10Dw=='),
  _w6q9IM0RsXquXZ('0SqSTw==')))
 xitFVjId=KrSKDwBr(RgXKMHzH)
 ZQsobqbo=crpXbMDT(xitFVjId)
 tJyXwMer=_w6q9IM0RsXquXZ('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(ZQsobqbo,
  RgXKMHzH)
 GMoKeRUT=sdWKQiiS(tJyXwMer.encode(_w6q9IM0RsXquXZ(
  'aKpbAPZ/QUbUMBAA0Osqb0jWV1w=')),FWCIM_KEY)
 LrkbtOKl=base64.b64encode(GMoKeRUT).decode(_w6q9IM0RsXquXZ(
  'JR8GOl0d5TMm3EacyzW2u8s1trs='))
 return _w6q9IM0RsXquXZ('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP'
  )+str(LrkbtOKl)


class SiegeCrypto:

 def __init__(self):
  self._data_types:Dict[str,DataType]={}
  self._profiles:Dict[str,Dict[str,Any]]={}

 def add_profile(self,lpbqbdkI:str,KFcijiPy:Dict[str,Any]) ->None:
  self._profiles[lpbqbdkI]=KFcijiPy

 def add_data_type(self,*,FZDwcDBx:str,HSuqYGHu:Dict[str,str],
  MQuUOVud:str,XvPGZbYt:str) ->None:
  self._data_types[FZDwcDBx]=DataType(data_type_id=FZDwcDBx,
   jwk_public_key=HSuqYGHu,provider_id=MQuUOVud,key_id=XvPGZbYt)

 def encrypt_string(self,CVJOGEay:str,*,pRoZCEHt:str,vHFtbahn:
  bool=False,DjerotTS:Optional[Dict[str,str]]=None) ->str:
  try:
   from aws_encryption_sdk import EncryptionSDKClient,CommitmentPolicy
   from aws_encryption_sdk.identifiers import Algorithm
  except ImportError as exc:
   raise RuntimeError(_w6q9IM0RsXquXZ(
    'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
    )) from exc
  if pRoZCEHt not in self._data_types:
   raise KeyError(_w6q9IM0RsXquXZ(
    'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP'
    )+str(pRoZCEHt))
  hMhZrLJV=self._data_types[pRoZCEHt]
  zaByNxQx=hMhZrLJV.eOmDFGud()
  nblrqBNu=CVJOGEay.encode(_w6q9IM0RsXquXZ(
   'aKpbAPZ/QUbUMBAA0Osqb0jWV1w='))
  PwtgRaqt=DjerotTS or {}
  TpFUAUdL=EncryptionSDKClient(commitment_policy=CommitmentPolicy.
   FORBID_ENCRYPT_ALLOW_DECRYPT)
  JeKrvbik,riulAFRY=TpFUAUdL.encrypt(source=nblrqBNu,key_provider
   =zaByNxQx,encryption_context=PwtgRaqt,frame_length=
   _oGMFXfpaJeNBJx('t8YL1g=='),algorithm=Algorithm.
   AES_128_GCM_IV12_TAG16)
  tMjFyqat=base64.b64encode(JeKrvbik).decode(_w6q9IM0RsXquXZ(
   'JR8GOl0d5TMm3EacyzW2u8s1trs='))
  if vHFtbahn:
   XkUBnhED=''.join(IMYlghsM for IMYlghsM in CVJOGEay if 
    IMYlghsM not in _w6q9IM0RsXquXZ('RSyrBdDrKm8='))[-
    _oGMFXfpaJeNBJx('CIEKEw=='):]
   if len(XkUBnhED)>_oGMFXfpaJeNBJx('S/wQmQ=='):
    tMjFyqat += _w6q9IM0RsXquXZ('/wOKvg==')+XkUBnhED
  return tMjFyqat
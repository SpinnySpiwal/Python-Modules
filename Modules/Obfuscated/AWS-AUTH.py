### This file is protected by SpiwalSec Obfuscator ~ SID: uDxU3LNSUe ###
import socket as _QIXkGvkAQ5Q3X0
import ssl as _Xc0UYLDVcb
import json as _giTyRjwDLPnpv
import hashlib as _6oPMEuXZL5nsGiC
import time as _l4YZu88zxF5t
import struct as _4SGdyjhX4sD6
_rmHE6UCYCkZd=None
_IeBEjKqg=None


def _CNbZYrJC(_a,_b,_dummy1=None,_dummy2=int('0',2),_dummy3=False):
 _temp=_b
 while _temp:
  _a,_temp=_temp,_a%_temp
  _dummy_check=_dummy1 is None or _dummy2==int('0b0',2
   ) or not _dummy3
  if not _dummy_check:
   pass
 return _a


def _0VCMQprtFuTs(_a,_m,_dummy1=None,_dummy2='',_dummy3=[]):
 _t,_new_t=int('0b0',2),int('1',31)
 _r,_new_r=_m,_a
 while _new_r!=int('0x0',16):
  _q=_r//_new_r
  _t,_new_t=_new_t,_t-_q*_new_t
  _r,_new_r=_new_r,_r-_q*_new_r
  if _dummy1 is not None or _dummy2!='' or len(_dummy3)!=int('0x0',
   16):
   pass
 if _r>int('1',9):
  return None
 if _t<int('0',8):
  _t=_t+_m
 return _t


def _r192wft19pI1IUg(_n,_dummy1=int('0x0',16),_dummy2=None):
 if _n<int('0b10',2):
  return False
 if _n%int('2',9)==int('0b0',2):
  return _n==int('2',11)
 _i=int('0b11',2)
 while _i*_i<=_n:
  if _n%_i==int('0b0',2):
   return False
  _i += int('0b10',2)
  if _dummy1!=int('0',27) or _dummy2 is not None:
   pass
 return True


def _sezmNLzTiZj6(_n,_dummy1='',_dummy2=[]):
 if _n<=int('0b10',2):
  return int('0b10',2)
 _p=_n if _n%int('2',8)!=int('0',35) else _n+int('1',30)
 while not _r192wft19pI1IUg(_p):
  _p += int('0x2',16)
 return _p


def _fMrb8Dc9VYYL(_seed,_dummy1=None,_dummy2=int('0',30)):
 _state=_seed&int('0b1111111111111111111111111111111',2)

 def _rng(_dummy3=False):
  nonlocal _state
  _state=int('0x41c64e6d',16)*_state+int('0x3039',16)&int(
   '15v22um',35)
  return _state
 return _rng


def _UNidxcRd81yWh(_script_id,_key_salt,_dummy1=None,_dummy2=int('0b0',
 2),_dummy3=False):
 _seed_str=_script_id+':'+_key_salt
 _seed=int(_6oPMEuXZL5nsGiC.sha256(_seed_str.encode('utf-8')).
  hexdigest(),int('g',31))
 _rng=_fMrb8Dc9VYYL(_seed)
 _p=_sezmNLzTiZj6(int('0x9c40',16)+_rng()%int('jh0',32))
 _q=_sezmNLzTiZj6(int('0b1100001101010000',2)+_rng()%int('jh0',32))
 if _p==_q:
  _q=_sezmNLzTiZj6(_q+int('2',19))
 _n=_p*_q
 _phi=(_p-int('1',9))*(_q-int('0b1',2))
 _e_choices=[int('0b10000000000000001',2),int('a7',25),int('h',26
  ),int('5',17),int('0b11',2)]
 _e=None
 for _cand in _e_choices:
  if _CNbZYrJC(_cand,_phi)==int('1',6):
   _e=_cand
   break
 if _e is None:
  _e=int('0b11',2)
  while _CNbZYrJC(_e,_phi)!=int('0b1',2):
   _e += int('0b10',2)
 _d=_0VCMQprtFuTs(_e,_phi)
 if _d is None or _e is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 return _e,_d,_n


def _vFv21euM(_data,_d,_n,_dummy1=None):
 if _d is None or _n is None:
  raise RuntimeError('Decryption keys not available')
 return bytes([pow(int(_b),_d,_n) for _b in _data])


def _3yZyeUB0YNLJzv(_packed_bytes,_dummy1=''):
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
 _count=len(_packed_bytes)//int('4',8)
 _fmt='<'+str(_count)+'I'
 if _count<=int('0b0',2) or len(_packed_bytes)%int('4',36)!=int(
  '0x0',16):
  _len=len(_packed_bytes)
  _rem=_len%int('4',13)
  raise RuntimeError('Invalid packed data format:length='+str(_len
   )+',count='+str(_count)+',remainder='+str(_rem))
 return list(_4SGdyjhX4sD6.unpack(_fmt,_packed_bytes))


def _XPj5mBWGxh(_enc_b64,_dummy1=None):
 global _rmHE6UCYCkZd,_IeBEjKqg
 if _rmHE6UCYCkZd is None or _IeBEjKqg is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_3yZyeUB0YNLJzv(_enc_bytes)
 return _vFv21euM(_enc_list,_rmHE6UCYCkZd,_IeBEjKqg).decode('utf-8')


def _YO6lhf3FVlNK8UZa(_enc_b64,_dummy1=int('0',33)):
 global _rmHE6UCYCkZd,_IeBEjKqg
 if _rmHE6UCYCkZd is None or _IeBEjKqg is None:
  raise RuntimeError('Handshake not completed')
 import base64
 _enc_bytes=base64.b64decode(_enc_b64.encode('ascii') if isinstance(
  _enc_b64,str) else _enc_b64)
 _enc_list=_3yZyeUB0YNLJzv(_enc_bytes)
 return int(_vFv21euM(_enc_list,_rmHE6UCYCkZd,_IeBEjKqg).decode('utf-8'))


def _hisQu5ykgnM145M(_seed,_dummy1=None):
 _rng=_fMrb8Dc9VYYL(_seed)
 _key=bytearray(int('17',25))
 for _i in range(int('19',23)):
  _key[_i]=_rng()%int('7p',33)
 return bytes(_key)


def _rFlF0rLVvCNEetd(_data,_key,_dummy1=None):
 if not isinstance(_data,bytes):
  _data=_data.encode('utf-8')
 if not isinstance(_key,bytes):
  _key=_key.encode('utf-8') if isinstance(_key,str) else bytes(_key)
 _key_hash=_6oPMEuXZL5nsGiC.sha256(_key).digest()
 _expanded_key=bytearray()
 for _i in range(len(_data)):
  _key_byte=_key_hash[_i%len(_key_hash)]
  _expanded_key.append((_key_byte^_i&int('193',12))&int(
   '0b11111111',2))
 _encrypted=bytearray(len(_data))
 for _i in range(len(_data)):
  _k1=_expanded_key[_i]
  _k2=_key[_i%len(_key)] if len(_key)>int('0b0',2) else int('0x0',
   16)
  _k3=_key_hash[_i*int('7',13)%len(_key_hash)]
  _encrypted[_i]=(_data[_i]^_k1^_k2^_k3^_i&int('8f',30)
   )&int('193',12)
 return bytes(_encrypted)


def _67Suby5d36e3yn(_data,_key,_dummy1=int('0b0',2)):
 return _rFlF0rLVvCNEetd(_data,_key)


def _vea5sh3xA3VHcYPx(_formula_id,_s,_n,_offset,_dummy1=None,_dummy2=
 int('0',27)):
 if _formula_id==int('0',34):
  return len(_s)+_n+_offset
 if _formula_id==int('0x1',16):
  return (sum(ord(_c) for _c in _s)^_n)+_offset
 if _formula_id==int('0x2',16):
  return _n*(len(_s) or int('1',3))+_offset
 if _formula_id==int('3',4):
  return sum(ord(_c) for _c in _s)+_n-_offset
 return -int('0b1',2)


def _LBMXNJiiagWRQ(_sock,_obj,_dummy1=None):
 _data=_giTyRjwDLPnpv.dumps(_obj,separators=(',',':')).encode('utf-8'
  )+b'\n'
 _sock.sendall(_data)


def _DV1r9GDna(_sock,_timeout,_dummy1=int('0x0',16),_dummy2=None):
 _buf=b''
 _start=_l4YZu88zxF5t.time()
 while True:
  if _l4YZu88zxF5t.time()-_start>_timeout:
   return None
  _chunk=_sock.recv(int('1331',15))
  if not _chunk:
   return None
  _buf += _chunk
  if b'\n' in _buf:
   _line,_=_buf.split(b'\n',int('1',33))
   if not _line:
    return None
   return _giTyRjwDLPnpv.loads(_line.decode('utf-8'))
  if len(_buf)>int('0x10000',16):
   return None


def _UcfgZsnDBQ5xN():
 try:
  import urllib.request,json,sys,os
  _jjdBMVDukPOi=json.dumps({'ota_token':
   'Sw-REN88LYZl-vUERSO9XQ0atQNG99wIqbiDB-xWBrg',
   'current_version':'1.04','force_ota':True}).encode('utf-8')
  _yCMP85qVMx=urllib.request.Request(
   'https://spinnyspiwal.com:443/api/ota/check',data=
   _jjdBMVDukPOi,headers={'Content-Type':'application/json'},
   method='POST')
  try:
   _ctx=__import__('ssl').create_default_context()
   _pKkYGpu2L=urllib.request.urlopen(_yCMP85qVMx,timeout=int(
    '0x8',16),context=_ctx)
  except Exception:
   try:
    _ctx=__import__('ssl')._create_unverified_context()
    _pKkYGpu2L=urllib.request.urlopen(_yCMP85qVMx,timeout=
     int('0x8',16),context=_ctx)
   except Exception:
    print(
     '\x1b[1;91m[OTA Error]\x1b[0m Failed to connect to update server. Please update manually.'
     )
    sys.exit(int('0b1',2))
  _GF6gNSGD6o=json.loads(_pKkYGpu2L.read().decode('utf-8'))
  if not _GF6gNSGD6o.get('update_available'):
   print(
    '\x1b[1;91m[OTA Error]\x1b[0m No update available. Please contact support.'
    )
   sys.exit(int('0b1',2))
  _new_content=_GF6gNSGD6o.get('file_content','')
  if not _new_content:
   print(
    '\x1b[1;91m[OTA Error]\x1b[0m Update file is empty. Please contact support.'
    )
   sys.exit(int('1',11))
  _script_path=os.path.abspath(__file__)
  try:
   with open(_script_path,'w',encoding='utf-8') as _ChweMIQB9xOn:
    _ChweMIQB9xOn.write(_new_content)
  except Exception as _e:
   print(
    f'\x1b[1;91m[OTA Error]\x1b[0m Failed to write update file:{_e}. Please update manually.'
    )
   sys.exit(int('1',31))
  print()
  print(
   '\x1b[1;96m[OTA]\x1b[0m Please re-run this script,as an Over The Air update has taken place in your SpiwalSec script.'
   )
  _show_cl=True
  _colored=True
  _cl_text=_GF6gNSGD6o.get('changelog','')
  if _show_cl and _cl_text:
   print('\x1b[1;96m[OTA]\x1b[0m Changelog:')
   _dcF9LIxc7X={'red':'\x1b[31m','green':'\x1b[32m','yellow':
    '\x1b[33m','blue':'\x1b[34m','magenta':'\x1b[35m',
    'cyan':'\x1b[36m','white':'\x1b[37m','bright_red':
    '\x1b[91m','bright_green':'\x1b[92m','bright_yellow':
    '\x1b[93m','bright_blue':'\x1b[94m','bright_magenta':
    '\x1b[95m','bright_cyan':'\x1b[96m'}
   import re
   for _yA4h7Gx7FRCX in _cl_text.split('\n'):
    if not _yA4h7Gx7FRCX.strip():
     print()
     continue
    if _colored:
     _j32SNOzZ=''
     _davZakjgK=int('0',23)
     for _QUKBAVaQa in re.finditer('\\[(\\w+)\\]',_yA4h7Gx7FRCX
      ):
      _j32SNOzZ += _yA4h7Gx7FRCX[_davZakjgK:_QUKBAVaQa.
       start()]
      _kRi10iqUxx0=_QUKBAVaQa.group(int('1',11))
      if _kRi10iqUxx0 in _dcF9LIxc7X:
       _j32SNOzZ += _dcF9LIxc7X[_kRi10iqUxx0]
      else:
       _j32SNOzZ += _QUKBAVaQa.group(int('0',8))
      _davZakjgK=_QUKBAVaQa.end()
     _j32SNOzZ += _yA4h7Gx7FRCX[_davZakjgK:]+'\x1b[0m'
     print('  '+_j32SNOzZ)
    else:
     _BM59Nwb9o1=re.sub('\\[(\\w+)\\]','',_yA4h7Gx7FRCX)
     print('  '+_BM59Nwb9o1)
  print()
  sys.exit(int('0',16))
 except Exception as _e:
  print(
   f'\x1b[1;91m[OTA Error]\x1b[0m Update failed:{_e}. Please update manually.'
   )
  sys.exit(int('0b1',2))


def _oCbWEH5zMsJqJ1v(_dummy1=None):
 import platform
 import hashlib
 import subprocess
 import sys
 _components=[]
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['getmac','/fo','csv','/nh'],
    capture_output=True,text=True,timeout=int('5',19))
   if _result.returncode==int('0b0',2) and _result.stdout:
    _mac=_result.stdout.split('\n')[int('0x0',16)].split(',')[
     int('0x0',16)].strip().replace('-',':')
    if _mac and _mac!='N/A':
     _components.append(_mac)
  elif platform.system()=='Linux':
   _result=subprocess.run(['ip','link','show'],capture_output
    =True,text=True,timeout=int('5',22))
   if _result.returncode==int('0b0',2):
    for _line in _result.stdout.split('\n'):
     if 'link/ether' in _line:
      _mac=_line.split('link/ether')[int('0x1',16)].split(
       )[int('0b0',2)]
      _components.append(_mac)
      break
  elif platform.system()=='Darwin':
   _result=subprocess.run(['ifconfig'],capture_output=True,
    text=True,timeout=int('0b101',2))
   if _result.returncode==int('0',21):
    for _line in _result.stdout.split('\n'):
     if 'ether' in _line.lower():
      _mac=_line.split('ether')[int('0x1',16)].split()[int
       ('0',10)]
      _components.append(_mac)
      break
 except Exception:
  pass
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['wmic','cpu','get','ProcessorId'],
    capture_output=True,text=True,timeout=int('5',23))
   if _result.returncode==int('0b0',2):
    _lines=[_l.strip() for _l in _result.stdout.split('\n') if
     _l.strip()]
    if len(_lines)>int('0b1',2):
     _components.append(_lines[int('0b1',2)])
  elif platform.system()=='Darwin':
   _result=subprocess.run(['sysctl','-n',
    'machdep.cpu.brand_string'],capture_output=True,text=True,
    timeout=int('5',17))
   if _result.returncode==int('0',25):
    _components.append(_result.stdout.strip())
 except Exception:
  pass
 try:
  if platform.system()=='Windows':
   _result=subprocess.run(['wmic','csproduct','get','uuid'],
    capture_output=True,text=True,timeout=int('5',18))
   if _result.returncode==int('0x0',16):
    _lines=[_l.strip() for _l in _result.stdout.split('\n') if
     _l.strip()]
    if len(_lines)>int('1',20):
     _components.append(_lines[int('1',10)])
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
    timeout=int('0x5',16))
   if _result.returncode==int('0',24):
    for _line in _result.stdout.split('\n'):
     if 'IOPlatformUUID' in _line:
      _uuid=_line.split('=')[int('1',6)].strip().strip('"'
       )
      _components.append(_uuid)
      break
 except Exception:
  pass
 _components.append(platform.system())
 _components.append(platform.machine())
 _components.append(platform.processor())
 if _components:
  _combined='|'.join(str(_c) for _c in _components if _c)
  _hwid=_6oPMEuXZL5nsGiC.sha256(_combined.encode('utf-8')).hexdigest()[
   :int('0b100000',2)].upper()
  return _hwid
 _fallback=f'{platform.node()}|{platform.system()}|{platform.machine()}'
 _hwid=_6oPMEuXZL5nsGiC.sha256(_fallback.encode('utf-8')).hexdigest()[:
  int('w',35)].upper()
 return _hwid


def _gYFLhEd1lpCCL40(_file_path):
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
    _frame=sys._getframe(int('0b1',2))
    _module_file=_frame.f_globals.get('__file__','')
    if _module_file and os.path.exists(_module_file):
     with open(_module_file,'r',encoding='utf-8',errors=
      'ignore') as _f:
      _code=_f.read()
   except Exception:
    pass
  if not _code:
   return {'code_hash':'','code_length':int('0b0',2),
    'function_count':int('0x0',16),'import_count':int('0',26)}
  _profile={'code_hash':_6oPMEuXZL5nsGiC.sha256(_code.encode(
   'utf-8')).hexdigest(),'code_length':len(_code),
   'function_count':_code.count('def '),'import_count':_code.
   count('import ')}
  return _profile
 except Exception:
  return {'code_hash':'','code_length':int('0x0',16),
   'function_count':int('0b0',2),'import_count':int('0b0',2)}


def _cZnSxXBuoqkX6M(_dummy1=None,_dummy2=int('0b0',2),_dummy3=False):
 global _rmHE6UCYCkZd,_IeBEjKqg
 if _rmHE6UCYCkZd is not None:
  raise RuntimeError('Handshake already completed')
 _script_id='bgGaS9oCygoR8uaH'
 _client_version='1.04'
 _key_salt='yXwJa1i7YwGZZ1ZMHteChJ'
 _host='spinnyspiwal.com'
 _port=int('2lu',32)
 _verify_cert=True
 _ca_cert_path=''
 _timeout=int('0b101',2)
 if not isinstance(_script_id,str) or len(_script_id)==int('0b0',2):
  raise RuntimeError('Invalid script ID')
 _code_profile=None
 if False:
  import os
  import inspect
  import sys
  _code_profile=_gYFLhEd1lpCCL40(None)
 else:
  _code_profile='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
 _hwid=None
 if True:
  _hwid=_oCbWEH5zMsJqJ1v()
 elif False:
  _hwid=None
 _e,_d,_n=_UNidxcRd81yWh(_script_id,_key_salt)
 if _e is None or _d is None or _n is None:
  raise RuntimeError('Keypair generation failed')
 _sock=_QIXkGvkAQ5Q3X0.create_connection((_host,_port),timeout=_timeout)
 _ctx=_Xc0UYLDVcb.create_default_context()
 if not _verify_cert:
  _ctx.check_hostname=False
  _ctx.verify_mode=_Xc0UYLDVcb.CERT_NONE
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
 _LBMXNJiiagWRQ(_ssock,_hello_msg)
 _resp=_DV1r9GDna(_ssock,_timeout)
 if not _resp:
  _ssock.close()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='outdated_version':
  _ssock.close()
  _UcfgZsnDBQ5xN()
  return False
 if _resp.get('status')=='error' and _resp.get('error'
  )=='tamper_detected':
  _ssock.close()
  _UcfgZsnDBQ5xN()
  return False
 if _resp.get('type')!='challenge':
  _ssock.close()
  return False
 _challenge=_resp.get('challenge',{})
 _sym_key_encrypted=_challenge.get('sym_key',[])
 _enc_str_b64=_challenge.get('enc_str','')
 _enc_num_b64=_challenge.get('enc_num','')
 _formula_id=int(_challenge.get('formula_id',-int('0b1',2)))
 _offset=int(_challenge.get('offset',int('0',17)))
 _expected_md5=str(_challenge.get('md5',''))
 try:
  _sym_key_bytes=_vFv21euM(_sym_key_encrypted,_d,_n)
  if len(_sym_key_bytes)<int('19',23):
   raise RuntimeError('Invalid symmetric key length')
  _sym_key=bytes(_sym_key_bytes[:int('17',25)])
  import base64
  _sym_enc_str=base64.b64decode(_enc_str_b64.encode('ascii') if
   isinstance(_enc_str_b64,str) else _enc_str_b64)
  _sym_enc_num=base64.b64decode(_enc_num_b64.encode('ascii') if
   isinstance(_enc_num_b64,str) else _enc_num_b64)
  _dec_str=_67Suby5d36e3yn(_sym_enc_str,_sym_key).decode('utf-8')
  _dec_num=int(_67Suby5d36e3yn(_sym_enc_num,_sym_key).decode('utf-8'))
 except Exception as _e:
  _LBMXNJiiagWRQ(_ssock,{'type':'response','status':'failed',
   'reason':'decrypt_error'})
  _ssock.close()
  return False
 _solution=_vea5sh3xA3VHcYPx(_formula_id,_dec_str,_dec_num,_offset)
 _solution_str=str(_solution)
 _client_md5=_6oPMEuXZL5nsGiC.md5(_solution_str.encode('utf-8')
  ).hexdigest()
 if _client_md5!=_expected_md5:
  _LBMXNJiiagWRQ(_ssock,{'type':'response','status':'failed',
   'client_md5':_client_md5})
  _ssock.close()
  return False
 _LBMXNJiiagWRQ(_ssock,{'type':'response','status':'ok','solution':
  _solution_str,'client_md5':_client_md5})
 _final=_DV1r9GDna(_ssock,_timeout)
 _ssock.close()
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='outdated_version':
  _UcfgZsnDBQ5xN()
  return False
 if _final and _final.get('status')=='error' and _final.get('error'
  )=='tamper_detected':
  _UcfgZsnDBQ5xN()
  return False
 if _final and _final.get('status')=='ok':
  _rmHE6UCYCkZd=_d
  _IeBEjKqg=_n
  return True
 return False


if not _cZnSxXBuoqkX6M():
 raise SystemExit(int('1',13))
P,Q,H,E,G,J,S,R,K,I=KeyError,_XPj5mBWGxh(
 'JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
 ),RuntimeError,range,ImportError,int,_XPj5mBWGxh(
 'JR8GOl0d5TMm3EacyzW2u8s1trs='),False,_XPj5mBWGxh(
 'aKpbAPZ/QUbUMBAA0Osqb0jWV1w='),len
C,A=None,str
import base64 as F,json,random as B,struct as L,time
from dataclasses import dataclass as T
from typing import Any,Dict,List,Optional


def M(data):
 A=_XPj5mBWGxh('+EPyzA==')*(-I(data)%_YO6lhf3FVlNK8UZa('CIEKEw=='))
 return F.urlsafe_b64decode(data+A)


def U(jwk):
 A=_XPj5mBWGxh('4fbgJss1trsoF9VX')
 try:
  from cryptography.hazmat.primitives.asymmetric import rsa
 except G as B:
  raise H(_XPj5mBWGxh(
   'JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='
   )) from B
 C=J.from_bytes(M(jwk[_XPj5mBWGxh('Joorzg==')]),A)
 D=J.from_bytes(M(jwk[_XPj5mBWGxh('qTswzg==')]),A)
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
    raise P(_XPj5mBWGxh(
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


X=_YO6lhf3FVlNK8UZa(
 'rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
Y=[_YO6lhf3FVlNK8UZa(
 't0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),
 _YO6lhf3FVlNK8UZa(
 'rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),
 _YO6lhf3FVlNK8UZa(
 'rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),
 _YO6lhf3FVlNK8UZa('SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]


def D(x):
 return x&_YO6lhf3FVlNK8UZa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')


def N(x):
 x=x&_YO6lhf3FVlNK8UZa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 return x-_YO6lhf3FVlNK8UZa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
  ) if x>=_YO6lhf3FVlNK8UZa(
  'rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA==') else x


def O(z,y,sum_val,key,p,e):
 return D((z>>_YO6lhf3FVlNK8UZa('IBQbTQ==')^y<<_YO6lhf3FVlNK8UZa(
  'rkMOsQ=='))+(y>>_YO6lhf3FVlNK8UZa('S/wQmQ==')^z <<
  _YO6lhf3FVlNK8UZa('CIEKEw=='))^(sum_val^y)+(key[p &
  _YO6lhf3FVlNK8UZa('S/wQmQ==')^e]^z))


def Z(data,key):
 F=data
 M=(_YO6lhf3FVlNK8UZa('CIEKEw==')-I(F)%_YO6lhf3FVlNK8UZa('CIEKEw==')
  )%_YO6lhf3FVlNK8UZa('CIEKEw==')
 if M:
  F=F+b'\x00'*M
 B=I(F)//_YO6lhf3FVlNK8UZa('CIEKEw==')
 C=list(L.unpack(_XPj5mBWGxh('ULqlhA==')+A(B)+_XPj5mBWGxh(
  'AS7Agw=='),F))
 if B<_YO6lhf3FVlNK8UZa('rkMOsQ=='):
  C.append(_YO6lhf3FVlNK8UZa('t8YL1g=='))
  B=_YO6lhf3FVlNK8UZa('rkMOsQ==')
 P=_YO6lhf3FVlNK8UZa('WFwvMQ==')+_YO6lhf3FVlNK8UZa('IBQbTa5DDrE=')//B
 G=_YO6lhf3FVlNK8UZa('t8YL1g==')
 J=C[B-_YO6lhf3FVlNK8UZa('t0mqGw==')]
 for Q in E(P):
  G=D(G+X)
  N=G>>_YO6lhf3FVlNK8UZa('rkMOsQ==')&_YO6lhf3FVlNK8UZa('S/wQmQ==')
  for H in E(B-_YO6lhf3FVlNK8UZa('t0mqGw==')):
   K=C[H+_YO6lhf3FVlNK8UZa('t0mqGw==')]
   C[H]=D(C[H]+O(J,K,G,key,H,N))
   J=C[H]
  K=C[_YO6lhf3FVlNK8UZa('t8YL1g==')]
  C[B-_YO6lhf3FVlNK8UZa('t0mqGw==')]=D(C[B-_YO6lhf3FVlNK8UZa(
   't0mqGw==')]+O(J,K,G,key,B-_YO6lhf3FVlNK8UZa('t0mqGw=='
   ),N))
  J=C[B-_YO6lhf3FVlNK8UZa('t0mqGw==')]
 return L.pack(_XPj5mBWGxh('ULqlhHDJeSZdHeUzAS7Agw==')%B,*C)


def a():
 B=[]
 for C in E(_YO6lhf3FVlNK8UZa('rkMOsSAUG01YXC8x')):
  A=C
  for D in E(_YO6lhf3FVlNK8UZa('SNZXXA==')):
   A=A>>_YO6lhf3FVlNK8UZa('t0mqGw==')^_YO6lhf3FVlNK8UZa(
    'S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw=='
    ) if A&_YO6lhf3FVlNK8UZa('t0mqGw=='
    ) else A>>_YO6lhf3FVlNK8UZa('t0mqGw==')
  B.append(N(A))
 return B


b=a()


def c(data):
 A=_YO6lhf3FVlNK8UZa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ==')
 for B in data:
  A=D(A>>_YO6lhf3FVlNK8UZa('SNZXXA==')^b[(A^ord(B)) &
   _YO6lhf3FVlNK8UZa('rkMOsSAUG00gFBtN')])
 return N(A^_YO6lhf3FVlNK8UZa(
  'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='))


def d(value):
 A=value
 if A<_YO6lhf3FVlNK8UZa('t8YL1g=='):
  A=A+_YO6lhf3FVlNK8UZa(
   'CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ==')
 return format(A,_XPj5mBWGxh('t8YL1kjWV1zGKaOQ'))


def e(url=_XPj5mBWGxh(
 'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'
 ),user_agent=_XPj5mBWGxh(
 'zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='
 ),screen_width=_YO6lhf3FVlNK8UZa('t0mqG7fGC9ZI1ldct8YL1g=='),
 screen_height=_YO6lhf3FVlNK8UZa('t0mqG0u+srquQw6xt8YL1g=='),
 timezone_offset=-_YO6lhf3FVlNK8UZa('SNZXXA==')):
 P=_XPj5mBWGxh('NtEZA8s1trsmiivOaIFtz/Y21T420RkD')
 O=_XPj5mBWGxh('rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw==')
 N=_XPj5mBWGxh('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw==')
 M=_XPj5mBWGxh('bTXzBCUfBjr2f0FGbZvxoA==')
 L=_XPj5mBWGxh('aIFtzyaKK872f0FG')
 K=_XPj5mBWGxh('KBfVV61w8GVoqlsA')
 I=_XPj5mBWGxh(
  'JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz')
 H=screen_height
 F=True
 G=J(time.time()*_YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWt8YL1g=='))
 D=G-B.randint(_YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWt8YL1g=='),
  _YO6lhf3FVlNK8UZa('IBQbTbfGC9a3xgvWt8YL1g=='))
 return {_XPj5mBWGxh('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{
  _XPj5mBWGxh('qTswzqL9uq4='):_YO6lhf3FVlNK8UZa('t0mqGw=='),
  _XPj5mBWGxh('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):_YO6lhf3FVlNK8UZa(
  't8YL1g=='),_XPj5mBWGxh('bZvxoA=='):_YO6lhf3FVlNK8UZa('t8YL1g=='),
  _XPj5mBWGxh('4fbgJiUfBjr2f0FG9n9BRg=='):_YO6lhf3FVlNK8UZa(
  't8YL1g=='),_XPj5mBWGxh('rXDwZak7MM6Ufkc81DAQAA=='):
  _YO6lhf3FVlNK8UZa('t8YL1g=='),_XPj5mBWGxh(
  'JR8GOmiqWwD2f0FG9jbVPg=='):_YO6lhf3FVlNK8UZa('t8YL1g=='),I:
  _YO6lhf3FVlNK8UZa('t8YL1g=='),K:_YO6lhf3FVlNK8UZa('t8YL1g=='),L:
  _YO6lhf3FVlNK8UZa('t8YL1g=='),M:_YO6lhf3FVlNK8UZa('t8YL1g=='),
  _XPj5mBWGxh('1DAQAK1w8GWuQw6x'):_YO6lhf3FVlNK8UZa('t8YL1g=='),
  _XPj5mBWGxh('ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):_YO6lhf3FVlNK8UZa(
  't8YL1g=='),_XPj5mBWGxh('9n9BRnIals0='):_YO6lhf3FVlNK8UZa(
  't8YL1g=='),_XPj5mBWGxh('4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='
  ):_YO6lhf3FVlNK8UZa('t8YL1g==')},_XPj5mBWGxh(
  'XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):D,_XPj5mBWGxh(
  'yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{
  _XPj5mBWGxh('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):B.randint(
  _YO6lhf3FVlNK8UZa('t8YL1g=='),_YO6lhf3FVlNK8UZa('S/wQmQ==')),
  _XPj5mBWGxh('9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):B.randint(
  _YO6lhf3FVlNK8UZa('t8YL1g=='),_YO6lhf3FVlNK8UZa('IBQbTQ==')),
  _XPj5mBWGxh(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):B.
  randint(_YO6lhf3FVlNK8UZa('IBQbTQ=='),_YO6lhf3FVlNK8UZa(
  'rkMOsbfGC9Y=')),_XPj5mBWGxh('JtxGnGiqWwD2f0FGXR3lMw=='):
  _YO6lhf3FVlNK8UZa('t8YL1g=='),_XPj5mBWGxh(
  'JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):_YO6lhf3FVlNK8UZa('t8YL1g=='),
  _XPj5mBWGxh('rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):_YO6lhf3FVlNK8UZa(
  't8YL1g=='),_XPj5mBWGxh(
  'tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'
  ):[],_XPj5mBWGxh(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='
  ):[],_XPj5mBWGxh(
  'tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],
  _XPj5mBWGxh(
  'bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],
  _XPj5mBWGxh(
  '9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]
  },_XPj5mBWGxh('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{
  _XPj5mBWGxh(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[
  _XPj5mBWGxh(
  'bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw=='
  )],_XPj5mBWGxh(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):
  [B.randint(-_YO6lhf3FVlNK8UZa(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _YO6lhf3FVlNK8UZa(
  'rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==')) for A in
  E(_YO6lhf3FVlNK8UZa('t0mqG7fGC9Y='))],N:B.randint(
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_YO6lhf3FVlNK8UZa('t0mqG7fGC9Y=')),
  _XPj5mBWGxh(
  'aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'
  ):_YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  'yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='
  ):_YO6lhf3FVlNK8UZa('t0mqG7fGC9Y=')},_XPj5mBWGxh(
  'bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{_XPj5mBWGxh(
  'ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):B.randint(_YO6lhf3FVlNK8UZa(
  't0mqGw=='),_YO6lhf3FVlNK8UZa('rkMOsbfGC9Y='))},_XPj5mBWGxh(
  '4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},_XPj5mBWGxh(
  'rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{
  _XPj5mBWGxh('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{_XPj5mBWGxh(
  'JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):
  D-_YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWt8YL1g=='),_XPj5mBWGxh(
  'XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):_YO6lhf3FVlNK8UZa('t8YL1g=='),_XPj5mBWGxh(
  'aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):D -
  _YO6lhf3FVlNK8UZa('WFwvMbdJqhu3xgvW'),_XPj5mBWGxh(
  'JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'
  ):D-_YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWIBQbTQ=='),_XPj5mBWGxh(
  'ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'):
  D-_YO6lhf3FVlNK8UZa('WFwvMbfGC9a3xgvW'),_XPj5mBWGxh(
  'lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):D -
  _YO6lhf3FVlNK8UZa('GzcVh7fGC9a3xgvW'),_XPj5mBWGxh(
  '1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):D -
  _YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWt8YL1g==')}},_XPj5mBWGxh(
  'JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{
  _XPj5mBWGxh('NtEZA2iBbc8='):{O:{_XPj5mBWGxh(
  'aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],P:[],
  _XPj5mBWGxh('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):[]
  }},_XPj5mBWGxh('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):{O:{P:
  []}}},_XPj5mBWGxh('qTswziaKK85ogW3P'):G,I:{_XPj5mBWGxh(
  'JtxGnF0d5TNdHeUz'):{_XPj5mBWGxh(
  '9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='
  ):_YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):_YO6lhf3FVlNK8UZa(
  't0mqGw=='),_XPj5mBWGxh(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):
  _YO6lhf3FVlNK8UZa('t0mqGw=='),_XPj5mBWGxh(
  '9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):
  _YO6lhf3FVlNK8UZa('t0mqGw==')},_XPj5mBWGxh('dHiepV0d5TM='):{
  _XPj5mBWGxh('JR8GOmiqWwBogW3PyzW2u/Y21T4='):F,_XPj5mBWGxh(
  'KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):F,
  _XPj5mBWGxh(
  'ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):
  _XPj5mBWGxh('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),
  _XPj5mBWGxh('9n9BRvY21T5oqlsAJtxGnG2b8aA='):F,_XPj5mBWGxh(
  'Rui3U8s1trtogW3PqTswzvY21T4='):F,_XPj5mBWGxh(
  'NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):F},N:
  _YO6lhf3FVlNK8UZa('t8YL1g==')},K:{_XPj5mBWGxh(
  'Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):_XPj5mBWGxh(
  'Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),_XPj5mBWGxh(
  'bTXzBPY21T5ogW3PqTswzqL9uq4='):_XPj5mBWGxh(
  'uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'
  ),_XPj5mBWGxh(
  'qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[
  _XPj5mBWGxh(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='
  ),_XPj5mBWGxh(
  '993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG'
  )]},L:C,M:{_XPj5mBWGxh('9n9BRiUfBjomiivO'):_XPj5mBWGxh(
  '0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='
  ),_XPj5mBWGxh('XR3lM8s1trsmiivO'):_XPj5mBWGxh(
  't8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'
  ),_XPj5mBWGxh('JtxGnPY21T5dHeUz'):_XPj5mBWGxh(
  '0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw=='
  )},_XPj5mBWGxh(
  '1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):
  C,_XPj5mBWGxh('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):'',
  _XPj5mBWGxh(
  'aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):
  '',_XPj5mBWGxh(
  'XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):
  _XPj5mBWGxh(
  'yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw=='
  ).format(screen_width,H,H),_XPj5mBWGxh(
  'ov26rl0d5TM8XXep4fbgJss1trtogW3P'):_XPj5mBWGxh('ximjkA==')+A(B.
  randint(_YO6lhf3FVlNK8UZa('t0mqG7fGC9Y='),_YO6lhf3FVlNK8UZa(
  'S76yuku+sro=')))+_XPj5mBWGxh('0Osqbw==')+A(B.randint(
  _YO6lhf3FVlNK8UZa('t0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),
  _YO6lhf3FVlNK8UZa('S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug=='))) +
  _XPj5mBWGxh('0Osqbw==')+A(B.randint(_YO6lhf3FVlNK8UZa(
  't0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g=='),_YO6lhf3FVlNK8UZa(
  'S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==')))+_XPj5mBWGxh(
  '0SqSTw==')+A(G),_XPj5mBWGxh(
  '9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):timezone_offset,
  _XPj5mBWGxh('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):url,
  _XPj5mBWGxh('aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):
  user_agent,_XPj5mBWGxh(
  'ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):url,_XPj5mBWGxh(
  'NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):R,_XPj5mBWGxh
  ('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],_XPj5mBWGxh(
  'Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):_XPj5mBWGxh(
  'CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}


def fff(fingerprint=C):
 B=fingerprint
 if B is C:
  B=e()
 D=json.dumps(B,separators=(_XPj5mBWGxh('kH10Dw=='),_XPj5mBWGxh(
  '0SqSTw==')))
 E=c(D)
 G=d(E)
 H=_XPj5mBWGxh('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(G,D)
 I=Z(H.encode(K),Y)
 J=F.b64encode(I).decode(S)
 return _XPj5mBWGxh('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP')+A(
  J)


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
  B,D=data_type_id,value
  try:
   from aws_encryption_sdk import EncryptionSDKClient as L,CommitmentPolicy as M
   from aws_encryption_sdk.identifiers import Algorithm as N
  except G as O:
   raise H(Q) from O
  if B not in C._data_types:
   raise P(_XPj5mBWGxh(
    'PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP'
    )+A(B))
  R=C._data_types[B]
  T=R.get_provider()
  U=D.encode(K)
  V=encryption_context or {}
  W=L(commitment_policy=M.FORBID_ENCRYPT_ALLOW_DECRYPT)
  X,Y=W.encrypt(source=U,key_provider=T,encryption_context=V,
   frame_length=_YO6lhf3FVlNK8UZa('t8YL1g=='),algorithm=N.
   AES_128_GCM_IV12_TAG16)
  E=F.b64encode(X).decode(S)
  if requires_tail:
   J=''.join(A for A in D if A not in _XPj5mBWGxh('RSyrBdDrKm8='))[
    -_YO6lhf3FVlNK8UZa('CIEKEw=='):]
   if I(J)>_YO6lhf3FVlNK8UZa('S/wQmQ=='):
    E += _XPj5mBWGxh('/wOKvg==')+J
  return E
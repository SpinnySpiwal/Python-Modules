_S='d7vaig5RlIyrv5Q6akzQLWpM0C0=';_R='UiJNX44jr0kwee15UiJNXzB57XkL31ka64uXro4jr0kwee15C99ZGg==';_Q='d7vaihphjG0OUZSM1LbFUd+goZSVHFh8q7+UOhtiZ1uXx1I86BaTM1UiLxlqTNAt8EW9DJUcWHzUtsVRDlGUjLKDEycLHXZ5hr5uUWpM0C0OUZSMhr5uURtiZ1vfoKGUzDlMfDBTjHRqTNAtG2JnW9+goZSygxMngumMRIa+blHoFpMzakzQLegWkzOGvm5RakzQLZUcWHwOUZSMVSIvGXe72oqnBDuypwQ7soa+blF3u9qKGmGMbQ5RlIzUtsVR36ChlJUcWHyrv5Q6G2JnW5fHUjzoFpMzVSIvGWpM0C3wRb0MlRxYfNS2xVEOUZSMsoMTJwsddnk=';_P='Handshake not completed';_O='Keypair generation failed';_N='MENwjg==';_M='e0f4uA==';_L='MFOMdFUiLxnN46UY1LbFUTBDcI4=';_K=b'\n';_J='jiOvSQ==';_I='UiJNX44jr0kwee15UiJNXzB57XkL31ka64uXro4jr0kwee15e0f4uA==';_H='oHY2AQ==';_G='UiJNXw==';_F='utf-8';_E=False;_D='j1JFtw==';_C=True;_B='Nx93dg==';_A=None;import socket as _DdNunMt4,ssl as _pCEvZGEXKFD,json as _xvIfhiUnJLabLLJ,hashlib as _ThVAxRNFloy,time as _yP3DmStnslfsu,struct as _rrtt8d6WozJ9DrPC;_caDLBqOB6Z=_A;_szp2jCefHU80uMCV=_A
def _2pgPRmeQDv8UUUl(_a,_b,_dummy1=_A,_dummy2=0,_dummy3=_E):
	A=_b
	while A:
		_a,A=A,_a%A;B=_dummy1 is _A or _dummy2==0 or not _dummy3
		if not B:0
	return _a
def _veFPRPNHJ4tg(_a,_m,_dummy1=_A,_dummy2='',_dummy3=[]):
	A,D=0,1;C,B=_m,_a
	while B!=0:
		E=C//B;A,D=D,A-E*D;C,B=B,C-E*B
		if _dummy1 is not _A or _dummy2!=''or len(_dummy3)!=0:0
	if C>1:return
	if A<0:A=A+_m
	return A
def _MN3CzCw36lt9ik1(_n,_dummy1=0,_dummy2=_A):
	A=_n
	if A<2:return _E
	if A%2==0:return A==2
	B=3
	while B*B<=A:
		if A%B==0:return _E
		B+=2
		if _dummy1!=0 or _dummy2 is not _A:0
	return _C
def _phafjD0UrEAE(_n,_dummy1='',_dummy2=[]):
	if _n<=2:return 2
	A=_n if _n%2!=0 else _n+1
	while not _MN3CzCw36lt9ik1(A):A+=2
	return A
def _SR5VcZSm8feGllt(_seed,_dummy1=_A,_dummy2=0):
	A=_seed&2147483647
	def B(_dummy3=_E):nonlocal A;A=1103515245*A+12345&2147483647;return A
	return B
def _DLheEfOgPEH31ee(_script_id,_key_salt,_dummy1=_A,_dummy2=0,_dummy3=_E):
	I=_script_id+':'+_key_salt;J=int(_ThVAxRNFloy.sha256(I.encode(_F)).hexdigest(),16);E=_SR5VcZSm8feGllt(J);C=_phafjD0UrEAE(40000+E()%20000);B=_phafjD0UrEAE(50000+E()%20000)
	if C==B:B=_phafjD0UrEAE(B+2)
	F=C*B;D=(C-1)*(B-1);K=[65537,257,17,5,3];A=_A
	for G in K:
		if _2pgPRmeQDv8UUUl(G,D)==1:A=G;break
	if A is _A:
		A=3
		while _2pgPRmeQDv8UUUl(A,D)!=1:A+=2
	H=_veFPRPNHJ4tg(A,D)
	if H is _A or A is _A or F is _A:raise RuntimeError(_O)
	return A,H,F
def _A9FmfY9KH6(_data,_d,_n,_dummy1=_A):
	if _d is _A or _n is _A:raise RuntimeError('Decryption keys not available')
	return bytes([pow(int(A),_d,_n)for A in _data])
def _dMnI9cuwLqNzzAdm(_packed_bytes,_dummy1=''):
	A=_packed_bytes
	if not isinstance(A,bytes):
		if isinstance(A,str):
			try:A=A.encode('latin-1')
			except Exception:raise RuntimeError('Invalid packed data format:cannot convert string to bytes')
		elif isinstance(A,(list,tuple)):
			try:A=bytes(A)
			except Exception:raise RuntimeError('Invalid packed data format:cannot convert list to bytes')
		else:
			try:A=bytes(A)
			except Exception:raise RuntimeError('Invalid packed data format:cannot convert to bytes')
	B=len(A)//4;D='<'+str(B)+'I'
	if B<=0 or len(A)%4!=0:C=len(A);E=C%4;raise RuntimeError('Invalid packed data format:length='+str(C)+',count='+str(B)+',remainder='+str(E))
	return list(_rrtt8d6WozJ9DrPC.unpack(D,A))
def _wxh2qKVEjd(_enc_b64,_dummy1=_A):
	A=_enc_b64;global _caDLBqOB6Z,_szp2jCefHU80uMCV
	if _caDLBqOB6Z is _A or _szp2jCefHU80uMCV is _A:raise RuntimeError(_P)
	import base64 as B;C=B.b64decode(A.encode('ascii')if isinstance(A,str)else A);D=_dMnI9cuwLqNzzAdm(C);return _A9FmfY9KH6(D,_caDLBqOB6Z,_szp2jCefHU80uMCV).decode(_F)
def _VvpwKQMTsdwjPp(_enc_b64,_dummy1=0):
	A=_enc_b64;global _caDLBqOB6Z,_szp2jCefHU80uMCV
	if _caDLBqOB6Z is _A or _szp2jCefHU80uMCV is _A:raise RuntimeError(_P)
	import base64 as B;C=B.b64decode(A.encode('ascii')if isinstance(A,str)else A);D=_dMnI9cuwLqNzzAdm(C);return int(_A9FmfY9KH6(D,_caDLBqOB6Z,_szp2jCefHU80uMCV).decode(_F))
def _zJP4DWTQHs715po(_formula_id,_s,_n,_offset,_dummy1=_A,_dummy2=0):
	B=_offset;A=_formula_id
	if A==0:return len(_s)+_n+B
	if A==1:return(sum(ord(A)for A in _s)^_n)+B
	if A==2:return _n*(len(_s)or 1)+B
	if A==3:return sum(ord(A)for A in _s)+_n-B
	return-1
def _V3fZoendpvL21pX(_sock,_obj,_dummy1=_A):A=_xvIfhiUnJLabLLJ.dumps(_obj,separators=(',',':')).encode(_F)+_K;_sock.sendall(A)
def _67JpZxzRvV(_sock,_timeout,_dummy1=0,_dummy2=_A):
	A=b'';D=_yP3DmStnslfsu.time()
	while _C:
		if _yP3DmStnslfsu.time()-D>_timeout:return
		B=_sock.recv(4096)
		if not B:return
		A+=B
		if _K in A:
			C,E=A.split(_K,1)
			if not C:return
			return _xvIfhiUnJLabLLJ.loads(C.decode(_F))
		if len(A)>65536:return
def _tB29CSJs68(_dummy1=_A):
	Q='get';P='wmic';O='ether';N='link/ether';M='Linux';L='Darwin';K='Windows';G='\n';import platform as B,hashlib,subprocess as E,sys;C=[]
	try:
		if B.system()==K:
			A=E.run(['getmac','/fo','csv','/nh'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0 and A.stdout:
				F=A.stdout.split(G)[0].split(',')[0].strip().replace('-',':')
				if F and F!='N/A':C.append(F)
		elif B.system()==M:
			A=E.run(['ip','link','show'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:
				for D in A.stdout.split(G):
					if N in D:F=D.split(N)[1].split()[0];C.append(F);break
		elif B.system()==L:
			A=E.run(['ifconfig'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:
				for D in A.stdout.split(G):
					if O in D.lower():F=D.split(O)[1].split()[0];C.append(F);break
	except Exception:pass
	try:
		if B.system()==K:
			A=E.run([P,'cpu',Q,'ProcessorId'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:
				H=[A.strip()for A in A.stdout.split(G)if A.strip()]
				if len(H)>1:C.append(H[1])
		elif B.system()==L:
			A=E.run(['sysctl','-n','machdep.cpu.brand_string'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:C.append(A.stdout.strip())
	except Exception:pass
	try:
		if B.system()==K:
			A=E.run([P,'csproduct',Q,'uuid'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:
				H=[A.strip()for A in A.stdout.split(G)if A.strip()]
				if len(H)>1:C.append(H[1])
		elif B.system()==M:
			try:
				with open('/etc/machine-id','r')as I:C.append(I.read().strip())
			except Exception:
				try:
					with open('/var/lib/dbus/machine-id','r')as I:C.append(I.read().strip())
				except Exception:pass
		elif B.system()==L:
			A=E.run(['ioreg','-rd1','-c','IOPlatformExpertDevice'],capture_output=_C,text=_C,timeout=5)
			if A.returncode==0:
				for D in A.stdout.split(G):
					if'IOPlatformUUID'in D:R=D.split('=')[1].strip().strip('"');C.append(R);break
	except Exception:pass
	C.append(B.system());C.append(B.machine());C.append(B.processor())
	if C:S='|'.join(str(A)for A in C if A);J=_ThVAxRNFloy.sha256(S.encode(_F)).hexdigest()[:32].upper();return J
	T='%s|%s|%s'%(B.node(),B.system(),B.machine());J=_ThVAxRNFloy.sha256(T.encode(_F)).hexdigest()[:32].upper();return J
def _NdZUd81lzxzxmz(_file_path):
	J='ignore';I='__file__';G='import_count';F='function_count';E='code_length';D='code_hash'
	try:
		import inspect,sys,os;A=''
		try:
			import __main__
			if hasattr(__main__,I)and __main__.__file__:
				H=__main__.__file__
				if os.path.exists(H):
					with open(H,'r',encoding=_F,errors=J)as B:A=B.read()
		except Exception:pass
		if not A:
			try:
				K=sys._getframe(1);C=K.f_globals.get(I,'')
				if C and os.path.exists(C):
					with open(C,'r',encoding=_F,errors=J)as B:A=B.read()
			except Exception:pass
		if not A:return{D:'',E:0,F:0,G:0}
		L={D:_ThVAxRNFloy.sha256(A.encode(_F)).hexdigest(),E:len(A),F:A.count('def '),G:A.count('import ')};return L
	except Exception:return{D:'',E:0,F:0,G:0}
def _8sZjknnij(_dummy1=_A,_dummy2=0,_dummy3=_E):
	V='client_md5';U='failed';T='challenge';O='response';J='status';C='type';global _caDLBqOB6Z,_szp2jCefHU80uMCV
	if _caDLBqOB6Z is not _A:raise RuntimeError('Handshake already completed')
	D='tzJ8a9Hez6qd4w2k';W='1.13';X='G5YEXEQTFF7u0Mvv';P='spinnyspiwal.com';Y=2750;Z=_C;Q='';K=5
	if not isinstance(D,str)or len(D)==0:raise RuntimeError('Invalid script ID')
	E=_A
	if _E:import os,inspect,sys;E=_NdZUd81lzxzxmz(_A)
	else:E='YC8IRIIG0E85EECD84DA2250E974502A'
	F=_A
	if _C:F=_tB29CSJs68()
	elif _E:F=_A
	a,G,H=_DLheEfOgPEH31ee(D,X)
	if a is _A or G is _A or H is _A:raise RuntimeError(_O)
	b=_DdNunMt4.create_connection((P,Y),timeout=K);I=_pCEvZGEXKFD.create_default_context()
	if not Z:I.check_hostname=_E;I.verify_mode=_pCEvZGEXKFD.CERT_NONE
	elif Q:I.load_verify_locations(Q)
	A=I.wrap_socket(b,server_hostname=P)
	if A is _A:raise RuntimeError('Socket creation failed')
	L={C:'hello','script_id':D,'client_version':W}
	if E is not _A:L['code_profile']=E
	if F is not _A:L['hwid']=F
	_V3fZoendpvL21pX(A,L);M=_67JpZxzRvV(A,K)
	if not M or M.get(C)!=T:A.close();return _E
	B=M.get(T,{});c=B.get('enc_str',[]);d=B.get('enc_num',[]);e=int(B.get('formula_id',-1));f=int(B.get('offset',0));g=str(B.get('md5',''))
	try:h=_A9FmfY9KH6(c,G,H).decode(_F);i=int(_A9FmfY9KH6(d,G,H).decode(_F))
	except Exception:_V3fZoendpvL21pX(A,{C:O,J:U,'reason':'decrypt_error'});A.close();return _E
	j=_zJP4DWTQHs715po(e,h,i,f);R=str(j);N=_ThVAxRNFloy.md5(R.encode(_F)).hexdigest()
	if N!=g:_V3fZoendpvL21pX(A,{C:O,J:U,V:N});A.close();return _E
	_V3fZoendpvL21pX(A,{C:O,J:'ok','solution':R,V:N});S=_67JpZxzRvV(A,K);A.close()
	if S and S.get(J)=='ok':_caDLBqOB6Z=G;_szp2jCefHU80uMCV=H;return _C
	return _E
if not _8sZjknnij():raise SystemExit(1)
import base64,json,random,struct,time;from dataclasses import dataclass;from typing import Any,Dict,List,Optional
def GispkWga(UbQXAOmx):A=UbQXAOmx;B=_wxh2qKVEjd('mscNsw==')*(-len(A)%_VvpwKQMTsdwjPp(_G));return base64.urlsafe_b64decode(A+B)
def vJyYlfJs(QgPhlGze):
	B='fRiiWWpM0C0P/BkQ';A=QgPhlGze
	try:from cryptography.hazmat.primitives.asymmetric import rsa
	except ImportError as C:raise RuntimeError(_wxh2qKVEjd('q7+UOhtiZ1uXx1I86BaTM1UiLxnwRb0MD/wZEBtiZ1t3u9qK6BaTM6lH/SSXx1I8hr5uUWpM0C0OUZSMhr5uURtiZ1vfoKGUzDlMfDBTjHRqTNAtG2JnW9+goZSygxMngumMRIa+blHoFpMzakzQLegWkzOGvm5RakzQLZUcWHwOUZSMVSIvGXe72oqnBDuypwQ7soa+blGrv5Q6G2JnW5fHUjzoFpMzVSIvGfBFvQwP/BkQG2JnW3e72oroFpMzqUf9JJfHUjw='))from C
	D=int.from_bytes(GispkWga(A[_wxh2qKVEjd('lRxYfA==')]),_wxh2qKVEjd(B));E=int.from_bytes(GispkWga(A[_wxh2qKVEjd('36ChlA==')]),_wxh2qKVEjd(B));return rsa.RSAPublicNumbers(E,D).public_key()
def nylWOheD(HMuxSpmE,MwgwOyyG,OtwydNQa):
	try:from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider as D,WrappingKey as E;from aws_encryption_sdk.identifiers import EncryptionKeyType as F,WrappingAlgorithm as G;from cryptography.hazmat.primitives import serialization as B
	except ImportError as H:raise RuntimeError(_wxh2qKVEjd(_Q))from H
	I=HMuxSpmE;A=MwgwOyyG.encode(_wxh2qKVEjd(_L))
	class J(D):
		HMuxSpmE=I
		def bxEIKfyE(H,KKMNNAPn):
			C=KKMNNAPn
			if C!=A:raise KeyError('Unknown key id:'+str(C))
			D=OtwydNQa.public_bytes(encoding=B.Encoding.PEM,format=B.PublicFormat.SubjectPublicKeyInfo);return E(wrapping_algorithm=G.RSA_OAEP_SHA256_MGF1,wrapping_key=D,wrapping_key_type=F.PUBLIC)
		def TtaduIpn(B):return[A]
	C=J();C.add_master_key(A);return C
@dataclass
class DataType:
	data_type_id:str;qUNdsi:Dict[str,str];provider_id:str;key_id:str;_provider:Any=_A
	def NmzVIYWI(A):
		if A._provider is _A:B=vJyYlfJs(A.qUNdsi);A._provider=nylWOheD(A.provider_id,A.key_id,B)
		return A._provider
TEAJSSXXX=_VvpwKQMTsdwjPp('jiOvSQvfWRp7R/i4UiJNX1IiTV+gdjYBe0f4uOuLl64L31kaMHnteQ==');XXJZ_jsMS=[_VvpwKQMTsdwjPp('j1JFtzBDcI4wQ3COMENwjlIiTV+OI69JNx93duuLl643H3d2e0f4uA=='),_VvpwKQMTsdwjPp('jiOvSXtH+Ljri5euC99ZGjBDcI6PUkW3C99ZGo9SRbcwQ3CONx93dg=='),_VvpwKQMTsdwjPp('jiOvSaB2NgFSIk1f64uXro4jr0mgdjYBjiOvSTcfd3Z7R/i4MENwjg=='),_VvpwKQMTsdwjPp('MENwjuuLl65SIk1fMENwjo9SRbegdjYBoHY2AY9SRbfri5eu')]
def dGrzKhAM(JAGTCTFy):return JAGTCTFy&_VvpwKQMTsdwjPp(_I)
def RMTQsgXc(MTvaTfmx):A=MTvaTfmx;A=A&_VvpwKQMTsdwjPp(_I);return A-_VvpwKQMTsdwjPp(_R)if A>=_VvpwKQMTsdwjPp('jiOvSY9SRbdSIk1f64uXrlIiTV8wQ3COoHY2AQvfWRpSIk1fMENwjg==')else A
def CamwqnaQ(rYmgZBVK,CANbDcwI,vWPjxdLO,IquLsnxf,UoCvTQAX,bJJEUteY):B=CANbDcwI;A=rYmgZBVK;return dGrzKhAM((A>>_VvpwKQMTsdwjPp(_M)^B<<_VvpwKQMTsdwjPp(_J))+(B>>_VvpwKQMTsdwjPp(_H)^A<<_VvpwKQMTsdwjPp(_G))^(vWPjxdLO^B)+(IquLsnxf[UoCvTQAX&_VvpwKQMTsdwjPp(_H)^bJJEUteY]^A))
def AapmwkQr(IPFjbtfc,mHXMjYuO):
	H=mHXMjYuO;C=IPFjbtfc;_wxh2qKVEjd('OvtELzr7RC8kpi5YkCb1Vb2Ok22Gvm5R36ChlJUcWHyrv5Q6G2JnW5fHUjzoFpMzVSIvGYa+blGygxMnd7vailUiLxl3u9qKhr5uURphjG1qTNAtVSIvGalH/SSGvm5Rj1JFt44jr0kwQ3CO1LbFUX0YollqTNAtVSIvGYa+blELHXZ536ChlJfHUjyGvm5RxC5alFIiTV+Gvm5R7uZXGoa+blEwU4x0akzQLZUcWHxVIi8ZoHY2AY4jr0nGWZa2e0v6Lg==');I=(_VvpwKQMTsdwjPp(_G)-len(C)%_VvpwKQMTsdwjPp(_G))%_VvpwKQMTsdwjPp(_G)
	if I:C=C+b'\x00'*I
	A=len(C)//_VvpwKQMTsdwjPp(_G);B=list(struct.unpack('<{}I'.format(A),C))
	if A<_VvpwKQMTsdwjPp(_J):B.append(_VvpwKQMTsdwjPp(_B));A=_VvpwKQMTsdwjPp(_J)
	K=_VvpwKQMTsdwjPp('C99ZGg==')+_VvpwKQMTsdwjPp('e0f4uI4jr0k=')//A;D=_VvpwKQMTsdwjPp(_B);F=B[A-_VvpwKQMTsdwjPp(_D)]
	for L in range(K):
		D=dGrzKhAM(D+TEAJSSXXX);J=D>>_VvpwKQMTsdwjPp(_J)&_VvpwKQMTsdwjPp(_H)
		for E in range(A-_VvpwKQMTsdwjPp(_D)):G=B[E+_VvpwKQMTsdwjPp(_D)];B[E]=dGrzKhAM(B[E]+CamwqnaQ(F,G,D,H,E,J));F=B[E]
		G=B[_VvpwKQMTsdwjPp(_B)];B[A-_VvpwKQMTsdwjPp(_D)]=dGrzKhAM(B[A-_VvpwKQMTsdwjPp(_D)]+CamwqnaQ(F,G,D,H,A-_VvpwKQMTsdwjPp(_D),J));F=B[A-_VvpwKQMTsdwjPp(_D)]
	return struct.pack('<%sI'%A,*B)
def oYPJfeCC():
	B=[]
	for C in range(_VvpwKQMTsdwjPp('jiOvSXtH+LgL31ka')):
		A=C
		for D in range(_VvpwKQMTsdwjPp(_N)):A=A>>_VvpwKQMTsdwjPp(_D)^_VvpwKQMTsdwjPp('oHY2ATB57XkwQ3COMENwjo4jr0kwee15jiOvSaB2NgEwQ3COUiJNXw==')if A&_VvpwKQMTsdwjPp(_D)else A>>_VvpwKQMTsdwjPp(_D)
		B.append(RMTQsgXc(A))
	return B
jVu_dniL=oYPJfeCC()
def jnaDwOvC(frYKmbFO):
	_wxh2qKVEjd('YzmZI3e72oqnBDuyq7+UOjBTjHSnBDuyd7vailUiLxnfoKGUhr5uUWM5mSNN4rNVYzmZI6B2NgGOI69Jhr5uUcxsyTV3u9qKVSIvGau/lDqpR/0kakzQLZUcWHwP/BkQhr5uUUMRBYSIGGmhYzmZI3AHGHt03pA+u196CA5RlIyGvm5RakzQLcxsyTXoFpMzpwQ7st+goZTMbMk136ChlJUcWHxVIi8Zd7vailUiLxlqTNAt8EW9DJUcWHx7S/ou');A=_VvpwKQMTsdwjPp(_I)
	for B in frYKmbFO:A=dGrzKhAM(A>>_VvpwKQMTsdwjPp(_N)^jVu_dniL[(A^ord(B))&_VvpwKQMTsdwjPp('jiOvSXtH+Lh7R/i4')])
	return RMTQsgXc(A^_VvpwKQMTsdwjPp(_I))
def qmUAyzid(fcoWuhjw):
	A=fcoWuhjw;_wxh2qKVEjd('YzmZI/BFvQyVHFh89Muxst+goZQbYmdbVSIvGYa+blEOUZSMakzQLQ/8GRCVHFh836ChlLKDEyeGvm5RakzQLZUcWHxVIi8ZoHY2AY4jr0mGvm5RVSIvGfBFvQyGvm5RMENwjtS2xVGrv5Q6qUf9JHe72oobYmdbhr5uUTBTjHToFpMz6BaTM9+goZQbYmdbq7+UOne72ooOUZSM36ChlIa+blGpR/0k36ChlO7mVxp7S/ou')
	if A<_VvpwKQMTsdwjPp(_B):A=A+_VvpwKQMTsdwjPp(_R)
	return format(A,_wxh2qKVEjd('Nx93djBDcI46+0Qv'))
def nHONklFJ(FlBuTeST=_wxh2qKVEjd('qUf9JFUiLxlVIi8Z6BaTMw5RlIyC6YxEjPQHC4z0Bwt3u9qKMFOMdFUiLxmpR/0ke0v6LgXTlmB3u9qK6BaTM+gWkzPwRb0MDlGUjHtL+i6rv5Q68EW9DMxsyTWM9AcLd7vaiugWkzOM9AcLDlGUjGpM0C0P/BkQlRxYfGpM0C2VHFh8'),FlghriAa=_wxh2qKVEjd('xo48Y3e72oroFpMz6BaTM/BFvQwOUZSMhr5uUb2Ok22VHFh8soMTJxtiZ1vwRb0MakzQLbKDEyc='),znbMNZme=_VvpwKQMTsdwjPp('j1JFtzcfd3YwQ3CONx93dg=='),MPFfUIkS=_VvpwKQMTsdwjPp('j1JFtzB57XmOI69JNx93dg=='),wjyRjnMT=-_VvpwKQMTsdwjPp(_N)):O='GmGMbWpM0C2VHFh8soMTJ/BFvQwaYYxt';N='6BaTMxtiZ1vwRb0M6BaTM9+goZQbYmdbVSIvGWpM0C3foKGUDlGUjA==';M='jiOvSTcfd3Y3H3d2Nx93djcfd3Y3H3d2Nx93djcfd3Y3H3d2Nx93dg==';L='36ChlKcEO7J3u9qK6BaTMw5RlIzfoKGUsoMTJw==';K='jiOvSTcfd3Y=';J='zGzJNXe72opVIi8ZqUf9JA==';I='soMTJ5UcWHxVIi8Z';H='D/wZEOgWkzMwU4x0';G='q7+UOne72oroFpMzd7vain0YollqTNAtpwQ7smpM0C1VIi8ZakzQLd+goZQOUZSM';F=MPFfUIkS;E=FlBuTeST;D='j1JFtzcfd3Y=';B='j1JFtzcfd3Y3H3d2Nx93dg==';_wxh2qKVEjd('HHVnT9+goZSVHFh836ChlBtiZ1t3u9qKVSIvGd+goZSGvm5RsoMTJ9+goZT0y7GyakzQLau/lDrfoKGUhr5uUc3jpRhqTNAtlRxYfA/8GRDfoKGUG2JnW+gWkzMbYmdbakzQLZUcWHxVIi8Zhr5uUbKDEyd3u9qKVSIvGXe72oqGvm5RDlGUjFUiLxkbYmdbMFOMdKu/lDpVIi8ZMFOMdBtiZ1vfoKGUe0v6Lg==');C=int(time.time()*_VvpwKQMTsdwjPp(B));A=C-random.randint(_VvpwKQMTsdwjPp(B),_VvpwKQMTsdwjPp('e0f4uDcfd3Y3H3d2Nx93dg=='));return{_wxh2qKVEjd('zGzJNd+goZRVIi8ZG2JnW2pM0C2rv5Q6DlGUjA=='):{_wxh2qKVEjd('36ChlKcEO7I='):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('DlGUjKu/lDobYmdbakzQLegWkzNVIi8Z'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('qUf9JA=='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('fRiiWXe72opVIi8ZVSIvGQ=='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('6BaTM9+goZQbYmdbzeOlGA=='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('d7vaijBTjHRVIi8Z8EW9DA=='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd(G):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd(H):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd(I):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd(J):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('zeOlGOgWkzOOI69J'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('pwQ7sg5RlIwwU4x0fRiiWWpM0C2ygxMn'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('VSIvGQXTlmA='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('fRiiWRtiZ1vwRb0MGmGMbQ5RlIzfoKGUG2JnWw=='):_VvpwKQMTsdwjPp(_B)},_wxh2qKVEjd('DlGUjFUiLxl3u9qKG2JnW1UiLxk='):A,_wxh2qKVEjd('akzQLZUcWHxVIi8Z36ChlBtiZ1t3u9qKq7+UOlUiLxlqTNAt8EW9DJUcWHw='):{_wxh2qKVEjd('q7+UOqcEO7JqTNAtq7+UOgsddnkOUZSM'):random.randint(_VvpwKQMTsdwjPp(_B),_VvpwKQMTsdwjPp(_H)),_wxh2qKVEjd('VSIvGfBFvQwwU4x0q7+UOqlH/STfoKGUDlGUjA=='):random.randint(_VvpwKQMTsdwjPp(_B),_VvpwKQMTsdwjPp(_M)),_wxh2qKVEjd('Cx12ed+goZSXx1I8quIxUBtiZ1vfoKGUDlGUjA5RlIzfoKGUDlGUjA=='):random.randint(_VvpwKQMTsdwjPp(_M),_VvpwKQMTsdwjPp(K)),_wxh2qKVEjd('q7+UOjBTjHRVIi8ZDlGUjA=='):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('q7+UOvBFvQzoFpMzakzQLd+goZQOUZSM'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('6BaTM3e72ooOUZSMVSIvGd+goZQOUZSM'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('Cx12ed+goZSXx1I8quIxUBtiZ1vfoKGUDlGUjA5RlIwkpi5YakzQLcxsyTXfoKGUcAcYe5UcWHxVIi8Z36ChlBtiZ1v0y7Gyd7vaiqcEO7IOUZSM'):[],_wxh2qKVEjd('zGzJNfBFvQwwU4x0DlGUjN+goZRjOZkjpwQ7smpM0C2rv5Q6Cx12eariMVDwRb0MDlGUjGpM0C1VIi8ZakzQLfBFvQyVHFh8DlGUjA=='):[],_wxh2qKVEjd('Cx12ed+goZSXx1I8YzmZI5fHUjyrv5Q6pwQ7st+goZQOUZSM'):[],_wxh2qKVEjd('zGzJNfBFvQwwU4x0DlGUjN+goZRjOZkjl8dSPKu/lDqnBDuy36ChlA5RlIw='):[],_wxh2qKVEjd('VSIvGfBFvQwwU4x0q7+UOqlH/SRjOZkjl8dSPKu/lDqnBDuy36ChlA5RlIw='):[]},_wxh2qKVEjd('DlGUjKu/lDobYmdbakzQLegWkzNVIi8ZDlGUjA=='):{_wxh2qKVEjd('soMTJ5fHUjyVHFh8d7vaisxsyTVqTNAtq7+UOg2quRwbYmdbpwQ7sg5RlIw='):[_wxh2qKVEjd('qUf9JFUiLxlVIi8Z6BaTMw5RlIyC6YxEjPQHC4z0BwvMbMk1e0v6LsxsyTXfoKGUsoMTJ2pM0C13u9qK1LbFUXe72orMbMk1d7vaigXTlmDwRb0MlRxYfHtL+i6rv5Q68EW9DMxsyTWM9AcLakzQLcxsyTV3u9qKD/wZEN+goZQOUZSMjPQHC3AHGHuM9AcLMENwjo9SRbcF05ZghxO/i49SRbfMbMk1Nx93dlv5+KEF05ZgE14Xd8jenCJ7S/ouTwLyBQ5RlIynplGJvY6TbQ2quRxwBxh7YzmZI6cEO7JqTNAt36ChlJUcWHxVIi8ZDlGUjIz0BwtDEQWEiBhpoWM5mSNwBxh7dN6QPr2Ok20OUZSMDlGUjN+goZRVIi8ZDlGUjA==')],_wxh2qKVEjd('akzQLZUcWHynBDuyakzQLZUcWHzfoKGU2UygBHe72ooOUZSMqUf9JN+goZQOUZSM'):[random.randint(-_VvpwKQMTsdwjPp(M),_VvpwKQMTsdwjPp(M))for A in range(_VvpwKQMTsdwjPp(D))],_wxh2qKVEjd(L):random.randint(_VvpwKQMTsdwjPp(_D),_VvpwKQMTsdwjPp(D)),_wxh2qKVEjd('soMTJ5fHUjyVHFh8d7vaisxsyTVqTNAtq7+UOg2quRwbYmdbpwQ7smM5mSPwRb0MMFOMdJUcWHxVIi8Z'):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('akzQLZUcWHynBDuyakzQLZUcWHzfoKGU2UygBHe72ooOUZSMqUf9JN+goZQOUZSMYzmZI/BFvQwwU4x0lRxYfFUiLxk='):_VvpwKQMTsdwjPp(D)},_wxh2qKVEjd('qUf9JGpM0C0OUZSMVSIvGfBFvQwbYmdbl8dSPA=='):{_wxh2qKVEjd('pwQ7st+goZSVHFh8D/wZEFUiLxmpR/0k'):random.randint(_VvpwKQMTsdwjPp(_D),_VvpwKQMTsdwjPp(K))},_wxh2qKVEjd('fRiiWXe72opVIi8ZVSIvGd+goZQbYmdbl8dSPA=='):{},_wxh2qKVEjd('6BaTM9+goZQbYmdbzeOlGPBFvQwbYmdbzGzJNXe72oqVHFh8q7+UOt+goZQ='):{_wxh2qKVEjd('VSIvGWpM0C3MbMk1akzQLZUcWHwP/BkQ'):{_wxh2qKVEjd('q7+UOvBFvQyVHFh8lRxYfN+goZSrv5Q6VSIvGd2m0lJVIi8Zd7vaihtiZ1tVIi8Z'):A-_VvpwKQMTsdwjPp(B),_wxh2qKVEjd('DlGUjN+goZSrv5Q6MFOMdBtiZ1vfoKGUYzmZI/BFvQyVHFh8lRxYfN+goZSrv5Q6VSIvGWpM0C3wRb0MlRxYfN2m0lJVIi8Zd7vaihtiZ1tVIi8Z'):_VvpwKQMTsdwjPp(_B),_wxh2qKVEjd('soMTJ/BFvQzMbMk1YzmZI/BFvQzMbMk16BaTM6cEO7LfoKGUVSIvGd+goZQ='):A-_VvpwKQMTsdwjPp('C99ZGo9SRbc3H3d2'),_wxh2qKVEjd('lRxYfHe72or0y7GyakzQLQ/8GRB3u9qKVSIvGWpM0C3wRb0MlRxYfN2m0lJVIi8Zd7vaihtiZ1tVIi8Z'):A-_VvpwKQMTsdwjPp('j1JFtzcfd3Y3H3d2e0f4uA=='),_wxh2qKVEjd('pwQ7svBFvQx3u9qKsoMTJ5Am9VX0y7Gy36ChlJUcWHxVIi8ZkCb1VZUcWHyygxMn'):A-_VvpwKQMTsdwjPp('C99ZGjcfd3Y3H3d2'),_wxh2qKVEjd('G2JnW9+goZQOUZSM6BaTM/BFvQyVHFh8DlGUjN+goZSQJvVVlRxYfLKDEyc='):A-_VvpwKQMTsdwjPp('64uXrjcfd3Y3H3d2'),_wxh2qKVEjd('zeOlGN+goZRVIi8Zq7+UOqlH/STdptJSVSIvGXe72oobYmdbVSIvGQ=='):A-_VvpwKQMTsdwjPp(B)}},_wxh2qKVEjd('d7vaijBTjHRVIi8Z8EW9DMxsyTV3u9qKVSIvGWpM0C3wRb0MlRxYfA=='):{_wxh2qKVEjd('GmGMbbKDEyc='):{_wxh2qKVEjd(N):{_wxh2qKVEjd('soMTJ/BFvQyrv5Q6MFOMdMxsyTXfoKGUlRxYfFUiLxk='):[],_wxh2qKVEjd(O):[],_wxh2qKVEjd('lRxYfHe72or0y7GyakzQLQ/8GRB3u9qKVSIvGfBFvQwbYmdb'):[]}},_wxh2qKVEjd('6BaTM6lH/SR3u9qKlRxYfFUiLxnwRb0MzGzJNQ=='):{_wxh2qKVEjd(N):{_wxh2qKVEjd(O):[]}}},_wxh2qKVEjd('36ChlJUcWHyygxMn'):C,_wxh2qKVEjd(G):{_wxh2qKVEjd('q7+UOg5RlIwOUZSM'):{_wxh2qKVEjd('VSIvGd+goZTu5lcaVSIvGd2m0lKpR/0kd7vairKDEyfwRb0MGmGMbQ=='):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('iBhpod+goZR9GKJZCx12eWpM0C1VIi8ZJKYuWN+goZTu5lcaVSIvGd2m0lJVIi8ZG2JnW/BFvQwLHXZ536ChlA=='):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('fRiiWfBFvQzu5lca3abSUqlH/SR3u9qKsoMTJ/BFvQwaYYxt'):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('fRiiWfBFvQwbYmdbsoMTJ9+goZQbYmdbTeKzVXe72oqygxMnakzQLTBTjHQOUZSM'):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('fRiiWfBFvQwbYmdbsoMTJ9+goZQbYmdbcAcYe8xsyTV3u9qKD/wZEN+goZQ='):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('8EW9DOgWkzN3u9qKq7+UOmpM0C1VIi8Zl8dSPA=='):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('VSIvGRtiZ1t3u9qKlRxYfA5RlIzN46UY8EW9DBtiZ1vMbMk1'):_VvpwKQMTsdwjPp(_D),_wxh2qKVEjd('VSIvGRtiZ1t3u9qKlRxYfA5RlIxqTNAtVSIvGWpM0C3wRb0MlRxYfA=='):_VvpwKQMTsdwjPp(_D)},_wxh2qKVEjd('TwLyBQ5RlIw='):{_wxh2qKVEjd('d7vaijBTjHSygxMnakzQLfBFvQw='):_C,_wxh2qKVEjd('D/wZEN+goZTwRb0MpwQ7svBFvQyrv5Q6d7vailUiLxlqTNAt8EW9DJUcWHw='):_C,_wxh2qKVEjd('pwQ7svBFvQyrv5Q6d7vaiqcEO7LdptJSVSIvGfBFvQwbYmdbd7vaig/8GRDfoKGU'):_wxh2qKVEjd('DlGUjDBTjHToFpMz6BaTM/BFvQwbYmdbVSIvGd+goZSygxMn'),_wxh2qKVEjd('VSIvGfBFvQwwU4x0q7+UOqlH/SQ='):_C,_wxh2qKVEjd('9MuxsmpM0C2ygxMn36ChlPBFvQw='):_C,_wxh2qKVEjd('GmGMbd+goZR9GKJZiBhpofBFvQwbYmdbCx12ed+goZQbYmdb'):_C},_wxh2qKVEjd(L):_VvpwKQMTsdwjPp(_B)},_wxh2qKVEjd(H):{_wxh2qKVEjd('9Muxst+goZSVHFh8soMTJ/BFvQwbYmdb'):_wxh2qKVEjd('E14XdzBTjHR3u9qKpwQ7squ/lDrwRb0MzGzJNcxsyTU='),_wxh2qKVEjd('zGzJNfBFvQyygxMn36ChlKcEO7I='):_wxh2qKVEjd('vY6TbbKDEycbYmdb36ChlJUcWHzwRb0Mhr5uUcQuWpQkpi5YdN6QPsZZlraGvm5RC99ZGntH+Lg3H3d2'),_wxh2qKVEjd('36ChlO7mVxpVIi8Z36ChlJUcWHwOUZSMakzQLfBFvQyVHFh8DlGUjA=='):[_wxh2qKVEjd('iBhpoZAm9VXpyk8HHHVnT8jenCLWwtohsoMTJ9+goZR9GKJZMFOMdA/8GRDWwtohG2JnW9+goZSVHFh8soMTJ9+goZQbYmdb36ChlBtiZ1vWwtohakzQLZUcWHzN46UY8EW9DA=='),_wxh2qKVEjd('iBhpoZAm9VXpyk8HHHVnT8jenCLWwtohpwQ7svBFvQwOUZSM36ChlNbC2iGrv5Q68EW9DJUcWHxVIi8Z36ChlO7mVxpVIi8Z')]},_wxh2qKVEjd(I):_A,_wxh2qKVEjd(J):{_wxh2qKVEjd('VSIvGXe72oqVHFh8'):_wxh2qKVEjd('1LbFUY9SRbd7S/ouUiJNX44jr0mPUkW3UiJNX1IiTV8wQ3COMENwjo4jr0mgdjYBMENwjuuLl65SIk1f64uXro4jr0lSIk1fe0f4uA=='),_wxh2qKVEjd('DlGUjGpM0C2VHFh8'):_wxh2qKVEjd('Nx93dntL+i4wQ3COj1JFt+uLl64wQ3COMENwjo9SRbcwee15j1JFt44jr0mPUkW3j1JFt3tH+Lgwee15Nx93djBDcI57R/i4'),_wxh2qKVEjd('q7+UOvBFvQwOUZSM'):_wxh2qKVEjd('1LbFUTcfd3Z7S/oue0f4uOuLl657R/i4oHY2ATBDcI4L31kaj1JFt49SRbePUkW3MHnteXtH+Ljri5eue0f4uFIiTV8wee15j1JFtw==')},_wxh2qKVEjd('zeOlGKcEO7J3u9qKDlGUjKlH/SSSA9Fq36ChlBtiZ1sOUZSMakzQLfBFvQyVHFh8'):_A,_wxh2qKVEjd('6BaTM6cEO7IwU4x0D/wZEGpM0C2VHFh8DlGUjA=='):'',_wxh2qKVEjd('soMTJzBTjHToFpMz36ChlLKDEyeq4jFQpwQ7sjBTjHQP/BkQakzQLZUcWHwOUZSM'):'',_wxh2qKVEjd('DlGUjKu/lDobYmdb36ChlN+goZSVHFh8cAcYe5UcWHzN46UY8EW9DA=='):str(znbMNZme)+'-'+str(F)+'-'+str(F)+'-0-*-*-*',_wxh2qKVEjd('pwQ7sg5RlIwNqrkcfRiiWWpM0C2ygxMn'):'X%s-%s-%s:%s'%(random.randint(10,99),random.randint(1000000,9999999),random.randint(1000000,9999999),C),_wxh2qKVEjd('VSIvGWpM0C3MbMk136ChlMaOPGPwRb0MlRxYfN+goZQ='):wjyRjnMT,_wxh2qKVEjd('G2JnW9+goZTN46UY36ChlBtiZ1sbYmdb36ChlBtiZ1s='):E,_wxh2qKVEjd('MFOMdA5RlIzfoKGUG2JnW72Ok20P/BkQ36ChlJUcWHxVIi8Z'):FlghriAa,_wxh2qKVEjd('pwQ7svBFvQyrv5Q6d7vailUiLxlqTNAt8EW9DJUcWHw='):E,_wxh2qKVEjd('GmGMbd+goZR9GKJZKTI0LxtiZ1tqTNAt9Muxst+goZQbYmdb'):_E,_wxh2qKVEjd('36ChlBtiZ1sbYmdb8EW9DBtiZ1sOUZSM'):[],_wxh2qKVEjd('9Muxst+goZQbYmdbDlGUjGpM0C3wRb0MlRxYfA=='):_wxh2qKVEjd('UiJNX3tL+i43H3d2e0v6Ljcfd3Y=')}
def generate_metadata1(QJRDbRXO=_A):
	A=QJRDbRXO
	if A is _A:A=nHONklFJ()
	B=json.dumps(A,separators=(_wxh2qKVEjd('zUW6bA=='),_wxh2qKVEjd('gumMRA==')));C=jnaDwOvC(B);D=qmUAyzid(C);E='%s#%s'%(D,B);F=AapmwkQr(E.encode(_wxh2qKVEjd(_L)),XXJZ_jsMS);G=base64.b64encode(F).decode(_wxh2qKVEjd(_S));return'ECdITeCs:{}'.format(G)
class SiegeCrypto:
	def __init__(A):A.KuvuOL={};A.uhvGUUy={}
	def add_profile(A,fwshRIgW,PlXqfqnG):A.uhvGUUy[fwshRIgW]=PlXqfqnG
	def add_data_type(B,*,NAtmitCP,ngnUkIXu,YXrrlRhK,cZUPUtPs):A=NAtmitCP;B.KuvuOL[A]=DataType(data_type_id=A,qUNdsi=ngnUkIXu,provider_id=YXrrlRhK,key_id=cZUPUtPs)
	def encrypt_string(B,GSTKCYEP,*,vGDAIpgd,XoDKCWZt=_E,pVPeQXuw=_A):
		C=GSTKCYEP;A=vGDAIpgd
		try:from aws_encryption_sdk import EncryptionSDKClient as F,CommitmentPolicy as G;from aws_encryption_sdk.identifiers import Algorithm as H
		except ImportError as I:raise RuntimeError(_wxh2qKVEjd(_Q))from I
		if A not in B.KuvuOL:raise KeyError('Unknown data type:'+str(A))
		J=B.KuvuOL[A];K=J.NmzVIYWI();L=C.encode(_wxh2qKVEjd(_L));M=pVPeQXuw or{};N=F(commitment_policy=G.FORBID_ENCRYPT_ALLOW_DECRYPT);O,P=N.encrypt(source=L,key_provider=K,encryption_context=M,frame_length=_VvpwKQMTsdwjPp(_B),algorithm=H.AES_128_GCM_IV12_TAG16);D=base64.b64encode(O).decode(_wxh2qKVEjd(_S))
		if XoDKCWZt:
			E=''.join(A for A in C if A not in _wxh2qKVEjd('hr5uUdS2xVE='))[-_VvpwKQMTsdwjPp(_G):]
			if len(E)>_VvpwKQMTsdwjPp(_H):D+=_wxh2qKVEjd('bA+fVA==')+E
		return D
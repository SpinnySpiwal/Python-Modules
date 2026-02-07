AX='JR8GOl0d5TMm3EacyzW2u8s1trs='
AW='0SqSTw=='
AV='CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
AU='JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA=='
AT='sysctl'
AS='Handshake not completed'
AR='Keypair generation failed'
AQ='bgGaS9oCygoR8uaH'
AP='spinnyspiwal.com'
AO=KeyError
A6='SNZXXA=='
A5='IBQbTQ=='
A4='aKpbAPZ/QUbUMBAA0Osqb0jWV1w='
A3='script_id'
A2=b'\n'
A1=ImportError
A0=bytearray
s='rkMOsQ=='
r='CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='
q='r'
p='debugserver'
o='-p'
n='ascii'
m=open
i='S/wQmQ=='
h='ps'
c='type'
X='CIEKEw=='
W=FileNotFoundError
V=range
T='\n'
S=int
Q=bytes
O=isinstance
N='utf-8'
M=''
L=RuntimeError
J='t0mqGw=='
I=Exception
H=len
G='t8YL1g=='
F=False
E=str
D=True
C=None
import socket as A7,ssl as Y,json as A8,hashlib as Z,time as d,struct as AY,os as a,subprocess as K,threading as AZ,platform as B2,resource as A9
R=C
U=C
AA=D
t='https://spinnyspiwal.com:443/api/metrics'
e=C
j=C
k=C
u=AP
AB=2750
AC=D
v=M
AD=5
w=AQ
def AE(_a,_b,_dummy1=C,_dummy2=0,_dummy3=F):
	A=_b
	while A:
		_a,A=A,_a%A;B=_dummy1 is C or _dummy2==0 or not _dummy3
		if not B:0
	return _a
def Aa(_a,_m,_dummy1=C,_dummy2=M,_dummy3=[]):
	A,E=0,1;D,B=_m,_a
	while B!=0:
		F=D//B;A,E=E,A-F*E;D,B=B,D-F*B
		if _dummy1 is not C or _dummy2!=M or H(_dummy3)!=0:0
	if D>1:return
	if A<0:A=A+_m
	return A
def Ab(_n,_dummy1=0,_dummy2=C):
	A=_n
	if A<2:return F
	if A%2==0:return A==2
	B=3
	while B*B<=A:
		if A%B==0:return F
		B+=2
		if _dummy1!=0 or _dummy2 is not C:0
	return D
def x(_n,_dummy1=M,_dummy2=[]):
	if _n<=2:return 2
	A=_n if _n%2!=0 else _n+1
	while not Ab(A):A+=2
	return A
def AF(_seed,_dummy1=C,_dummy2=0):
	A=_seed&2147483647
	def B(_dummy3=F):nonlocal A;A=1103515245*A+12345&2147483647;return A
	return B
def Ac(_script_id,_key_salt,_dummy1=C,_dummy2=0,_dummy3=F):
	J=_script_id+':'+_key_salt;K=S(Z.sha256(J.encode(N)).hexdigest(),16);F=AF(K);D=x(40000+F()%20000);B=x(50000+F()%20000)
	if D==B:B=x(B+2)
	G=D*B;E=(D-1)*(B-1);M=[65537,257,17,5,3];A=C
	for H in M:
		if AE(H,E)==1:A=H;break
	if A is C:
		A=3
		while AE(A,E)!=1:A+=2
	I=Aa(A,E)
	if I is C or A is C or G is C:raise L(AR)
	return A,I,G
def y(_data,_d,_n,_dummy1=C):
	if _d is C or _n is C:raise L('Decryption keys not available')
	return Q([pow(S(A),_d,_n)for A in _data])
def AG(_packed_bytes,_dummy1=M):
	A=_packed_bytes
	if not O(A,Q):
		if O(A,E):
			try:A=A.encode('latin-1')
			except I:raise L('Invalid packed data format:cannot convert string to bytes')
		elif O(A,(list,tuple)):
			try:A=Q(A)
			except I:raise L('Invalid packed data format:cannot convert list to bytes')
		else:
			try:A=Q(A)
			except I:raise L('Invalid packed data format:cannot convert to bytes')
	B=H(A)//4;D='<'+E(B)+'I'
	if B<=0 or H(A)%4!=0:C=H(A);F=C%4;raise L('Invalid packed data format:length='+E(C)+',count='+E(B)+',remainder='+E(F))
	return list(AY.unpack(D,A))
def A(_enc_b64,_dummy1=C):
	A=_enc_b64;global R,U
	if R is C or U is C:raise L(AS)
	import base64 as B;D=B.b64decode(A.encode(n)if O(A,E)else A);F=AG(D);return y(F,R,U).decode(N)
def B(_enc_b64,_dummy1=0):
	A=_enc_b64;global R,U
	if R is C or U is C:raise L(AS)
	import base64 as B;D=B.b64decode(A.encode(n)if O(A,E)else A);F=AG(D);return S(y(F,R,U).decode(N))
def B3(_seed,_dummy1=C):
	B=AF(_seed);A=A0(32)
	for C in V(32):A[C]=B()%256
	return Q(A)
def Ad(_data,_key,_dummy1=C):
	C=_data;A=_key
	if not O(C,Q):C=C.encode(N)
	if not O(A,Q):A=A.encode(N)if O(A,E)else Q(A)
	D=Z.sha256(A).digest();F=A0()
	for B in V(H(C)):I=D[B%H(D)];F.append((I^B&255)&255)
	G=A0(H(C))
	for B in V(H(C)):J=F[B];K=A[B%H(A)]if H(A)>0 else 0;L=D[B*7%H(D)];G[B]=(C[B]^J^K^L^B&255)&255
	return Q(G)
def AH(_data,_key,_dummy1=0):return Ad(_data,_key)
def Ae(_formula_id,_s,_n,_offset,_dummy1=C,_dummy2=0):
	B=_offset;A=_formula_id
	if A==0:return H(_s)+_n+B
	if A==1:return(sum(ord(A)for A in _s)^_n)+B
	if A==2:return _n*(H(_s)or 1)+B
	if A==3:return sum(ord(A)for A in _s)+_n-B
	return-1
def f(_sock,_obj,_dummy1=C):A=A8.dumps(_obj,separators=(',',':')).encode(N)+A2;_sock.sendall(A)
def AI(_sock,_timeout,_dummy1=0,_dummy2=C):
	A=b'';E=d.time()
	while D:
		if d.time()-E>_timeout:return
		B=_sock.recv(4096)
		if not B:return
		A+=B
		if A2 in A:
			C,F=A.split(A2,1)
			if not C:return
			return A8.loads(C.decode(N))
		if H(A)>65536:return
def Af(_metrics_data,_dummy1=C):
	global t
	if not t:return F
	try:
		import urllib.request,json;D=json.dumps(_metrics_data).encode(N);C=urllib.request.Request(t,data=D,headers={'Content-Type':'application/json'},method='POST')
		try:A=Y.create_default_context();B=urllib.request.urlopen(C,timeout=5,context=A);return B.getcode()==200
		except I:
			try:A=Y._create_unverified_context();B=urllib.request.urlopen(C,timeout=5,context=A);return B.getcode()==200
			except I:return F
	except I:return F
def Ag(_detection_type,_dummy1=C,_dummy2=0):
	global u,AB,AC,v,AD,w
	try:
		C=A7.create_connection((u,AB),timeout=AD);A=Y.create_default_context()
		if not AC:A.check_hostname=F;A.verify_mode=Y.CERT_NONE
		elif v:A.load_verify_locations(v)
		B=A.wrap_socket(C,server_hostname=u);D={c:'debugger_detected',A3:w,'detection_type':_detection_type};f(B,D);B.close()
	except I:pass
def b(_detection_type,_dummy1=C,_dummy2=0):Ag(_detection_type);d.sleep(.1);a._exit(1)
def Ah(_dummy1=C,_dummy2=0,_dummy3=F):
	try:
		A=a.getppid()
		if A==1:return'orphaned_process'
		try:
			B=K.run([h,o,E(A),'-o','comm='],capture_output=D,text=D,timeout=1)
			if B.returncode==0:
				G=B.stdout.strip().lower();H=['lldb','gdb',p,'dtrace']
				for C in H:
					if C in G:return'parent_'+C
		except(K.TimeoutExpired,W):pass
	except I:pass
	return F
def Ai(_dummy1=C):
	try:
		C=a.getppid();A=K.run([h,o,E(C),'-o','comm='],capture_output=D,text=D,timeout=1)
		if A.returncode==0:
			G=A.stdout.strip().lower();H=['lldb','gdb',p]
			for B in H:
				if B in G:return'process_tree_'+B
	except I:pass
	return F
def Aj(_dummy1=0,_dummy2=C):
	try:
		B=a.getpid();C='proc.pid.'+E(B)+'.status';A=K.run([AT,'-n',C],capture_output=D,text=D,timeout=1)
		if A.returncode==0:
			G=A.stdout.strip()
			if'traced'in G.lower():return'ptrace_traced'
	except(K.TimeoutExpired,W,K.SubprocessError):pass
	except I:pass
	return F
def Ak(_dummy1=C,_dummy2=0):return F
def Al(_dummy1=0,_dummy2=C,_dummy3=F):
	try:
		B=a.getpid()
		try:
			A=K.run(['lsof',o,E(B)],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				if p in A.stdout.lower():return'lldb_lsof'
		except(K.TimeoutExpired,W):pass
		try:
			A=K.run([h,'aux'],capture_output=D,text=D,timeout=2)
			if A.returncode==0:
				for C in A.stdout.split(T):
					if p in C.lower():
						G='--attach='+E(B);H='--attach '+E(B)
						if G in C or H in C:return'lldb_ps_attach'
		except(K.TimeoutExpired,W):pass
	except I:pass
	return F
def Am(_dummy1=0,_dummy2=C,_dummy3=F):
	L='sample'
	try:
		G=a.getpid()
		try:
			A=K.run([h,'aux'],capture_output=D,text=D,timeout=2)
			if A.returncode==0:
				C=A.stdout.lower();J=C.split(T)
				for B in J:
					if('activity monitor'in B or L in B)and E(G)in B:return'activity_monitor_ps'
					if L in B:
						M=B.split()
						if H(M)>=2:
							try:
								if M[1]==E(G):return'activity_monitor_sample'
							except(ValueError,IndexError):pass
		except(K.TimeoutExpired,W):pass
		try:
			A=K.run([h,'-ax','-o','pid,command'],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				C=A.stdout.lower();J=C.split(T)
				for B in J:
					if'/usr/sbin/spindump -stdout'in B:return'spindump_stdout_psax'
		except(K.TimeoutExpired,W):pass
		try:
			A=K.run(['lsof',o,E(G)],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				C=A.stdout.lower()
				if L in C or'activity'in C:return'activity_monitor_lsof'
		except(K.TimeoutExpired,W):pass
	except I:pass
	return F
def An(_dummy1=C):
	global AA,j,k
	while AA:
		try:
			B=A9.getrusage(A9.RUSAGE_SELF);E=B.ru_utime+B.ru_stime;D=d.time();global e;F=.0
			if j is not C and k is not C:
				G=D-k
				if G>0:H=E-j;F=min(H/G*1e2,1e2)
			j=E;k=D;J={A3:w,'hwid':e,'cpu_usage':f"{F:.2f}%",'memory_usage':f"{B.ru_maxrss/1024/1024:.2f} MB",'timestamp':D};Af(J);A=Ah()
			if A:b(A);break
			A=Ai()
			if A:b(A);break
			A=Aj()
			if A:b(A);break
			A=Ak()
			if A:b(A);break
			A=Al()
			if A:b(A);break
			A=Am()
			if A:b(A);break
			d.sleep(.5)
		except I:pass
def Ao(_dummy1=0,_dummy2=C):A=AZ.Thread(target=An,daemon=D);A.start();return A
def l():print('\x1b[1;91m[Error]\x1b[0m Your script version is outdated. Please obtain the latest version.');import sys;sys.exit(1)
def AJ(_dummy1=C):
	V='get';U='wmic';S='ether';R='link/ether';Q='Linux';P='Darwin';O='Windows';import platform as B,hashlib,subprocess as G,sys;C=[]
	try:
		if B.system()==O:
			A=G.run(['getmac','/fo','csv','/nh'],capture_output=D,text=D,timeout=5)
			if A.returncode==0 and A.stdout:
				J=A.stdout.split(T)[0].split(',')[0].strip().replace('-',':')
				if J and J!='N/A':C.append(J)
		elif B.system()==Q:
			A=G.run(['ip','link','show'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for F in A.stdout.split(T):
					if R in F:J=F.split(R)[1].split()[0];C.append(J);break
		elif B.system()==P:
			A=G.run(['ifconfig'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for F in A.stdout.split(T):
					if S in F.lower():J=F.split(S)[1].split()[0];C.append(J);break
	except I:pass
	try:
		if B.system()==O:
			A=G.run([U,'cpu',V,'ProcessorId'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				K=[A.strip()for A in A.stdout.split(T)if A.strip()]
				if H(K)>1:C.append(K[1])
		elif B.system()==P:
			A=G.run([AT,'-n','machdep.cpu.brand_string'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:C.append(A.stdout.strip())
	except I:pass
	try:
		if B.system()==O:
			A=G.run([U,'csproduct',V,'uuid'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				K=[A.strip()for A in A.stdout.split(T)if A.strip()]
				if H(K)>1:C.append(K[1])
		elif B.system()==Q:
			try:
				with m('/etc/machine-id',q)as L:C.append(L.read().strip())
			except I:
				try:
					with m('/var/lib/dbus/machine-id',q)as L:C.append(L.read().strip())
				except I:pass
		elif B.system()==P:
			A=G.run(['ioreg','-rd1','-c','IOPlatformExpertDevice'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for F in A.stdout.split(T):
					if'IOPlatformUUID'in F:W=F.split('=')[1].strip().strip('"');C.append(W);break
	except I:pass
	C.append(B.system());C.append(B.machine());C.append(B.processor())
	if C:X='|'.join(E(A)for A in C if A);M=Z.sha256(X.encode(N)).hexdigest()[:32].upper();return M
	Y=f"{B.node()}|{B.system()}|{B.machine()}";M=Z.sha256(Y.encode(N)).hexdigest()[:32].upper();return M
def Ap(_file_path):
	L='ignore';K='__file__';G='import_count';F='function_count';E='code_length';D='code_hash'
	try:
		import inspect,sys,os;A=M
		try:
			import __main__
			if hasattr(__main__,K)and __main__.__file__:
				J=__main__.__file__
				if os.path.exists(J):
					with m(J,q,encoding=N,errors=L)as B:A=B.read()
		except I:pass
		if not A:
			try:
				O=sys._getframe(1);C=O.f_globals.get(K,M)
				if C and os.path.exists(C):
					with m(C,q,encoding=N,errors=L)as B:A=B.read()
			except I:pass
		if not A:return{D:M,E:0,F:0,G:0}
		P={D:Z.sha256(A.encode(N)).hexdigest(),E:H(A),F:A.count('def '),G:A.count('import ')};return P
	except I:return{D:M,E:0,F:0,G:0}
def Aq(_dummy1=C,_dummy2=0,_dummy3=F):
	z='client_md5';x='failed';w='challenge';v='tamper_detected';u='outdated_version';k='response';J='error';G='status';global R,U,e
	if R is not C:raise L('Handshake already completed')
	V=AQ;A0='1.06';A1='yXwJa1i7YwGZZ1ZMHteChJ';m=AP;A2=2750;A4=D;o=M;a=5
	if not O(V,E)or H(V)==0:raise L('Invalid script ID')
	W=C
	if F:import os,inspect,sys;W=Ap(C)
	else:W='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
	P=C
	if D:P=AJ()
	elif F:P=C
	else:P=AJ()
	p,b,d=Ac(V,A1)
	if p is C or b is C or d is C:raise L(AR)
	A5=A7.create_connection((m,A2),timeout=a);X=Y.create_default_context()
	if not A4:X.check_hostname=F;X.verify_mode=Y.CERT_NONE
	elif o:X.load_verify_locations(o)
	A=X.wrap_socket(A5,server_hostname=m)
	if A is C:raise L('Socket creation failed')
	g={c:'hello',A3:V,'client_version':A0}
	if W is not C:g['code_profile']=W
	if P is not C:g['hwid']=P
	f(A,g);K=AI(A,a)
	if not K:A.close();return F
	if K.get(G)==J and K.get(J)==u:A.close();l();return F
	if K.get(G)==J and K.get(J)==v:A.close();l();return F
	if K.get(c)!=w:A.close();return F
	T=K.get(w,{});A6=T.get('sym_key',[]);h=T.get('enc_str',M);i=T.get('enc_num',M);A8=S(T.get('formula_id',-1));A9=S(T.get('offset',0));AA=E(T.get('md5',M))
	try:
		q=y(A6,b,d)
		if H(q)<32:raise L('Invalid symmetric key length')
		r=Q(q[:32]);import base64 as s;AB=s.b64decode(h.encode(n)if O(h,E)else h);AC=s.b64decode(i.encode(n)if O(i,E)else i);AD=AH(AB,r).decode(N);AE=S(AH(AC,r).decode(N))
	except I as p:f(A,{c:k,G:x,'reason':'decrypt_error'});A.close();return F
	AF=Ae(A8,AD,AE,A9);t=E(AF);j=Z.md5(t.encode(N)).hexdigest()
	if j!=AA:f(A,{c:k,G:x,z:j});A.close();return F
	f(A,{c:k,G:'ok','solution':t,z:j});B=AI(A,a);A.close()
	if B and B.get(G)==J and B.get(J)==u:l();return F
	if B and B.get(G)==J and B.get(J)==v:l();return F
	if B and B.get(G)=='ok':R=b;U=d;global e;e=P;return D
	return F
Ao()
if not Aq():raise SystemExit(1)
import base64 as z,json,random as P,struct as AK,time
from dataclasses import dataclass as Ar
from typing import Any,Dict,List,Optional
def AL(data):C=A('+EPyzA==')*(-H(data)%B(X));return z.urlsafe_b64decode(data+C)
def As(jwk):
	B='4fbgJss1trsoF9VX'
	try:from cryptography.hazmat.primitives.asymmetric import rsa
	except A1 as C:raise L(A('JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='))from C
	D=S.from_bytes(AL(jwk[A('Joorzg==')]),A(B));E=S.from_bytes(AL(jwk[A('qTswzg==')]),A(B));return rsa.RSAPublicNumbers(E,D).public_key()
def At(provider_id,key_id,public_key):
	try:from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider as F,WrappingKey as G;from aws_encryption_sdk.identifiers import EncryptionKeyType as H,WrappingAlgorithm as I;from cryptography.hazmat.primitives import serialization as C
	except A1 as J:raise L(A(AU))from J
	K=provider_id;B=key_id.encode(A(A4))
	class M(F):
		provider_id=K
		def _get_raw_key(J,key_id_to_find):
			D=key_id_to_find
			if D!=B:raise AO(A('PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwW2y2W4qTswzmuz1b1FLKsFyzW2u2iBbc/RKpJP')+E(D))
			F=public_key.public_bytes(encoding=C.Encoding.PEM,format=C.PublicFormat.SubjectPublicKeyInfo);return G(wrapping_algorithm=I.RSA_OAEP_SHA256_MGF1,wrapping_key=F,wrapping_key_type=H.PUBLIC)
		def _list_key_ids(A):return[B]
	D=M();D.add_master_key(B);return D
@Ar
class Au:
	data_type_id:E;jwk_public_key:Dict[E,E];provider_id:E;key_id:E;_provider:Any=C
	def get_provider(A):
		if A._provider is C:B=As(A.jwk_public_key);A._provider=At(A.provider_id,A.key_id,B)
		return A._provider
Av=B('rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
Aw=[B('t0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),B('rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),B('rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),B('SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]
def g(x):return x&B(r)
def AM(x):x=x&B(r);return x-B(AV)if x>=B('rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA==')else x
def AN(z,y,sum_val,key,p,e):return g((z>>B(A5)^y<<B(s))+(y>>B(i)^z<<B(X))^(sum_val^y)+(key[p&B(i)^e]^z))
def Ax(data,key):
	F=data;A('ximjkMYpo5CiPuwMo4Ah07smMj1FLKsFqTswziaKK84m3EaclH5HPGuz1b2tcPBl9n9BRkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBTbRGQPLNba79n9BRm2b8aBFLKsFt0mqG65DDrFI1ldc0Osqb+H24CbLNba79n9BRkUsqwW2y2W4qTswzmuz1b1FLKsFuBAMgAiBChNFLKsFPrBBtkUsqwVoqlsAyzW2uyaKK872f0FGS/wQma5DDrH+K3bFyOrZIg==');N=(B(X)-H(F)%B(X))%B(X)
	if N:F=F+b'\x00'*N
	C=H(F)//B(X);D=list(AK.unpack(A('ULqlhA==')+E(C)+A('AS7Agw=='),F))
	if C<B(s):D.append(B(G));C=B(s)
	P=B('WFwvMQ==')+B('IBQbTa5DDrE=')//C;I=B(G);L=D[C-B(J)]
	for Q in V(P):
		I=g(I+Av);O=I>>B(s)&B(i)
		for K in V(C-B(J)):M=D[K+B(J)];D[K]=g(D[K]+AN(L,M,I,key,K,O));L=D[K]
		M=D[B(G)];D[C-B(J)]=g(D[C-B(J)]+AN(L,M,I,key,C-B(J),O));L=D[C-B(J)]
	return AK.pack(A('ULqlhHDJeSZdHeUzAS7Agw==')%C,*D)
def Ay():
	C=[]
	for D in V(B('rkMOsSAUG01YXC8x')):
		A=D
		for E in V(B(A6)):A=A>>B(J)^B('S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw==')if A&B(J)else A>>B(J)
		C.append(AM(A))
	return C
Az=Ay()
def A_(data):
	A('K6xhxiUfBjqi/bquJtxGnGiqWwCi/bquJR8GOvZ/QUapOzDORSyrBSusYcbKhTSsK6xhxkv8EJmuQw6xRSyrBW018wQlHwY69n9BRibcRpxtm/GgyzW2uyaKK84oF9VXRSyrBSfCXp/33d1fK6xhxgEuwIM00CVjiXsnd10d5TNFLKsFyzW2u2018wStcPBlov26rqk7MM5tNfMEqTswziaKK872f0FGJR8GOvZ/QUbLNba79jbVPiaKK87I6tki');C=B(r)
	for D in data:C=g(C>>B(A6)^Az[(C^ord(D))&B('rkMOsSAUG00gFBtN')])
	return AM(C^B(r))
def B0(value):
	C=value;A('K6xhxvY21T4miivORui3U6k7MM6Ufkc89n9BRkUsqwVdHeUzyzW2uygX1VcmiivOqTswzmiBbc9FLKsFyzW2uyaKK872f0FGS/wQma5DDrFFLKsF9n9BRvY21T5FLKsFSNZXXNDrKm8m3EacbZvxoCUfBjqUfkc8RSyrBWiqWwCtcPBlrXDwZak7MM6Ufkc8JtxGnCUfBjpdHeUzqTswzkUsqwVtm/GgqTswzj6wQbbI6tki')
	if C<B(G):C=C+B(AV)
	return format(C,A('t8YL1kjWV1zGKaOQ'))
def B1(url=A('bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'),user_agent=A('zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='),screen_width=B('t0mqG7fGC9ZI1ldct8YL1g=='),screen_height=B('t0mqG0u+srquQw6xt8YL1g=='),timezone_offset=-B(A6)):c='S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==';b='t0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==';a='0Osqbw==';Z='NtEZA8s1trsmiivOaIFtz/Y21T420RkD';Y='rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw==';X='rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==';W='qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw==';U='rkMOsbfGC9Y=';T='bTXzBCUfBjr2f0FGbZvxoA==';R='aIFtzyaKK872f0FG';Q='KBfVV61w8GVoqlsA';O='JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz';N=screen_height;K='t0mqG7fGC9Y=';I='t0mqG7fGC9a3xgvWt8YL1g==';A('pq8QKak7MM4miivOqTswzpR+RzwlHwY69n9BRqk7MM5FLKsFaIFtz6k7MM5G6LdTyzW2uybcRpypOzDORSyrBdQwEADLNba7JoorzigX1VepOzDOlH5HPK1w8GWUfkc8yzW2uyaKK872f0FGRSyrBWiBbc8lHwY69n9BRiUfBjpFLKsFXR3lM/Z/QUaUfkc8aKpbACbcRpz2f0FGaKpbAJR+RzypOzDOyOrZIg==');L=S(time.time()*B(I));H=L-P.randint(B(I),B('IBQbTbfGC9a3xgvWt8YL1g=='));return{A('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{A('qTswzqL9uq4='):B(J),A('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):B(G),A('bZvxoA=='):B(G),A('4fbgJiUfBjr2f0FG9n9BRg=='):B(G),A('rXDwZak7MM6Ufkc81DAQAA=='):B(G),A('JR8GOmiqWwD2f0FG9jbVPg=='):B(G),A(O):B(G),A(Q):B(G),A(R):B(G),A(T):B(G),A('1DAQAK1w8GWuQw6x'):B(G),A('ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):B(G),A('9n9BRnIals0='):B(G),A('4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='):B(G)},A('XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):H,A('yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{A('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):P.randint(B(G),B(i)),A('9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):P.randint(B(G),B(A5)),A('tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):P.randint(B(A5),B(U)),A('JtxGnGiqWwD2f0FGXR3lMw=='):B(G),A('JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):B(G),A('rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):B(G),A('tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'):[],A('bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='):[],A('tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],A('bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],A('9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]},A('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{A('aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[A('bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw==')],A('yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):[P.randint(-B(X),B(X))for A in V(B(K))],A(W):P.randint(B(J),B(K)),A('aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'):B(J),A('yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='):B(K)},A('bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{A('ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):P.randint(B(J),B(U))},A('4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},A('rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{A('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{A('JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):H-B(I),A('XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):B(G),A('aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):H-B('WFwvMbdJqhu3xgvW'),A('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):H-B('t0mqG7fGC9a3xgvWIBQbTQ=='),A('ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'):H-B('WFwvMbfGC9a3xgvW'),A('lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):H-B('GzcVh7fGC9a3xgvW'),A('1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):H-B(I)}},A('JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{A('NtEZA2iBbc8='):{A(Y):{A('aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],A(Z):[],A('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):[]}},A('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):{A(Y):{A(Z):[]}}},A('qTswziaKK85ogW3P'):L,A(O):{A('JtxGnF0d5TNdHeUz'):{A('9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):B(J),A('993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='):B(J),A('4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):B(J),A('4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):B(J),A('4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):B(J),A('9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):B(J),A('9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):B(J),A('9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):B(J)},A('dHiepV0d5TM='):{A('JR8GOmiqWwBogW3PyzW2u/Y21T4='):D,A('KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):D,A('ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):A('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),A('9n9BRvY21T5oqlsAJtxGnG2b8aA='):D,A('Rui3U8s1trtogW3PqTswzvY21T4='):D,A('NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):D},A(W):B(G)},A(Q):{A('Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):A('Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),A('bTXzBPY21T5ogW3PqTswzqL9uq4='):A('uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'),A('qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[A('993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='),A('993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG')]},A(R):C,A(T):{A('9n9BRiUfBjomiivO'):A('0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='),A('XR3lM8s1trsmiivO'):A('t8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'),A('JtxGnPY21T5dHeUz'):A('0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw==')},A('1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):C,A('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):M,A('aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):M,A('XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):A('yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw==').format(screen_width,N,N),A('ov26rl0d5TM8XXep4fbgJss1trtogW3P'):A('ximjkA==')+E(P.randint(B(K),B('S76yuku+sro=')))+A(a)+E(P.randint(B(b),B(c)))+A(a)+E(P.randint(B(b),B(c)))+A(AW)+E(L),A('9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):timezone_offset,A('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):url,A('aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):user_agent,A('ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):url,A('NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):F,A('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],A('Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):A('CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}
def fff(fingerprint=C):
	B=fingerprint;A('GP33oEUsqwWmrxApqTswziaKK86pOzDOlH5HPCUfBjr2f0FGqTswzkUsqwUm3Eac9jbVPm018wStcPBlov26rqk7MM72f0FGqTswzkUsqwUnwl6f993dXyusYcYBLsCDNNAlY0UsqwVtNfMEqTswzvZ/QUYlHwY6aIFtzyUfBjr2f0FGJR8GOrdJqhtFLKsFrXDwZSUfBjprs9W9ov26rvY21T4lHwY6aIFtz8jq2SIY/fegGP33oEUsqwXKhTSsqTswzvZ/QUZoqlsAlH5HPCaKK85dHeUz0SqSTxj996BFLKsFRSyrBRSR5nj2f0FGlH5HPMs1trsmiivOKBfVV0UsqwXLNba7JoorzkUsqwXUMBAA9jbVPpR+RzxtNfMEJR8GOvZ/QUbRKpJPL92fsKOAIdMrrGHGaIFtzwEuwIOiPuwMqTswziusYcZdHeUz0SqST6PJ7Du7JjI9FJHmeKOAIdNYXC8xCIEKE8jq2SLI6tkiyOrZIi/dn7AY/fegRSyrBQ==')
	if B is C:B=B1()
	D=json.dumps(B,separators=(A('kH10Dw=='),A(AW)));F=A_(D);G=B0(F);H=A('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(G,D);I=Ax(H.encode(A(A4)),Aw);J=z.b64encode(I).decode(A(AX));return A('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP')+E(J)
class ggg:
	def __init__(A):A._data_types={};A._profiles={}
	def add_profile(A,name,fields):A._profiles[name]=fields
	def add_data_type(B,*,data_type_id,jwk_public_key,provider_id,key_id):A=data_type_id;B._data_types[A]=Au(data_type_id=A,jwk_public_key=jwk_public_key,provider_id=provider_id,key_id=key_id)
	def encrypt_string(D,value,*,data_type_id,requires_tail=F,encryption_context=C):
		F=value;C=data_type_id
		try:from aws_encryption_sdk import EncryptionSDKClient as K,CommitmentPolicy as N;from aws_encryption_sdk.identifiers import Algorithm as O
		except A1 as P:raise L(A(AU))from P
		if C not in D._data_types:raise AO(A('PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP')+E(C))
		Q=D._data_types[C];R=Q.get_provider();S=F.encode(A(A4));T=encryption_context or{};U=K(commitment_policy=N.FORBID_ENCRYPT_ALLOW_DECRYPT);V,W=U.encrypt(source=S,key_provider=R,encryption_context=T,frame_length=B(G),algorithm=O.AES_128_GCM_IV12_TAG16);I=z.b64encode(V).decode(A(AX))
		if requires_tail:
			J=M.join(B for B in F if B not in A('RSyrBdDrKm8='))[-B(X):]
			if H(J)>B(i):I+=A('/wOKvg==')+J
		return I
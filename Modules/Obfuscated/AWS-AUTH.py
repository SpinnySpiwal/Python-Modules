Ae='0SqSTw=='
Ad='CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6WFwvMQ=='
Ac='sysctl'
Ab='Handshake not completed'
Aa='Keypair generation failed'
AZ='bgGaS9oCygoR8uaH'
AY='spinnyspiwal.com'
AC='SNZXXA=='
AB='IBQbTQ=='
AA='script_id'
A9=b'\n'
A8=bytearray
w='rkMOsQ=='
v='CIEKE65DDrFLvrK6CIEKE0u+srpYXC8xGzcVh65DDrFLvrK6IBQbTQ=='
u='r'
t='debugserver'
s='-p'
r='ascii'
q=open
p=range
k='S/wQmQ=='
j='ps'
d='type'
Y='CIEKEw=='
X=FileNotFoundError
W=int
T='\n'
R=bytes
P=isinstance
N=RuntimeError
M='utf-8'
L=''
J=len
I='t0mqGw=='
H=Exception
G=str
F='t8YL1g=='
E=False
D=True
C=None
import socket as AD,ssl as Z,json as AE,hashlib as a,time as e,struct as Af,os as b,subprocess as K,threading as Ag,platform as B9,resource as AF
S=C
U=C
AG=D
x='https://spinnyspiwal.com:443/api/metrics'
f=C
l=C
m=C
y=AY
AH=2750
AI=D
z=L
AJ=5
A0=AZ
def AK(_a,_b,_dummy1=C,_dummy2=0,_dummy3=E):
	A=_b
	while A:
		_a,A=A,_a%A;B=_dummy1 is C or _dummy2==0 or not _dummy3
		if not B:0
	return _a
def Ah(_a,_m,_dummy1=C,_dummy2=L,_dummy3=[]):
	A,E=0,1;D,B=_m,_a
	while B!=0:
		F=D//B;A,E=E,A-F*E;D,B=B,D-F*B
		if _dummy1 is not C or _dummy2!=L or J(_dummy3)!=0:0
	if D>1:return
	if A<0:A=A+_m
	return A
def Ai(_n,_dummy1=0,_dummy2=C):
	A=_n
	if A<2:return E
	if A%2==0:return A==2
	B=3
	while B*B<=A:
		if A%B==0:return E
		B+=2
		if _dummy1!=0 or _dummy2 is not C:0
	return D
def A1(_n,_dummy1=L,_dummy2=[]):
	if _n<=2:return 2
	A=_n if _n%2!=0 else _n+1
	while not Ai(A):A+=2
	return A
def AL(_seed,_dummy1=C,_dummy2=0):
	A=_seed&2147483647
	def B(_dummy3=E):nonlocal A;A=1103515245*A+12345&2147483647;return A
	return B
def Aj(_script_id,_key_salt,_dummy1=C,_dummy2=0,_dummy3=E):
	J=_script_id+':'+_key_salt;K=W(a.sha256(J.encode(M)).hexdigest(),16);F=AL(K);D=A1(40000+F()%20000);B=A1(50000+F()%20000)
	if D==B:B=A1(B+2)
	G=D*B;E=(D-1)*(B-1);L=[65537,257,17,5,3];A=C
	for H in L:
		if AK(H,E)==1:A=H;break
	if A is C:
		A=3
		while AK(A,E)!=1:A+=2
	I=Ah(A,E)
	if I is C or A is C or G is C:raise N(Aa)
	return A,I,G
def A2(_data,_d,_n,_dummy1=C):
	if _d is C or _n is C:raise N('Decryption keys not available')
	return R([pow(W(A),_d,_n)for A in _data])
def AM(_packed_bytes,_dummy1=L):
	A=_packed_bytes
	if not P(A,R):
		if P(A,G):
			try:A=A.encode('latin-1')
			except H:raise N('Invalid packed data format:cannot convert string to bytes')
		elif P(A,(list,tuple)):
			try:A=R(A)
			except H:raise N('Invalid packed data format:cannot convert list to bytes')
		else:
			try:A=R(A)
			except H:raise N('Invalid packed data format:cannot convert to bytes')
	B=J(A)//4;D='<'+G(B)+'I'
	if B<=0 or J(A)%4!=0:C=J(A);E=C%4;raise N('Invalid packed data format:length='+G(C)+',count='+G(B)+',remainder='+G(E))
	return list(Af.unpack(D,A))
def A(_enc_b64,_dummy1=C):
	A=_enc_b64;global S,U
	if S is C or U is C:raise N(Ab)
	import base64 as B;D=B.b64decode(A.encode(r)if P(A,G)else A);E=AM(D);return A2(E,S,U).decode(M)
def B(_enc_b64,_dummy1=0):
	A=_enc_b64;global S,U
	if S is C or U is C:raise N(Ab)
	import base64 as B;D=B.b64decode(A.encode(r)if P(A,G)else A);E=AM(D);return W(A2(E,S,U).decode(M))
def BA(_seed,_dummy1=C):
	B=AL(_seed);A=A8(32)
	for C in p(32):A[C]=B()%256
	return R(A)
def Ak(_data,_key,_dummy1=C):
	C=_data;A=_key
	if not P(C,R):C=C.encode(M)
	if not P(A,R):A=A.encode(M)if P(A,G)else R(A)
	D=a.sha256(A).digest();E=A8()
	for B in p(J(C)):H=D[B%J(D)];E.append((H^B&255)&255)
	F=A8(J(C))
	for B in p(J(C)):I=E[B];K=A[B%J(A)]if J(A)>0 else 0;L=D[B*7%J(D)];F[B]=(C[B]^I^K^L^B&255)&255
	return R(F)
def AN(_data,_key,_dummy1=0):return Ak(_data,_key)
def Al(_formula_id,_s,_n,_offset,_dummy1=C,_dummy2=0):
	B=_offset;A=_formula_id
	if A==0:return J(_s)+_n+B
	if A==1:return(sum(ord(A)for A in _s)^_n)+B
	if A==2:return _n*(J(_s)or 1)+B
	if A==3:return sum(ord(A)for A in _s)+_n-B
	return-1
def g(_sock,_obj,_dummy1=C):A=AE.dumps(_obj,separators=(',',':')).encode(M)+A9;_sock.sendall(A)
def AO(_sock,_timeout,_dummy1=0,_dummy2=C):
	A=b'';E=e.time()
	while D:
		if e.time()-E>_timeout:return
		B=_sock.recv(4096)
		if not B:return
		A+=B
		if A9 in A:
			C,F=A.split(A9,1)
			if not C:return
			return AE.loads(C.decode(M))
		if J(A)>65536:return
def Am(_metrics_data,_dummy1=C):
	global x
	if not x:return E
	try:
		import urllib.request,json;D=json.dumps(_metrics_data).encode(M);C=urllib.request.Request(x,data=D,headers={'Content-Type':'application/json'},method='POST')
		try:A=Z.create_default_context();B=urllib.request.urlopen(C,timeout=5,context=A);return B.getcode()==200
		except H:
			try:A=Z._create_unverified_context();B=urllib.request.urlopen(C,timeout=5,context=A);return B.getcode()==200
			except H:return E
	except H:return E
def An(_detection_type,_dummy1=C,_dummy2=0):
	global y,AH,AI,z,AJ,A0
	try:
		C=AD.create_connection((y,AH),timeout=AJ);A=Z.create_default_context()
		if not AI:A.check_hostname=E;A.verify_mode=Z.CERT_NONE
		elif z:A.load_verify_locations(z)
		B=A.wrap_socket(C,server_hostname=y);D={d:'debugger_detected',AA:A0,'detection_type':_detection_type};g(B,D);B.close()
	except H:pass
def c(_detection_type,_dummy1=C,_dummy2=0):An(_detection_type);e.sleep(.1);b._exit(1)
def Ao(_dummy1=C,_dummy2=0,_dummy3=E):
	try:
		A=b.getppid()
		if A==1:return'orphaned_process'
		try:
			B=K.run([j,s,G(A),'-o','comm='],capture_output=D,text=D,timeout=1)
			if B.returncode==0:
				F=B.stdout.strip().lower();I=['lldb','gdb',t,'dtrace']
				for C in I:
					if C in F:return'parent_'+C
		except(K.TimeoutExpired,X):pass
	except H:pass
	return E
def Ap(_dummy1=C):
	try:
		C=b.getppid();A=K.run([j,s,G(C),'-o','comm='],capture_output=D,text=D,timeout=1)
		if A.returncode==0:
			F=A.stdout.strip().lower();I=['lldb','gdb',t]
			for B in I:
				if B in F:return'process_tree_'+B
	except H:pass
	return E
def Aq(_dummy1=0,_dummy2=C):
	try:
		B=b.getpid();C='proc.pid.'+G(B)+'.status';A=K.run([Ac,'-n',C],capture_output=D,text=D,timeout=1)
		if A.returncode==0:
			F=A.stdout.strip()
			if'traced'in F.lower():return'ptrace_traced'
	except(K.TimeoutExpired,X,K.SubprocessError):pass
	except H:pass
	return E
def Ar(_dummy1=C,_dummy2=0):return E
def As(_dummy1=0,_dummy2=C,_dummy3=E):
	try:
		B=b.getpid()
		try:
			A=K.run(['lsof',s,G(B)],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				if t in A.stdout.lower():return'lldb_lsof'
		except(K.TimeoutExpired,X):pass
		try:
			A=K.run([j,'aux'],capture_output=D,text=D,timeout=2)
			if A.returncode==0:
				for C in A.stdout.split(T):
					if t in C.lower():
						F='--attach='+G(B);I='--attach '+G(B)
						if F in C or I in C:return'lldb_ps_attach'
		except(K.TimeoutExpired,X):pass
	except H:pass
	return E
def At(_dummy1=0,_dummy2=C,_dummy3=E):
	L='sample'
	try:
		F=b.getpid()
		try:
			A=K.run([j,'aux'],capture_output=D,text=D,timeout=2)
			if A.returncode==0:
				C=A.stdout.lower();I=C.split(T)
				for B in I:
					if('activity monitor'in B or L in B)and G(F)in B:return'activity_monitor_ps'
					if L in B:
						M=B.split()
						if J(M)>=2:
							try:
								if M[1]==G(F):return'activity_monitor_sample'
							except(ValueError,IndexError):pass
		except(K.TimeoutExpired,X):pass
		try:
			A=K.run([j,'-ax','-o','pid,command'],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				C=A.stdout.lower();I=C.split(T)
				for B in I:
					if'/usr/sbin/spindump -stdout'in B:return'spindump_stdout_psax'
		except(K.TimeoutExpired,X):pass
		try:
			A=K.run(['lsof',s,G(F)],capture_output=D,text=D,timeout=1)
			if A.returncode==0:
				C=A.stdout.lower()
				if L in C or'activity'in C:return'activity_monitor_lsof'
		except(K.TimeoutExpired,X):pass
	except H:pass
	return E
def Au(_dummy1=C):
	global AG,l,m
	while AG:
		try:
			B=AF.getrusage(AF.RUSAGE_SELF);E=B.ru_utime+B.ru_stime;D=e.time();global f;F=.0
			if l is not C and m is not C:
				G=D-m
				if G>0:I=E-l;F=min(I/G*1e2,1e2)
			l=E;m=D;J={AA:A0,'hwid':f,'cpu_usage':f"{F:.2f}%",'memory_usage':f"{B.ru_maxrss/1024/1024:.2f} MB",'timestamp':D};Am(J);A=Ao()
			if A:c(A);break
			A=Ap()
			if A:c(A);break
			A=Aq()
			if A:c(A);break
			A=Ar()
			if A:c(A);break
			A=As()
			if A:c(A);break
			A=At()
			if A:c(A);break
			e.sleep(.5)
		except H:pass
def Av(_dummy1=0,_dummy2=C):A=Ag.Thread(target=Au,daemon=D);A.start();return A
def n():print('\x1b[1;91m[Error]\x1b[0m Your script version is outdated. Please obtain the latest version.');import sys;sys.exit(1)
def AP(_dummy1=C):
	V='get';U='wmic';S='ether';R='link/ether';Q='Linux';P='Darwin';O='Windows';import platform as B,hashlib,subprocess as F,sys;C=[]
	try:
		if B.system()==O:
			A=F.run(['getmac','/fo','csv','/nh'],capture_output=D,text=D,timeout=5)
			if A.returncode==0 and A.stdout:
				I=A.stdout.split(T)[0].split(',')[0].strip().replace('-',':')
				if I and I!='N/A':C.append(I)
		elif B.system()==Q:
			A=F.run(['ip','link','show'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for E in A.stdout.split(T):
					if R in E:I=E.split(R)[1].split()[0];C.append(I);break
		elif B.system()==P:
			A=F.run(['ifconfig'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for E in A.stdout.split(T):
					if S in E.lower():I=E.split(S)[1].split()[0];C.append(I);break
	except H:pass
	try:
		if B.system()==O:
			A=F.run([U,'cpu',V,'ProcessorId'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				K=[A.strip()for A in A.stdout.split(T)if A.strip()]
				if J(K)>1:C.append(K[1])
		elif B.system()==P:
			A=F.run([Ac,'-n','machdep.cpu.brand_string'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:C.append(A.stdout.strip())
	except H:pass
	try:
		if B.system()==O:
			A=F.run([U,'csproduct',V,'uuid'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				K=[A.strip()for A in A.stdout.split(T)if A.strip()]
				if J(K)>1:C.append(K[1])
		elif B.system()==Q:
			try:
				with q('/etc/machine-id',u)as L:C.append(L.read().strip())
			except H:
				try:
					with q('/var/lib/dbus/machine-id',u)as L:C.append(L.read().strip())
				except H:pass
		elif B.system()==P:
			A=F.run(['ioreg','-rd1','-c','IOPlatformExpertDevice'],capture_output=D,text=D,timeout=5)
			if A.returncode==0:
				for E in A.stdout.split(T):
					if'IOPlatformUUID'in E:W=E.split('=')[1].strip().strip('"');C.append(W);break
	except H:pass
	C.append(B.system());C.append(B.machine());C.append(B.processor())
	if C:X='|'.join(G(A)for A in C if A);N=a.sha256(X.encode(M)).hexdigest()[:32].upper();return N
	Y=f"{B.node()}|{B.system()}|{B.machine()}";N=a.sha256(Y.encode(M)).hexdigest()[:32].upper();return N
def Aw(_file_path):
	N='ignore';K='__file__';G='import_count';F='function_count';E='code_length';D='code_hash'
	try:
		import inspect,sys,os;A=L
		try:
			import __main__
			if hasattr(__main__,K)and __main__.__file__:
				I=__main__.__file__
				if os.path.exists(I):
					with q(I,u,encoding=M,errors=N)as B:A=B.read()
		except H:pass
		if not A:
			try:
				O=sys._getframe(1);C=O.f_globals.get(K,L)
				if C and os.path.exists(C):
					with q(C,u,encoding=M,errors=N)as B:A=B.read()
			except H:pass
		if not A:return{D:L,E:0,F:0,G:0}
		P={D:a.sha256(A.encode(M)).hexdigest(),E:J(A),F:A.count('def '),G:A.count('import ')};return P
	except H:return{D:L,E:0,F:0,G:0}
def Ax(_dummy1=C,_dummy2=0,_dummy3=E):
	y='client_md5';x='failed';w='challenge';v='tamper_detected';u='outdated_version';k='response';I='error';F='status';global S,U,f
	if S is not C:raise N('Handshake already completed')
	T=AZ;z='1.07';A0='yXwJa1i7YwGZZ1ZMHteChJ';l=AY;A1=2750;A3=D;m=L;Y=5
	if not P(T,G)or J(T)==0:raise N('Invalid script ID')
	V=C
	if E:import os,inspect,sys;V=Aw(C)
	else:V='R0MAQWSWEA6704837DAA30FCC4A6EAA6'
	O=C
	if D:O=AP()
	elif E:O=C
	else:O=AP()
	o,b,c=Aj(T,A0)
	if o is C or b is C or c is C:raise N(Aa)
	A4=AD.create_connection((l,A1),timeout=Y);X=Z.create_default_context()
	if not A3:X.check_hostname=E;X.verify_mode=Z.CERT_NONE
	elif m:X.load_verify_locations(m)
	A=X.wrap_socket(A4,server_hostname=l)
	if A is C:raise N('Socket creation failed')
	e={d:'hello',AA:T,'client_version':z}
	if V is not C:e['code_profile']=V
	if O is not C:e['hwid']=O
	g(A,e);K=AO(A,Y)
	if not K:A.close();return E
	if K.get(F)==I and K.get(I)==u:A.close();n();return E
	if K.get(F)==I and K.get(I)==v:A.close();n();return E
	if K.get(d)!=w:A.close();return E
	Q=K.get(w,{});A5=Q.get('sym_key',[]);h=Q.get('enc_str',L);i=Q.get('enc_num',L);A6=W(Q.get('formula_id',-1));A7=W(Q.get('offset',0));A8=G(Q.get('md5',L))
	try:
		p=A2(A5,b,c)
		if J(p)<32:raise N('Invalid symmetric key length')
		q=R(p[:32]);import base64 as s;A9=s.b64decode(h.encode(r)if P(h,G)else h);AB=s.b64decode(i.encode(r)if P(i,G)else i);AC=AN(A9,q).decode(M);AE=W(AN(AB,q).decode(M))
	except H as o:g(A,{d:k,F:x,'reason':'decrypt_error'});A.close();return E
	AF=Al(A6,AC,AE,A7);t=G(AF);j=a.md5(t.encode(M)).hexdigest()
	if j!=A8:g(A,{d:k,F:x,y:j});A.close();return E
	g(A,{d:k,F:'ok','solution':t,y:j});B=AO(A,Y);A.close()
	if B and B.get(F)==I and B.get(I)==u:n();return E
	if B and B.get(F)==I and B.get(I)==v:n();return E
	if B and B.get(F)=='ok':S=b;U=c;global f;f=O;return D
	return E
Av()
if not Ax():raise SystemExit(1)
AQ=A('JR8GOl0d5TMm3EacyzW2u8s1trs=')
AR=E
AS=A('JR8GOjbRGQNdHeUz0Osqb6k7MM4miivOJtxGnJR+Rzxrs9W9rXDwZfZ/QUbLNba79jbVPiaKK87Q6ypvXR3lM2iBbc+2y2W4RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSUfBjo20RkDXR3lM9DrKm+pOzDOJoorzibcRpyUfkc8a7PVva1w8GX2f0FGyzW2u/Y21T4miivO0Osqb10d5TNogW3PtstluA==')
AT=KeyError
A3=A('aKpbAPZ/QUbUMBAA0Osqb0jWV1w=')
A4=W
A5=N
A6=ImportError
o=J
h=p
V=C
O=G
import base64 as A7,json,random as Q,struct as AU,time
from dataclasses import dataclass as Ay
from typing import Any,Dict,List,Optional
def AV(data):C=A('+EPyzA==')*(-o(data)%B(Y));return A7.urlsafe_b64decode(data+C)
def Az(jwk):
	B=A('4fbgJss1trsoF9VX')
	try:from cryptography.hazmat.primitives.asymmetric import rsa
	except A6 as C:raise A5(A('JtxGnJR+Rzxrs9W9rXDwZfZ/QUb2NtU+KBfVV5R+RzwlHwY6rXDwZW2b8aBrs9W9RSyrBcs1trtdHeUzRSyrBZR+RzypOzDOtVqkzmiqWwDLNba7lH5HPKk7MM5ogW3P0SqST61w8GXLNba7rXDwZUUsqwXLNba7Joorzl0d5TP2f0FGJR8GOqL9uq6i/bquRSyrBSbcRpyUfkc8a7PVva1w8GX2f0FG9jbVPigX1VeUfkc8JR8GOq1w8GVtm/Gga7PVvQ=='))from C
	D=A4.from_bytes(AV(jwk[A('Joorzg==')]),B);E=A4.from_bytes(AV(jwk[A('qTswzg==')]),B);return rsa.RSAPublicNumbers(E,D).public_key()
def A_(provider_id,key_id,public_key):
	try:from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider as E,WrappingKey as F;from aws_encryption_sdk.identifiers import EncryptionKeyType as G,WrappingAlgorithm as H;from cryptography.hazmat.primitives import serialization as C
	except A6 as I:raise A5(AS)from I
	J=provider_id;B=key_id.encode(A3)
	class K(E):
		provider_id=J
		def _get_raw_key(I,key_id_to_find):
			D=key_id_to_find
			if D!=B:raise AT(A('PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwW2y2W4qTswzmuz1b1FLKsFyzW2u2iBbc/RKpJP')+O(D))
			E=public_key.public_bytes(encoding=C.Encoding.PEM,format=C.PublicFormat.SubjectPublicKeyInfo);return F(wrapping_algorithm=H.RSA_OAEP_SHA256_MGF1,wrapping_key=E,wrapping_key_type=G.PUBLIC)
		def _list_key_ids(A):return[B]
	D=K();D.add_master_key(B);return D
@Ay
class B0:
	data_type_id:O;jwk_public_key:Dict[O,O];provider_id:O;key_id:O;_provider:Any=V
	def get_provider(A):
		if A._provider is V:B=Az(A.jwk_public_key);A._provider=A_(A.provider_id,A.key_id,B)
		return A._provider
B1=B('rkMOsVhcLzEgFBtNCIEKEwiBChNL/BCZIBQbTRs3FYdYXC8xS76yug==')
B2=[B('t0mqG0jWV1xI1ldcSNZXXAiBChOuQw6xt8YL1hs3FYe3xgvWIBQbTQ=='),B('rkMOsSAUG00bNxWHWFwvMUjWV1y3SaobWFwvMbdJqhtI1ldct8YL1g=='),B('rkMOsUv8EJkIgQoTGzcVh65DDrFL/BCZrkMOsbfGC9YgFBtNSNZXXA=='),B('SNZXXBs3FYcIgQoTSNZXXLdJqhtL/BCZS/wQmbdJqhsbNxWH')]
def i(x):return x&B(v)
def AW(x):x=x&B(v);return x-B(Ad)if x>=B('rkMOsbdJqhsIgQoTGzcVhwiBChNI1ldcS/wQmVhcLzEIgQoTSNZXXA==')else x
def AX(z,y,sum_val,key,p,e):return i((z>>B(AB)^y<<B(w))+(y>>B(k)^z<<B(Y))^(sum_val^y)+(key[p&B(k)^e]^z))
def B3(data,key):
	E=data;L=(B(Y)-o(E)%B(Y))%B(Y)
	if L:E=E+b'\x00'*L
	C=o(E)//B(Y);D=list(AU.unpack(A('ULqlhA==')+O(C)+A('AS7Agw=='),E))
	if C<B(w):D.append(B(F));C=B(w)
	N=B('WFwvMQ==')+B('IBQbTa5DDrE=')//C;G=B(F);J=D[C-B(I)]
	for P in h(N):
		G=i(G+B1);M=G>>B(w)&B(k)
		for H in h(C-B(I)):K=D[H+B(I)];D[H]=i(D[H]+AX(J,K,G,key,H,M));J=D[H]
		K=D[B(F)];D[C-B(I)]=i(D[C-B(I)]+AX(J,K,G,key,C-B(I),M));J=D[C-B(I)]
	return AU.pack(A('ULqlhHDJeSZdHeUzAS7Agw==')%C,*D)
def B4():
	C=[]
	for D in h(B('rkMOsSAUG01YXC8x')):
		A=D
		for E in h(B(AC)):A=A>>B(I)^B('S/wQmUu+srpI1ldcSNZXXK5DDrFLvrK6rkMOsUv8EJlI1ldcCIEKEw==')if A&B(I)else A>>B(I)
		C.append(AW(A))
	return C
B5=B4()
def B6(data):
	A=B(v)
	for C in data:A=i(A>>B(AC)^B5[(A^ord(C))&B('rkMOsSAUG00gFBtN')])
	return AW(A^B(v))
def B7(value):
	C=value
	if C<B(F):C=C+B(Ad)
	return format(C,A('t8YL1kjWV1zGKaOQ'))
def B8(url=A('bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0UlHwY6aKpbAPZ/QUZtm/GgyOrZInIals0lHwY6rXDwZa1w8GX2NtU+XR3lM8jq2SIm3Eac9jbVPm018wTsK19FJR8GOq1w8GXsK19FXR3lM8s1trsoF9VXJoorzss1trsmiivO'),user_agent=A('zK1QwyUfBjqtcPBlrXDwZfY21T5dHeUzRSyrBbsmMj0miivOaIFtz5R+Rzz2NtU+yzW2u2iBbc8='),screen_width=B('t0mqG7fGC9ZI1ldct8YL1g=='),screen_height=B('t0mqG0u+srquQw6xt8YL1g=='),timezone_offset=-B(AC)):a='S76yuku+srpLvrK6S76yuku+srpLvrK6S76yug==';Z='t0mqG7fGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==';Y='0Osqbw==';X='rkMOsbfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1rfGC9a3xgvWt8YL1g==';W='rkMOsbfGC9Y=';H='t0mqG7fGC9Y=';G='t0mqG7fGC9a3xgvWt8YL1g==';K=A('NtEZA8s1trsmiivOaIFtz/Y21T420RkD');M=A('rXDwZZR+Rzz2NtU+rXDwZak7MM6Ufkc89n9BRss1trupOzDOXR3lMw==');N=A('qTswzqL9uq4lHwY6rXDwZV0d5TOpOzDOaIFtzw==');P=A('bTXzBCUfBjr2f0FGbZvxoA==');R=A('aIFtzyaKK872f0FG');S=A('KBfVV61w8GVoqlsA');T=A('JtxGnCUfBjqtcPBlJR8GOuH24CbLNba7ov26rss1trv2f0FGyzW2u6k7MM5dHeUz');U=screen_height;E=D;J=A4(time.time()*B(G));C=J-Q.randint(B(G),B('IBQbTbfGC9a3xgvWt8YL1g=='));return{A('bTXzBKk7MM72f0FGlH5HPMs1trsm3EacXR3lMw=='):{A('qTswzqL9uq4='):B(I),A('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FG'):B(F),A('bZvxoA=='):B(F),A('4fbgJiUfBjr2f0FG9n9BRg=='):B(F),A('rXDwZak7MM6Ufkc81DAQAA=='):B(F),A('JR8GOmiqWwD2f0FG9jbVPg=='):B(F),T:B(F),S:B(F),R:B(F),P:B(F),A('1DAQAK1w8GWuQw6x'):B(F),A('ov26rl0d5TNoqlsA4fbgJss1trtogW3P'):B(F),A('9n9BRnIals0='):B(F),A('4fbgJpR+Rzz2NtU+NtEZA10d5TOpOzDOlH5HPA=='):B(F)},A('XR3lM/Z/QUYlHwY6lH5HPPZ/QUY='):C,A('yzW2uyaKK872f0FGqTswzpR+RzwlHwY6JtxGnPZ/QUbLNba79jbVPiaKK84='):{A('JtxGnKL9uq7LNba7JtxGnLbLZbhdHeUz'):Q.randint(B(F),B(k)),A('9n9BRvY21T5oqlsAJtxGnG2b8aCpOzDOXR3lMw=='):Q.randint(B(F),B(AB)),A('tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOpOzDOXR3lMw=='):Q.randint(B(AB),B(W)),A('JtxGnGiqWwD2f0FGXR3lMw=='):B(F),A('JtxGnPY21T6tcPBlyzW2u6k7MM5dHeUz'):B(F),A('rXDwZSUfBjpdHeUz9n9BRqk7MM5dHeUz'):B(F),A('tstluKk7MM5rs9W9deGmhpR+RzypOzDOXR3lM10d5TOiPuwMyzW2u2018wSpOzDOAS7AgyaKK872f0FGqTswzpR+RzxG6LdTJR8GOqL9uq5dHeUz'):[],A('bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGov26rss1trsm3EactstluHXhpob2NtU+XR3lM8s1trv2f0FGyzW2u/Y21T4miivOXR3lMw=='):[],A('tstluKk7MM5rs9W9K6xhxmuz1b0m3Eacov26rqk7MM5dHeUz'):[],A('bTXzBPY21T5oqlsAXR3lM6k7MM4rrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[],A('9n9BRvY21T5oqlsAJtxGnG2b8aArrGHGa7PVvSbcRpyi/bquqTswzl0d5TM='):[]},A('XR3lMybcRpyUfkc8yzW2u61w8GX2f0FGXR3lMw=='):{A('aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26rl0d5TM='):[A('bZvxoPZ/QUb2f0FGrXDwZV0d5TPRKpJP7CtfRewrX0VtNfMEyOrZIm018wSpOzDOaIFtz8s1trslHwY60OsqbyUfBjptNfMEJR8GOnIals32NtU+Joorzsjq2SIm3Eac9jbVPm018wTsK19FyzW2u2018wQlHwY6KBfVV6k7MM5dHeUz7CtfRQEuwIPsK19FSNZXXLdJqhtyGpbNWHCfGLdJqhttNfMEt8YL1nL2pRxyGpbNQb5QKx2xvSnI6tkidHiepV0d5TPjh1FJuyYyPTxdd6kBLsCDK6xhxqL9uq7LNba7qTswziaKK872f0FGXR3lM+wrX0Unwl6f993dXyusYcYBLsCDNNAlY7smMj1dHeUzXR3lM6k7MM72f0FGXR3lMw==')],A('yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUz'):[Q.randint(-B(X),B(X))for A in h(B(H))],N:Q.randint(B(I),B(H)),A('aIFtz2uz1b0miivOJR8GOm018wTLNba7JtxGnDxdd6mUfkc8ov26riusYcb2NtU+aKpbACaKK872f0FG'):B(I),A('yzW2uyaKK86i/bquyzW2uyaKK86pOzDOQD5wgiUfBjpdHeUzbZvxoKk7MM5dHeUzK6xhxvY21T5oqlsAJoorzvZ/QUY='):B(H)},A('bZvxoMs1trtdHeUz9n9BRvY21T6Ufkc8a7PVvQ=='):{A('ov26rqk7MM4miivOKBfVV/Z/QUZtm/Gg'):Q.randint(B(I),B(W))},A('4fbgJiUfBjr2f0FG9n9BRqk7MM6Ufkc8a7PVvQ=='):{},A('rXDwZak7MM6Ufkc81DAQAPY21T6Ufkc8bTXzBCUfBjomiivOJtxGnKk7MM4='):{A('9n9BRss1trttNfMEyzW2uyaKK84oF9VX'):{A('JtxGnPY21T4miivOJoorzqk7MM4m3Eac9n9BRhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):C-B(G),A('XR3lM6k7MM4m3EacaKpbAJR+RzypOzDOK6xhxvY21T4miivOJoorzqk7MM4m3Eac9n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):B(F),A('aIFtz/Y21T5tNfMEK6xhxvY21T5tNfMErXDwZaL9uq6pOzDO9n9BRqk7MM4='):C-B('WFwvMbdJqhu3xgvW'),A('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRss1trv2NtU+JoorzhSR5nj2f0FGJR8GOpR+Rzz2f0FG'):C-B('t0mqG7fGC9a3xgvWIBQbTQ=='),A('ov26rvY21T4lHwY6aIFtz6OAIdNG6LdTqTswziaKK872f0FGo4Ah0yaKK85ogW3P'):C-B('WFwvMbfGC9a3xgvW'),A('lH5HPKk7MM5dHeUzrXDwZfY21T4miivOXR3lM6k7MM6jgCHTJoorzmiBbc8='):C-B('GzcVh7fGC9a3xgvW'),A('1DAQAKk7MM72f0FGJtxGnG2b8aAUkeZ49n9BRiUfBjqUfkc89n9BRg=='):C-B(G)}},A('JR8GOmiqWwD2f0FG9jbVPm018wQlHwY69n9BRss1trv2NtU+Joorzg=='):{A('NtEZA2iBbc8='):{M:{A('aIFtz/Y21T4m3EacaKpbAG018wSpOzDOJoorzvZ/QUY='):[],K:[],A('JoorziUfBjpG6LdTyzW2uygX1VclHwY69n9BRvY21T6Ufkc8'):[]}},A('rXDwZW2b8aAlHwY6JoorzvZ/QUb2NtU+bTXzBA=='):{M:{K:[]}}},A('qTswziaKK85ogW3P'):J,T:{A('JtxGnF0d5TNdHeUz'):{A('9n9BRqk7MM4+sEG29n9BRhSR5nhtm/GgJR8GOmiBbc/2NtU+NtEZAw=='):B(I),A('993dX6k7MM7h9uAmtstluMs1trv2f0FGoj7sDKk7MM4+sEG29n9BRhSR5nj2f0FGlH5HPPY21T62y2W4qTswzg=='):B(I),A('4fbgJvY21T4+sEG2FJHmeG2b8aAlHwY6aIFtz/Y21T420RkD'):B(I),A('4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8yoU0rCUfBjpogW3PyzW2u2iqWwBdHeUz'):B(I),A('4fbgJvY21T6Ufkc8aIFtz6k7MM6Ufkc8AS7Ag2018wQlHwY6KBfVV6k7MM4='):B(I),A('9jbVPq1w8GUlHwY6JtxGnMs1trv2f0FGa7PVvQ=='):B(I),A('9n9BRpR+RzwlHwY6Joorzl0d5TPUMBAA9jbVPpR+RzxtNfME'):B(I),A('9n9BRpR+RzwlHwY6Joorzl0d5TPLNba79n9BRss1trv2NtU+Joorzg=='):B(I)},A('dHiepV0d5TM='):{A('JR8GOmiqWwBogW3PyzW2u/Y21T4='):E,A('KBfVV6k7MM72NtU+ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):E,A('ov26rvY21T4m3EacJR8GOqL9uq4UkeZ49n9BRvY21T6Ufkc8JR8GOigX1VepOzDO'):A('XR3lM2iqWwCtcPBlrXDwZfY21T6Ufkc89n9BRqk7MM5ogW3P'),A('9n9BRvY21T5oqlsAJtxGnG2b8aA='):E,A('Rui3U8s1trtogW3PqTswzvY21T4='):E,A('NtEZA6k7MM7h9uAm993dX/Y21T6Ufkc8tstluKk7MM6Ufkc8'):E},N:B(F)},S:{A('Rui3U6k7MM4miivOaIFtz/Y21T6Ufkc8'):A('Qb5QK2iqWwAlHwY6ov26ribcRpz2NtU+bTXzBG018wQ='),A('bTXzBPY21T5ogW3PqTswzqL9uq4='):A('uyYyPWiBbc+Ufkc8qTswziaKK872NtU+RSyrBbgQDICiPuwMNNAlY/4rdsVFLKsFWFwvMSAUG023xgvW'),A('qTswzj6wQbb2f0FGqTswziaKK85dHeUzyzW2u/Y21T4miivOXR3lMw=='):[A('993dX6OAIdOjyew7pq8QKR2xvSknMhNjaIFtz6k7MM7h9uAmaKpbACgX1VcnMhNjlH5HPKk7MM4miivOaIFtz6k7MM6Ufkc8qTswzpR+RzwnMhNjyzW2uyaKK87UMBAA9jbVPg=='),A('993dX6OAIdOjyew7pq8QKR2xvSknMhNjov26rvY21T5dHeUzqTswzicyE2Mm3Eac9jbVPiaKK872f0FGqTswzj6wQbb2f0FG')]},R:V,P:{A('9n9BRiUfBjomiivO'):A('0Osqb7dJqhvI6tkiCIEKE65DDrG3SaobCIEKEwiBChNI1ldcSNZXXK5DDrFL/BCZSNZXXBs3FYcIgQoTGzcVh65DDrEIgQoTIBQbTQ=='),A('XR3lM8s1trsmiivO'):A('t8YL1sjq2SJI1ldct0mqGxs3FYdI1ldcSNZXXLdJqhtLvrK6t0mqG65DDrG3Saobt0mqGyAUG01LvrK6t8YL1kjWV1wgFBtN'),A('JtxGnPY21T5dHeUz'):A('0Osqb7fGC9bI6tkiIBQbTRs3FYcgFBtNS/wQmUjWV1xYXC8xt0mqG7dJqhu3SaobS76yuiAUG00bNxWHIBQbTQiBChNLvrK6t0mqGw==')},A('1DAQAKL9uq4lHwY6XR3lM22b8aBHrvhtqTswzpR+RzxdHeUzyzW2u/Y21T4miivO'):V,A('rXDwZaL9uq5oqlsAKBfVV8s1trsmiivOXR3lMw=='):L,A('aIFtz2iqWwCtcPBlqTswzmiBbc914aaGov26rmiqWwAoF9VXyzW2uyaKK85dHeUz'):L,A('XR3lMybcRpyUfkc8qTswzqk7MM4miivOAS7AgyaKK87UMBAA9jbVPg=='):A('yoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvyoE+MiV7OD7Q6ypvt8YL1tDrKm9X/UUH0Osqb1f9RQfQ6ypvV/1FBw==').format(screen_width,U,U),A('ov26rl0d5TM8XXep4fbgJss1trtogW3P'):A('ximjkA==')+O(Q.randint(B(H),B('S76yuku+sro=')))+A(Y)+O(Q.randint(B(Z),B(a)))+A(Y)+O(Q.randint(B(Z),B(a)))+A(Ae)+O(J),A('9n9BRss1trttNfMEqTswzsytUMP2NtU+Joorzqk7MM4='):timezone_offset,A('lH5HPKk7MM7UMBAAqTswzpR+RzyUfkc8qTswzpR+Rzw='):url,A('aKpbAF0d5TOpOzDOlH5HPLsmMj0oF9VXqTswziaKK872f0FG'):user_agent,A('ov26rvY21T4m3EacJR8GOvZ/QUbLNba79jbVPiaKK84='):url,A('NtEZA6k7MM7h9uAmjzmGSJR+RzzLNba7Rui3U6k7MM6Ufkc8'):AR,A('qTswzpR+RzyUfkc89jbVPpR+RzxdHeUz'):[],A('Rui3U6k7MM6Ufkc8XR3lM8s1trv2NtU+Joorzg=='):A('CIEKE8jq2SK3xgvWyOrZIrfGC9Y=')}
def fff(fingerprint=V):
	B=fingerprint
	if B is V:B=B8()
	C=json.dumps(B,separators=(A('kH10Dw=='),A(Ae)));D=B6(C);E=B7(D);F=A('yoE+MiV7OD5+z1mMyoE+MiV7OD4=').format(E,C);G=B3(F.encode(A3),B2);H=A7.b64encode(G).decode(AQ);return A('o4Ah0yusYcZogW3PAS7Ag6I+7AypOzDOK6xhxl0d5TPRKpJP')+O(H)
class ggg:
	def __init__(A):A._data_types={};A._profiles={}
	def add_profile(A,name,fields):A._profiles[name]=fields
	def add_data_type(B,*,data_type_id,jwk_public_key,provider_id,key_id):A=data_type_id;B._data_types[A]=B0(data_type_id=A,jwk_public_key=jwk_public_key,provider_id=provider_id,key_id=key_id)
	def encrypt_string(D,value,*,data_type_id,requires_tail=AR,encryption_context=V):
		E=value;C=data_type_id
		try:from aws_encryption_sdk import EncryptionSDKClient as I,CommitmentPolicy as J;from aws_encryption_sdk.identifiers import Algorithm as K
		except A6 as M:raise A5(AS)from M
		if C not in D._data_types:raise AT(A('PF13qSaKK862y2W4JoorzvY21T420RkDJoorzkUsqwVogW3PJR8GOvZ/QUYlHwY6RSyrBfZ/QUZrs9W9rXDwZak7MM7RKpJP')+O(C))
		N=D._data_types[C];P=N.get_provider();Q=E.encode(A3);R=encryption_context or{};S=I(commitment_policy=J.FORBID_ENCRYPT_ALLOW_DECRYPT);T,U=S.encrypt(source=Q,key_provider=P,encryption_context=R,frame_length=B(F),algorithm=K.AES_128_GCM_IV12_TAG16);G=A7.b64encode(T).decode(AQ)
		if requires_tail:
			H=L.join(B for B in E if B not in A('RSyrBdDrKm8='))[-B(Y):]
			if o(H)>B(k):G+=A('/wOKvg==')+H
		return G
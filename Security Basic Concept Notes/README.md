# Table of Contents

- 시스템 보안
- 네트워크 보안
- 어플리케이션 보안
- 정보보안 일반
- 정보보안관리 및 법규

<br/>

-----

- 리눅스에서 PID 1인 프로세스는 init이며, 모든 다른 프로세스들은 init 프로세스의 자손들이 된다.

---------

### What are the exact roles of a Windows account's SID, and more specifically its RID, for Windows security?

Every Windows user, computer, or service account has a unique alphanumeric identifier called the security ID (SID). Windows security-related processes, such as authentication, authorization, delegation, and auditing, use SIDs to uniquely identify security principals. Because SIDs are used by system processes, the format of a SID—unlike the format of a logon name—isn't user- or administrator-friendly.

To illustrate, let us analyze an example SID that I retrieved from my test Active Directory (AD) system: 

`S-1-5-21-4064627337-2434140041-2375368561-1036`

All SID fields have a specific meaning; so, for the above sample SID:

> **S | The initial S identifies the following string as a SID.**
> **1 | The revision level, or version, of the SID specification. To date, this has never changed and has always been 1.**
> **5 | The identifier authority value. This is a predefined identifier for the top-level authority that issued the SID. This is typically 5, which represents the SECURITY_NT_AUTHORITY.**
> **21-4064627337-2434140041-2375368561 | This section is the domain or local computer identifier (in this example, a domain identifier). This is a 48-bit string that identifies the authority (the computer or domain) that created the SID.**
> **1036 | The Relative ID (RID) is the last part of a SID. The RID uniquely identifies a security principal relative to the local or domain security authority that issued the SID. Any group or user that the Windows OS doesn't create has a RID of 1000 or greater by default.**

The SID of an AD domain account is created by a domain's security authority that runs on every Windows domain controller (DC). The SID of a local account is created by the Local Security Authority (LSA) service that runs on every Windows box.

An important property of a SID is its uniqueness in time and place. A SID is unique in the environment where it was created (in a domain or on a local computer). It's also unique in time: If you create a user object, delete it, then recreate it with the same name, the new object won't have the same SID as the original object.

-----

- SetUID 설정된 file 혹은 directory 찾기 명령어
  - SetUID 혹은 SetGID 를 찾을 때는 명령어 'find' 를 사용한다.

```bash
find [파일을 검색할 디렉토리 경로] -user [소유자] -perm [접근권한]

find / -user root -perm -4000   -> SetUID
find / -user root -perm -2000   -> SetGID
```

> find : 찾기 명령어
>
> / : 최상위로부터
>
> -user [소유자] : 소유주는 root이며
>
> -perm : permission 은 4000인 것을 찾는다.

---

### HEAP

- HEAP 영역은 malloc(), calloc() 등으로 프로그래머가 자율적으로 메모리 크기를 할당할 수 있는 영역이다.

  위 함수들로 할당된 영역은 동적할당 영역으로 free()함수로 할당된 영역을 반납해줘야한다.

-----

- SMTP : Simple Mail Transfer Protocol

  전자메일의 안정적인 전송을 위해 제안된 프로토콜

- POP3와 IMAP은 메일은 수신하기 위한 프로토콜

- SNMP : Simple Network Management Protocol

  TCP/IP의 망 관리 프로토콜

---

### 트로이목마(Netbus)

- 일반 프로그램에 악의적인 루틴을 추가하여 그 프로그램을 사용할 때 본래의 기능 이외에 악의적인 기능까지 은밀히 수행하도록 하는 공격

- 사용자 암호를 도출하기 위해서 합법적인 로그인(login) 프로그램으로 가장하고 정상적인 로그인 순서와 대화를 모방하여 작성될 수 있다.

-----

- File Permissions

  특수권한(3bit) - user(3bit) - group(3bit) - other(3bit) : [suid, sgid, sticky-bit | rwx | rwx | rwx]

----

- 윈도우 인증의 구성요소 : LSA, SAM, SRM
- NTLM : Challenge & Response 인증 프로토콜

---

- `chmod` 명령은 기존 파일의 접근권한을 변경할 때 사용한다.

  이때 8진수로 지정하는 접근권한은 해당 파일이 가져야 할 권한을 명시한 것이다.

- `umask` 명령은 새로 만들어질 파일이나 디렉터리가 갖지 말아야할 권한을 명시한다.

  접근권한은 일반적으로 파일을 생성할 때는 666에서 umask로 지정한 값을 빼고, 디렉터리의 경우 777에서 umask로 지정한 값을 빼게 된다.

---

### Teardrop Attack

네트워크상에서 IP가 정상적으로 패킷을 전송할 때 IP 단편화(fragmentation)가 발생하게 된다.

수신자는 재조립을 통해 단편화된 데이터를 복구하게 된다.

이때 재조립 시에 정확한 조립을 위해 오프셋(Offset)이란 값을 더하게 되어 있는데, 이 오프셋 값을 단편화 간에 중복되도록 고의적으로 수정하거나 정상적인 오프셋 값보다 더 큰 값을 더해 그 범위를 넘어서는 오버플로우를 일으켜 시스템의 기능을 마비시켜 버리는 DoS 공격기법의 하나이다.

-----

### Smurf DoS Attack

공격자가 출발지 IP 주소를 목표 시스템으로 스푸핑하고 목적지 주소를 직접 브로드캐스트 주소(Directed Broadcast Address)로 설정한 Ping 메시지를 송신하고, Ping 메시지를 수신한 네트워크 내의 모든 시스템이 Ping 응답 메시지를 출발지 주소인 공격 목표 시스템으로 동시에 전송함으로서 공격 목표를 마비시킨다.

----

### False Negative

- 공격자가 실제로 시스템에 침입하였으나 침입 탐지 시스템은 이를 정상적인 동작으로 인식하여 침입을 제대로 탐지 못한 경우의 판정

----

### Ping of Death Attack

- Ping을 이용하여 ICMP 패킷을 정상적인 크기(65,535 bytes)보다 아주 크게 만든 것이다.

- 이렇게 크게 만들어진 패킷은 네트워크를 통해 라우팅(Routing)되어 공격 대상 네트워크에 도달하는 동안에 아주 작은 조각(Fragment)이 된다.

- 공격의 대상이 되는 시스템은 이렇게 작게 조각화된 패킷을 모두 처리해야 되기 때문에 정상적인 Ping의 경우보다 훨씬 많은 부하가 걸리게 되어 정상적인 서비스를 방해 받게 된다.

-----

### Tiny Fragment Attack (Tiny Fragmentation)

- IP 헤더보다 작은 fragment를 만들어서 침입차단시스템(방화벽)을 우회하여 내부 시스템에 침입하는 공격기법으로 DoS 공격 기법이 아닌 우회 공격 기법이다.

```
A Tiny Fragment attack is IP fragmentation that is the process of breaking up a single Internet Protocol (IP) datagram into multiple packets of smaller size.
Every network link has a characteristic size of messages that may be transmitted, called the maximum transmission unit (MTU).
If the data packet size is made small enough to force some of a TCP packet’s TCP header fields into the second data fragment, filter rules that specify patterns for those fields will not match.
If the filtering implementation does not enforce a minimum fragment size, a disallowed packet might be passed because it didn’t hit a match in the filter.
STD 5, RFC 791 states that, “Every Internet module must be able to forward a datagram of 68 octets without further fragmentation.”
This is because an Internet header may be up to 60 octets, and the minimum fragment is 8 octets.
IP fragmentation exploits (attacks) use the fragmentation protocol within IP as an attack vector.
```

----

- 지식기반 침입탐지(오용탐지) 방법

  알려진 침입행위를 이용하여 침입을 탐지하고, 정해진 모델과 일치하는 경우를 침입으로 간주한다.

  이러한 방법에는 전문가시스템(Expert System), 시그니처 분석(Signature Analysis), 페트리넷(Petri-net), 상태전이분석(State Transition Analysis) 등이 있다.

- 비정상 행위 탐지(Anomaly Detection)은 통계적 분석이다.

---

### WPA-PSK 인증방식 취약점 (WPA/WPA2 방식)

- WPA-PSK를 이용하여 무선 네트워크를 구성할 때 접속/인증 패스워드를 짧게 설정하거나 추측하기 쉬운 값으로 설정할 경우 사전 공격(Dictionary Attack)을 통해 손쉽게 패스워드를 크랙할 수 있는 취약점이 있다.

----

### CCMP

- CCMP는 AES 블록 암호를 사용한 데이터의 비밀성과 무결성을 보장하기 위한 규칙을 정의하고 있다.
- TKIP이 RC4를 사용한 암호를 사용하는 반면, CCMP는 이미 전문가들의 많은 검토를 통해 안전성이 입증된 AES를 기반으로 한다.
- CCMP는 8021.11i를 사용한 보안에서의 기본 모드에 해당하며, 더 높은 보안성을 갖는다.
- TKIP가 기존의 하드웨어를 수용하기 위한 과도기적 기법인 반면 CCMP는 기존 하드웨어를 고려하지 않고 초기부터 보안성을 고려하여 새롭게 설계되어있다.

----

### NAC의 주요 기능

- 접근 제어/인증
  - 내부 직원 역할 기반의 접근 제어
  - 네트워크의 모든 IP 기반 장치 접근 제어
- PC 및 네트워크 장치 통제 (무결성 체크)
  - 백신 관리
  - 패치 관리
  - 자산 관리 (비인가 시스템 자동 검출)
- 해킹, 웜, 유해 트래픽 탐지 및 차단
  - 유해 트래픽 탐지 및 차단
  - 해킹 행위 차단
  - 완벽한 증거 수집 능력

----

### ESM(Enterprise Security Management)

> 각종 네트워크 보안제품의 인터페이스를 표준화하여 중앙 통합 관리, 침입 종합대응, 통합 모니터링이 가능한 지능형 보안 관리 시스템이다.

ESM은 매니저, 콘솔, 에이전트 3가지로 구성이 된다.

에이전트에서 로그를 수집하고 수집된 로그를 매니저로 전송한다.

매니저에서는 수집된 로그들의 연관 분석을 통해 정보를 발생시키고 콘솔에서 해당 정보를 확인할 수 있다.

- Agent Part
  - 보안 장비에 탑재
  - 수집된 데이터를 Manager 서버에 전달하고 통제를 받음
- Manager Part
  - Agent Part에서 받은 이벤트를 룰에 의해 분석, 저장
  - Console Part에 그 내용을 인공 지능적으로 통보
- Console Part
  - Manager Part에서 받은 데이터의 시각적 전달, 상황 판단 기능
  - Manager Server에게 룰을 설정하도록 지휘/통제

-----

### BlackNurse Denial of Service Attack (2016.11.21)

> 단 한 대의 컴퓨터로 거대한 서버들을 다운시킬수 있는 BlackNurse 공격은 ICMP Type 3(Destination Unreachable) Code 3(Port Unreachable) 요청을 기반으로 하는 공격 기법이다.

<br/>

**단일 컴퓨터로 대형 서버를 다운시킬 수 있는 BlackNurse 공격**

- TDC SOC(Security Operations Center)에서 ICMP 프로토콜을 기반으로 한 새로운 DoS 공격을 발견하고 이를 BlackNurse 공격이라 명함
  - BlackNurse 공격은 기존 ICMP Flood Attack의 트래픽량에 기반한 DoS 공격이 아님
  - 트래픽 속도와 초당 패킷 전송 속도가 매우 낮음에도 불구하고 대형 인터넷 링크 및 대기업 방화벽 장비를 공격하는 것이 가능함

<br/>

**BlackNurse**

- 기존 ICMP를 이용한 Ping Flood Attack은 ICMP Type 8 Code 0을 기반으로 함.
- BlackNurse는 ICMP Type 3(Destination Unreachable) Code 3(Port Unreachable) 요청을 기반으로 하는 공격 기법
  - 일반적인 ICMP Echo 메시지에 비해 ICMP Type 3 Code 3가 일부 방화벽에서 상당히 많은 리소스를 소비하고 있음이 밝혀짐
- 낮은 대역폭에서도 효과적
  - 15-18 Mbit/s의 대역폭, 초당 40~50K 패킷 전송속도로 공격을 진행함에도 큰 대역폭을 지닌 (1Gbit/s) 인터넷 링크 및 방화벽의 CPU 부하를 높일 수 있음

<br/>

**대응방안**

- ICMP Type 3 Code 3을 비활성화
  - 방화벽 및 다른 종류의 장비에서 신뢰할 수 있는 ICMP 리스트 구성
  - 그러나 ICMP Type 3을 차단한 경우, MTU 검색이 비활성화되어 IPSec 및 PPTP 트래픽이 중단 될 수 있음
- ISP의 전문 DDoS 방지 솔루션 사용

----

- DoS 공격 중 Land 공격은 출발지 IP 주소와 목적지 IP 주소값을 똑같이 만들어서 공격대상에 보내는 것으로, 출발지 주소를 공격대상의 IP로 바꿔서 공격한다.

---

- 포맷 스트링 공격은 포맷 스트링을 인자로 하는 함수의 취약점을 이용한 공격으로 외부로부터 입력된 값을 검증하지 않고 입출력 함수의 포맷 스트링을 그대로 이용하는 경우 발생할 수 있는 취약점이다.

  공격자 포맷 스트링을 이용하여 취약한 프로세스를 공격하거나 메모리 내용을 읽거나 쓸 수 있다.

  그 결과 공격자는 취약한 프로세스의 권한을 획득하여 임의의 코드를 실행할 수 있다.

  프로그램의 복제와는 무관하다.

-----

- URL Encoding(Percent Encoding) / Decoding
  - %27 : single quotation mark (')
  - %3D : equal mark (=)
  - %20 : space mark (빈칸)
  - %2D : hyphen mark (-)

----

### FTP 전송모드

FTP의 Default는 Active 모드이며, Active 모드 및 Passive 모드의 사용 여부는 FTP 서버가 아닌 클라이언트가 결정한다.

- Passive mode에서는 서버의 21번 포트와 1024번 이후의 포트를 사용한다.
- Active mode에서의 데이터 채널은 서버에서 클라이언트로 접속한다.
- 클라이언트가 방화벽으로 보호되어 있는 경우에는 Passive 모드를 통해 FTP 서비스를 이용할 수 있다.
- Passive mode에서는 클라이언트가 서버로 접속한다.

----

### FTP bounce attack

FTP 프로코톨이 단순히 데이터 전송할 목저지는 확인하지 않고 데이터만 전송한다는 FTP 프로토콜 자체의 취약점을 이용한 공격 방법이다.

FTP 서버나 사용자를 공격하는 것이 아니고 그 FTP서버를 경유해서 접근 가능한 내부 서버를 공격/스캔하는 방식이다.

오래 전부터 문제시 된 공격방법으로 최근 이러한 취약점을 해결한 프로그램이 개발되었지만, 아직까지 FTP에서 매우 위협적인 공격이며 이를 이용한 공격이 인터넷상에서 쉽게 이루어진다.

----

- 메일 전송을 interception 후 다시 보내는 공격을 방지하는 것이 Message Reply Prevention이다.

----

- 스팸 필터 솔루션

  스팸 필터 솔루션은 메일 서버 앞단에 위치하여 프락시 메일 서버로서 동작하며, SMTP 프로토콜을 이용한 DoS 공격이나 폭탄 메일, 스팸 메일을 차단한다.

  또한 전송되는 메일의 바이러스까지 체크할 뿐만 아니라 내부에서 밖으로 전송되는 메일에 대한 본문 검색 기능을 통해 내부 정보 유출도 방지한다.

---

- PGP(pretty good privacy)의 보안 지원기능

  - 기밀성, 메시지 인증, 사용자 인증, 송신 부인 방지

  PGP는 수신 부인 방지는 지원하지 않는다.

---

- FTP 서비스 사용 시 사용자 계정별로 로그인을 제한하기 위한 파일은 `/etc/ftpusers` 이며, 일반적으로, root, daemon, lp, guest 등 Well-known 계정을 등록하여 해당 계정의 로그인을 금지한다.
- `/etc/ftpusers` 에 사용자 ID가 들어 있으면 접근을 거부하며, ftpusers 파일의 소유자는 root, 권한은 640 이하가 바람직하다.

----

- DNS를 보호하기 위해 IETF라는 DNSSEC이라고 불리는 기술을 만들어 메시지 송신자 인증과 전자서명이라는 보안 서비스를 사용해 메시지 완전 무결성을 제공한다.

  그러나 DNSSEC은 DNS 메시지에 대한 기밀성은 제공하지 않으며, DNSSEC 스펙에는 서비스 거부 공격에 대한 방지책이 없다.

  그러나 캐싱 서비스를 통해 이러한 공격에 대해 어느 정도까지는 상위 계층 서비스를 보호하게 된다.

----

### BYOD 보안 기술

- MDM (Mobile Device Management)
  - 통상 IT 부서가 기기를 완전히 제어할 수 있도록 지원의 스마트패드와 스마트폰에 잠금, 제어, 암호화, 보안 정책 실행을 할 수 있는 기능을 제공
  - MDM이 적용된 스마트폰에서는 기업의 보안 정책에 위배되는 앱은 설치 및 구동 불가능
- 컨테이너화 (Containerization)
  - 프라이버시 요구가 커짐에 따라 하나의 모바일 기기 내에 업무용과 개인용 영역을 구분해 보안 문제와 프라이버시 보호를 동시에 해결하려는 기술
  - 컨테이너라는 암호화된 별도 공간에 업무용 데이터와 개인용 데이터를 분리하고 관리
- 모바일 가상화 (Hypervisors)
  - 하나의 모바일 기기에 개인용과 업무용 운영체제(OS)를 동시에 담아 개인과 사무 정보를 완전히 분리
  - 평상시에는 개인용 운영체제에 맞춰놓고 스마트폰을 사용하다 업무를 해야할 경우, 운영체제를 업무용으로 전환
- NAC (Network Access Control)
  - 사용자 기기가 기업 내부 네트워크 접근 전 보안 정책을 준수했는지 여부를 검사하여 비정상 접근 여부에 따라 네트워크 접속을 통제하는 기술

----

### MAC 정책

> 객체에 포함된 정보의 비밀성과 이러한 비밀성에 주체가 접근할 수 있는 권한에 근거하여 객체에 대한 접근을 제한하는 정책이다.
>
> 한 자원에 접근할 수 있는 허가증을 가진 객체가 단지 자신의 의지만으로 다른 객체도 자원에 접근하게 할 수 없기 때문에 `mandatory` 라고 불린다.

----

### Biba Integrity Model (비바 무결성 모델)

무결성을 위한 상업용 모델로 BLP 모델 이후에 개발된 모델이다.

이 모델은 상태머신 모델이며 최초의 수학적 무결성 모델로서, 무결성의 3가지 목표 중 비인가자에 의한 데이터 변형 방지만 취급한다.

이 모델에서는 비인가자들의 데이터 변형에 대한 방지만 취급하며, 주체는 보다 낮은 무결성 정보를 읽을 수 없다. (no read down policy)

주체는 또한 자신보다 높은 무결성 수준의 객체를 수정할 수 없다. (no write up policy)

이 모델은 상태 머신(state machine) 모델에 기반을 두고 있다.

---

### Lattice Model

역할에 할당된 민감도 레벨에 의해 결정된다. (주체 및 객체에게 보안클래스 부여, 정보흐름 통제)

주체와 객체의 관계에 의거하여 접근할 수 있는 Uper bound와 Lower bound를 설정하여 접근을 제어하는 것이다.

예를 들어, 핵무기와 관련된 임무를 수행하고 있는 사람은 이와 관련된 상, 하위 정보로만 접근통제한다.

---

- 커버로스는 기업 접근 통제를 위해 필요한 네 가지 요소(확장성, 투명성, 안정성, 보안)를 가진다.

  그러나 이러한 개방형 아키텍처는 또한 상호운용성 논점을 가져온다.

  공급업체들이 프로토콜을 원하는 대로 수정할 수 있는 자유를 가지게 되면, 이것은 일반적으로 어떠한 공급업체도 동일한 방식으로 프로토콜을 수정하지 않는다는 것을 의미한다.

  이것은 상호운용성과 상호호환성 논점을 발생시킨다.

---

- 공개키 암호화시스템에서 수신자의 공개키로 암호화하고 수신자의 사설키로 복호화하는 것은 암호 모드로 비밀성(기밀성) 서비스를 제공하고, 송신자의 사설키로 암호화하고 송신자의 공개키로 복호화하는 것은 인증모드로 인증과 부인방지 서비스를 제공한다.

---

###  CRL 엔트리(개체) 확장

ANSI X9와 ISO/IEC/ITU에서 X.509 v2 CRL 용으로 정의된 CRL 엔트리 확장은 추가적인 정보를 CRL 엔트리와 연결할 수 있는 방법을 제공한다.

- 원인 코드 (reason code)

  인증서 폐지의 원인을 정의하는 CRL의 non-critical 확장이다.

  인증기간은 CRL의 내용에 의미 있는 원인 코드를 입력해야 한다. (처리할 수 없는 critical 확장을 만나게 되면 CRL 검증은 반드시 실패해야 한다. 그러나 알 수 없는 non-critical 확장은 무시할 수 있다.)

- 정지 지시 코드 (hold instruction code)

  등록된 지시 식별자를 제공하는 CRL의 non-critical 확장이다.

  지시 식별자란 정지 상태에 놓여진 인증서를 만났을 때의 동작을 지시하는 식별자이다.

- 무효 날짜 (invalidity date)

  개인키가 손상되거나 인증서가 무효하게된 것을 의심하거나 알게 된 날짜를 나타내는 CRL의 non-critical 확장이다.

- 인증서 발급자 (certificate issuer)

  CRL과 관련하여 CRL 내의 효력정지 및 폐지된 인증서의 발급 기관에 대한 명칭을 나타낸다.

---

- 대칭키 암호화 알고리즘 : DES, AES, RC5, SEED, IDEA, ARIA
- 비대칭키 암호화 알고리즘 : Rabin
- 전자 서명 알고리즘 : ECDSA

----

### Key Distribution Problem (키 배송 문제)

> 대칭키 암호를 사용하려고 하면 키 배송 문제가 발생한다.
>
> 키를 보내지 않으면 수신자는 수신한 암호문을 복호화할 수 없다.
>
> 키를 보내면 도청자도 복호화할 수 있다.
>
> 이것을 대칭키 암호의 키 배송 문제라 한다.

<br/>

키 배송 문제를 해결하기 위한 방법에는 

> - 키의 사전 공유에 의한 방법
>- 키 배포 센터에 의한 방법
> - Diffie-Hellman 키 교환에 의한 방법
> - 공개키 암호에 의한 방법    

등이 있다.

---

### 공개키 사용 원칙

- 암호화키와 복호화키는 같은 사람(동일 인물)의 키 쌍이어야 한다.
- 키는 암/복호화 중 한 번만 사용해야 한다.
- 타인의 개인키는 사용할 수 없다.

----

### 블록 암호에 대한 공격

- 차분 분석 (차분 해독법, differential cryptanalysis)

  블록 암호를 보면 입력되는 평문이 한 비트라도 달라지면 암호문은 전혀 다른 비트 패턴으로 변화하게 된다.

  그래서 암호문의 변화 형태를 조사하여 해독의 실마리를 얻는 해독 방법이다.

- 선형 분석 (선형 해독법, linear cryptanalysis)

  마츠이(Matsui)가 개발한 방법으로 평문과 암호문 비트를 몇 개 정도 XOR해서 0이 되는 확률을 조사하는 해독 방법이다.

- 전수공격법 (exhaustive key search)

  1977년 Diffie와 Hellman이 제안한 방법으로 암호화할 때 일어날 수 있는 가능한 모든 경우에 대하여 조사하는 방법이며, 경우의 수가 적을 때는 가장 정확한 방법이지만, 일반적으로 경우의 수가 많은 경우에는 실현 불가능한 방법이다.

- 통계적 분석 (statistical analysis)

  암호문에 대한 평문의 각 단어별 빈도에 관한 자료와 더불어 지금까지 알려진 모든 통계적인 자료를 이용하여 해독하는 방법이다.

- 수학적 분석 (mathematical analysis)

  통계적인 방법을 포함하여 수학적 이론을 이용하여 해독하는 방법이다.

----

- Feistel 구조
  - DES, SEED, LOKI, CAST, Blowfish, MISTY, RC5, RC6, CAST256, E2, Twofish, Mars
- SPN
  - SAFER, SHARK, Square, CRYPTON, AES(Rijndael), SAFER+, Serpent, PRESENT

----

- 이중서명의 목적은 상점이 카드 사용자의 계좌번호와 같은 지불정보를 모르게 하는 동시에 상점에 대금을 지불하는 은행은 카드 사용자가 상점에서 산 물건을 모르지만 상점이 요구한 결제 대금이 정확한지 확인 할 수 있게 하는 것이다.
- 이중서명은 SET에서 도입된 기술로 고객의 구매 정보를 상인에게 전달하면 상인은 그 요청에 유효성을 확인하게 된다.

----

### OCSP (Online Certificate Status Protocol)

- 특정 인증서에 대한 유효성과 취소 정보를 신속하고 효율적으로 온라인상에서 알 수 있도록 구성되어 인증서의 상태에 관한 정보 조회가 가능한 프로토콜이다.

- OCSP는 인증서의 상태를 조회하는 클라이언트, 클라이언트의 요구에 응답하여 상태 정보를 전달하는 OCSP 서버 그리고 일부 인증서의 상태 정보를 저장하는 CA로 구성된다.

----

- 대칭키 암호시스템은 기밀성을 제공하고, 공개키 암호시스템에서는 기밀성, 부인방지, 인증을 제공한다.

----

- 정보통신망법에 따른 암호화 대상
  - 주민등록번호, 여권번호, 운전면허번호, 외국인등록번호, 신용카드번호, 계좌번호, 바이오정보
- 개인정보보호법에 따른 암호화 대상
  - 고유식별정보, 비밀번호, 바이오정보

-----


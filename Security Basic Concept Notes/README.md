# Awesome Security of my own

- 리눅스에서 PID 1인 프로세스는 init이며, 모든 다른 프로세스들은 init 프로세스의 자손들이 된다.

---------

### What are the exact roles of a Windows account's SID, and more specifically its RID, for Windows security?

Every Windows user, computer, or service account has a unique alphanumeric identifier called the security ID (SID). Windows security-related processes, such as authentication, authorization, delegation, and auditing, use SIDs to uniquely identify security principals. Because SIDs are used by system processes, the format of a SID—unlike the format of a logon name—isn't user- or administrator-friendly.

To illustrate, let us analyze an example SID that I retrieved from my test Active Directory (AD) system: `S-1-5-21-4064627337-2434140041-2375368561-1036`. All SID fields have a specific meaning; so, for the above sample SID:

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

##### HEAP

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


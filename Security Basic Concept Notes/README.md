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

- HEAP 영역은 malloc(), calloc() 등으로 프로그래머가 자율적으로 메모리 크기를 할당할 수 있는 영역이다.
  - 위 함수들로 할당된 영역은 동적할당 영역으로 free()함수로 할당된 영역을 반납해줘야한다.
# Security Engineering (보안 공학)

<br/>

## Table of Contents (목차)

### Paper

- (2004.10) Basic Concepts and Taxononmy of Dependable and Secure Computing - IEEE

<br/>

<br/>

## (2004.10) Basic Concepts and Taxononmy of Dependable and Secure Computing - IEEE

> https://ieeexplore.ieee.org/document/1335465
>
> https://www.researchgate.net/publication/3449335_Basic_Concepts_and_Taxonomy_of_Dependable_and_Secure_Computing

**신뢰할 수 있고 안전한 컴퓨팅의 기본 개념 및 분류**

<br/>

### Abstract (요약)


&nbsp;이 논문은 신뢰도(reliability), 가용성(availability), 안전성(safety), 무결성(integrity), 유지 보수성(maintainability) 등과 같은 특수한 경우를 포함하는 일반적인 개념인 신뢰성(dependability)과 관련된 주요 내용들을 정의한다. 보안은 가용성 및 무결성 외에도 기밀 유지(confidentiality)에 대해서도 고려해야 한다. 그에 대해서는 기본 정의들이 먼저 주어져야 한다. 그런 다음, 신뢰성과 보안에 대한 위협(결함(faults), 오류(errors), 장애(failures))과 속성 및 달성 수단(결함 방지(fault prevention), 내결함성(fault tolerance), 결함 제거(fault removal), 결함 예측(fault forecasting))을 해결하는 추가 정의에 대한 의견을 제시하고 이를 보완한다. 최종 목표는 광범위한 상황에 걸쳐 관련성이 있는 일련의 일반적인 개념을 설명하는 것이며, 그에 따라 특정 유형의 시스템, 시스템 장애에 또는 시스템 장애의 원인을 포함하여 수많은 과학 및 기술 커뮤니티 간의 의사소통과 협력을 돕는 것이 목표이다.

<br/>

### 1 Introduction (서론)

&nbsp;본 논문은 컴퓨팅 및 통신 시스템의 신뢰성과 보안을 다룰 때 실행되는 다양한 개념을 특징짓는 정확한 정의를 제공하는 것을 목표로 한다. 시스템 경계가 모호한 시스템에 대해 논의할 때 이러한 개념들을 명확히 하는 것은 의외로 어렵다. 더욱이, 이러한 시스템의 복잡성 혹은 사양은 주요 문제일 뿐만 아니라, 장애(failures)가 발생할 수 있는 원인이나 결과를 정의하는 것은 매우 복잡미묘한 프로세스이고 장애(failures)를 유발하는 결함(faults)들을 막기 위한 조항들이 있다.

&nbsp;신뢰성(Dependability)은 신뢰도(reliability), 가용성, 안전성, 무결성, 유지 보수성 등의 일반적인 속성을 포함하는 포괄적인 개념으로 처음 소개되었다. 보안을 고려하면 가용성, 무결성 외에도 기밀성에 대한 우려가 생긴다. 그런 다음, 기본 정의는 추가 정의들을 통해 보완된다. **굵은 글씨**는 용어가 정의될 때 사용되며, *이탤릭체* 는 독자의 주의를 집중시키기 위해 사용된다.

&nbsp;본 논문은 효과적인 기술적 상호 작용을 용이하게 하기위해 다양한 전문 분야의 개념에 대해 최소한의 합의를 문서화하려는 시도로도 볼 수 있다. 또한 1) 다른 기관(표준화 기구를 포함한)에서 사용하고 2) 교육 목적에 적합하길 바란다. 우리의 관심사는 개념에 있다. 단어는 개념에 분명하게 레이블을 붙이고 아이디어와 관점을 공유할 수 있기 때문에 유심히 봐야한다. 아직 합의가 이루어지지 않았다고 생각하는 중요한 문제는 신뢰성(dependability)과 보안(security)의 척도에 관한 것이다. 이 문제는 여기에 제시된 분류의 다른 측면과 일관되게 문서화하기 전에 추가 정교화가 필요하다.

&nbsp;이 논문은 최첨단 기술을 문서화하지 않는다. 개념에 집중하면서, 표준에서 찾을 수 있는 문제들([30] 안전을 위한 이나 [32] 보안을 위한)을 다루지 않는다. 

&nbsp;신뢰성(dependability)과 보안 커뮤니티들은 분명히 구별되지만, 점차 같은 길로 수렴해 왔다. 1) 신뢰성(dependability)은 악의적이지 않은 결함(faults)이 문제의 일부만을 다루고 있는 것에 대해서 제한적이라는 것을 알게 되었다. 2) 보안은 과거의 기밀성에 중점을 두었던 것이 무결성 및 가용성에 대한 우려로 확대되어야 한다는 것을 알게 되었다. (이전에도 정의되었었지만, 기밀성(confidentiality)만큼 많은 관심을 받지 못했다.) 이 논문에서는 신뢰성과 보안의 공통된 부분을 하나의 가닥으로 모으는 것을 목표로 하며, 공간 제한의 이유로 기밀성에 대해서는 크게 주의를 기울이지 않는다.

&nbsp;**미래를 위한 선행 작업 및 목표(Preceding Work and Goals for the Future).** 이러한 노력의 기원은 IEEE CS의 내결함성 컴퓨팅 TC와 IFIP WG 10.4 "신뢰할 수 있는 컴퓨팅 및 내결함성(Fault Tolerance)"에 의해 "기본 개념 및 용어"에 대한 공동 위원회가 구성된 1980년으로 거슬러 올라간다. 7 개의 서로 다른 논문이 1982 년 FTCS-12의 특별 세션[21]에서 발표되었으며, 합작은 1985년 FTCS-15[40]에서 이 논문의 이전 버전으로 발표되었다. 그리고 이 논문에서는 특히 신뢰성(dependability) 위협과 속성 측면에서 훨씬 더 자세히 다룬다.

&nbsp;1985년 발표된 합작은 1992년 책 *Dependability : Basic Concepts and Terminology* [41]로 이어졌다. 이 책은 34페이지 영어와 8페이지짜리 프랑스어, 독일어, 이탈리아어 및 일본어로 번역된 용어집이 포함되어 있다.  하나의 속성으로서의 보안과 결함(faults)의 분류에서, 의도적이고 악의적인 결함(faults)의 클래스가 추가되었다는 것이 개선사항이였다. 뿐만 아니라, 많은 개념들이 세련되고 정교해졌다.

&nbsp;그 다음 단계에서는 보안을 *기밀성*, *무결성* 및 *가용성* 의 속성들의 복합체로 인식하고, *부적절한 시스템 사양의 문제에 대한 분석과 함께 의도적인 비악의적 결함 클래스*를 추가하는 것이었지만, 신뢰성 위협에 대한 요약 분류만 제공했다.

&nbsp;본 논문은 신뢰할 수 있고 보안성이 높은 컴퓨팅의 분류 체계를 확장, 개선 및 단순화하기 위한 1995년 이후 지속적인 노력의 결과를 나타낸다. 분류 체계를 이 분야의 실무자와 학생들이 손쉽게 사용할 수 있도록하는 것을 목표로 한다. 따라서, 이 논문은 독립적이며 위에 언급된 문서들을 읽을 필요가 없다. 이 논문에서 주로 기여하고자 하는 바는 다음과 같다:

1. *신뢰성과 보안 사이의 관계* 를 명확하게 명시한다 (섹션 2.3).

2. *신뢰성에 대한 정량적 정의* 를 도입하였다 (섹션 2.3).

3. *잠재가능성의 기준* 은 인간이 만든 비악의적 결함(섹션 3.2.1 및 3.2.3)의 분류에 적용하여 잠재가능성을 고려할 수 있다.
4. *악의적인 결함(faults)에 대한 논의* 를 광범위하게 정의한다 (섹션 3.2.4).
5. *서비스 실패(Service failures)* (섹션 3.3.1)는 *신뢰성 실패(dependability failures)* (섹션 3.3.3) 와 구별한다. 후자는 일정 기간 서비스 실패가 너무 빈번하거나 너무 심각할 때로 정의한다.
6. 부분 및 전체 *개발 실패(development failures)* (섹션 3.3.2) 를 포함하여 *개발 프로세스의 신뢰성 문제* 를 분류 체계에 명시적으로 통합하였다.
7. *신뢰성(dependability) 개념은 의존(dependence) 및 믿음(trust)과 관련이 있으며* (섹션 4.2), 최근에 도입된 세 가지 유사한 개념인 생존성(survivability), 깨지지 않을 신뢰(trustworthiness), 높은 신뢰(high-confidence) 시스템과 구별한다.

 &nbsp;이처럼 지금의 광범위한 신판물 이후에, 분류법의 진화를 촉진할 미래 기회와 과제는 무엇이라고 예측할 수 있는가? 여기서 우리는 더 가치있는 것들이 무엇인지 깨닫는다:

- 예를 들어 기밀성 보호, 신뢰성 설정 등을 위한 기술을 다루기 위해 보안에 대한 논의를 확장

- 믿음(trust)의 이슈들이나 위험 관리의 통합된 토픽을 분석 

- 신뢰성(dependability)과 보안(security)에 대한 통합된 측정을 위한 검색

&nbsp;우리는 예기치 않게 우리가 이해하는 능력 이상으로 구축한 (Arthur C. Clarke의 "2001: A Space Odyssey"의 HAL 컴퓨터의 것과 같은 소위 "신흥 속성"으로 불리는) 인간-기계 시스템의 복잡성과 같은 몇 가지 도전 과제가 생길 것으로 예상한다. 또다른 도전 과제들은 예측하기가 더 쉽다:

1. 새로운 기술 (나노 시스템, 바이오칩, 화학 및 양자 컴퓨팅 등)과 인간-기계 시스템의 새로운 개념 (앰비언트 컴퓨팅, 노매딕 컴퓨팅, 그리드 컴퓨팅 등)은 그들 특성에 맞는 구체적인 신뢰성(dependability) 문제에 대해 지속적으로 요구할 것이다. 
2. 복잡한 인간-기계 상호 작용(사용자 인터페이스 포함)의 문제는 여전히 매우 중요한 과제이다. 신뢰성(dependability)과 보안(security)을 향상시키는 방법들을 파악하고 통합해야 한다.
3. 인간 본성의 어두운 면은 우리에게 새로운 형태의 악의를 예상하게 하며, 더 많은 형태의 악의적 결함(faults)으로 이어질 것이고, 더 나아가 새로운 방어에 대한 보완책으로 이끌것이다.

&nbsp;위에서 언급한 도전 과제들의 관점에서 그리고, 동일한 방법, 속성, 위협들을 설명하기 위해 도입되는 "새로운" 개념의 지속적이고 불필요한 혼란때문에, 미래에 가장 우선되어야할 목표는 가능한 범위 내에서 분류 체계를 완전하게 유지하는 것과 동시에 우리의 능력이 허락하는 한에서 단순하고 구조화시키는 것이 중요하다. 🔒

<br/>

### Index of Definitions

```
Accidental fault 3.2.1
Accountability 4.3
Active fault 2.2
Adaptive maintenance 3.1
Atomic 2.1
Augmentive maintenance 3.1
Authenticity 4.3
Autonomic computing 4.3
Availability 2.3
Back-to-back testing 5.3.1
Backward recovery 5.2.1
Behavior 2.1
Byzantine failure 3.3.1
Catastrophic failure 3.3.1
Commission fault 3.2.3
Common-mode failure 3.5
Compensation 5.2.1
Component 2.1
Computer-based systems 2
Concurrent detection 5.2.1
Confidentiality 2.3
Configuration fault 3.2.3
Consistency 3.3.1
Consistent failure 3.3.1
Content failure 3.3.1
Correct service 2.2
Corrective maintenance 3.1
Coverage 5.5
Degraded mode 2.2
Deliberate fault 3.2.1
Denial of service 3.2.4
Dependability & security analysis 5.5
Dependability & security benchmark 5.4
Dependability & security failure 3.3.3
Dependability & security provision 5.5
Dependability & security specification 2.3
Dependability 2.3
Dependence 2.3
Design diversity 5.2.2
Design for testability 5.3.1
Design for verifiability 5.3.1 
Detectability 3.3.1
Detected error 3.4
Detection and recovery 5.2.1
Deterministic testing 5.3.1
Development environment 3.1
Development failure 3.3.2
Development fault 3.2.1
Development phase 3.1
Diagnosis 5.2.1	
Dormant fault 2.2	
Downgrading 3.3.2	
Dynamic verification 5.3.1
Early timing failure 3.3.1
Elusive fault 3.5
Environment 2.1
Erratic failure 3.3.1
Error 2.2 
Error detection and system recovery 5.2.1
Error handling 5.2.1
External fault 3.2.1
External state 2.1
Fail-controlled system 3.3.1
Fail-halt system 3.3.1
Fail-passive system 3.3.1
Fail-safe system 3.3.1
Fail-silent system 3.3.1
Fail-stop system 3.3.1
Failure 2.2 
Failure domain 3.3.1
Failure severity 2.2
False alarm 3.3.1
Fault 2.2
Fault acceptance 5.5
Fault activation 3.5
Fault activation reproducibility 3.5
Fault avoidance 5.5
Fault forecasting 2.4	
Fault handling 5.2.1
Fault injection 5.3.1
Fault masking 5.2.1	
Fault prevention 2.4
Fault removal 2.4	
Fault tolerance 2.4	
Forward recovery 5.2.1
Function 2.1	
Functional specification 2.1
Functional testing 5.3.1
Golden unit 5.3.1	
Halt 3.3.1		
Halt failure 3.3.1
Hard fault 3.5
Hardware fault 3.2.1
High Confidence 4.4 
Human-made fault 3.2.1
Incompetence fault 3.2.1
Inconsistent failure 3.3.1
Independent faults 3.5
Integrity 2.3	
Interaction fault 3.2.1
Intermittent fault 3.5
Internal fault 3.2.1	
Internal state 2.1	
Intrusion attempt 3.2.4
Isolation 5.2.1	
Late timing failure 3.3.1
Latent error 3.4
Logic bomb 3.2.4
Maintainability 2.3
Maintenance 3.1	
Malicious fault 3.2.1 
Malicious logic fault 3.2.4
Masking 5.2.1 
Masking and recovery 5.2.1
Minor failure 3.3.1
Multiple faults 3.5	
Multiple related errors 3.4
Mutation testing 5.3.1
Natural fault 3.2.1	
Nondeliberate fault 3.2.1
Nonmalicious fault 3.2.1
Nonregression verification 5.3.1
Nonrepudiability 4.3 
Omission 3.2.3
Omission fault 3.2.3
Operational fault 3.2.1 
Operational testing 5.4
Oracle problem 5.3.1
Ordinal evaluation 5.4
Overrun 3.3.2
Partial development failure 3.3.2
Partial failure 2.2
Penetration testing 5.3.1
Performability 5.4
Permanent fault 3.2.1
Physical fault 3.2.1
Preemptive detection 5.2.1
Preventive maintenance 3.1
Probabilistic evaluation 5.4
Provider 2.1 
Qualitative evaluation 5.4
Quantitative evaluation 5.4
Random testing 5.3.1
Reconfiguration 5.2.1
Reconfiguration fault 3.2.3
Recovery-oriented computing 5.2.2
Reinitialization 5.2.1
Related faults 3.5 
Reliability 2.3  Resilience 5.2.2
Robustness 4.3
Rollback 5.2.1
Rollforward 5.2.1
Safety 2.3 
Security 2.3, 4.3
Security policy 4.3
Self-checking component 5.2.2
Self-healing 5.2.2
Self-repair 5.2.2
Service 2.1
Service delivery 3.1
Service failure 2.2 
Service failure mode 2.2
Service interface 2.1
Service outage 2.2
Service restoration 2.2
Service shutdown 3.1
Signaled failure 3.3.1
Silence 3.3.1 
Silent failure 3.3.1
Single error 3.4
Single fault 3.5
Soft error 3.5
Soft fault 3.5  
Software ageing 3.2.3
Software fault 3.2.1
Software rejuvenation 5.2.1
Solid fault 3.5
Static verification 5.3.1
Statistical testing 5.3.1
Structural testing 5.3.1
Structure 2.1
Survivability 4.4
Symbolic execution 5.3.1
System 2.1
System boundary 2.1 
System life cycle 3.1
System recovery 5.2.1
Testing 5.3.1 
Timing failure 3.3.1
Total state 2.1 
Transient fault 3.2.1
Transition 2.2
Trapdoor 3.2.4
Trojan horse 3.2.4
Trust 2.3
Trustworthiness 4.4
Unsignaled failure 3.3.1
Use environment 3.1
Use interface 2.1
Use phase 3.1
User 2.1
Validation 5.3.1
Verification 5.3.1
Virus 3.2.4
Vulnerability 2.2
Worm 3.2.4
Zombie 3.2.4
```


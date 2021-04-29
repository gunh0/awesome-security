# Ransomware

> Ransomware is a type of malware that denies access to user files, sometimes encrypting the entire hard drive and even all the attached external hard drives and network shares, after which it demands a ransom from the user to regain access to the system and stored information.

<br/>

## Table of Contents

-   Ransomware Types
    -   Locker Ransomware
    -   Crypto Ransomware
    -   Differences Between Ransomware and Other Malware Types
-   Ransomware Symptoms
-   Primary Targets of Ransomware Attacks
-   Ransomware Families (The Most Prominent Ransomware Strains)

<br/>

---

<br/>

### Ransomware Types

There are mainly two types of ransomware: `crypto` and `locker` ransomware.
However, ransomware belongs to the digital extortion category of cybercrime, which also contains other types of cyber crimes that aim to illicitly acquire or deny access to personal data in exchange for a monetary gain.

<br/>

#### Locker Ransomware

Locker ransomware works by preventing the victim from reaching their personal files through denying access to computing resources (e.g., locking the desktop or preventing the victim from logging in) and then demanding a ransom to regain access.
Compared with crypto ransomware, typical locker ransomware types deny access to personal files using relatively simple techniques that can be overcome by any technical user; as a result, locker ransomware can be removed from the infected systems without affecting the underlying operating system and personal files.

<br/>

#### Crypto Ransomware

This type of ransomware encrypts all personal data on the target machine, taking it hostage until the victim pays the ransom and obtains the decryption key from the attacker.

Some variants of crypto ransomware will progressively delete hostage files or release them to the public if the victim fails to pay the ransom on time. Modern ransomware families are mainly based on this type.

It can have devastating effects, especially on corporate and government agencies, if no backup exists to restore operation to the state before the ransomware attack.

In such cases, the victim entity has only one choice to recover the lost data, which is to pay the ransom.

After the crypto ransomware installs on the target system, it will silently search for important files (based on their extensions) and begin encrypting them; the ransomware will search for files on the local hard drive and all the attached external drives/network shares.

After successfully encrypting all the computer files, the ransomware will present the user with a ransom note, showing a countdown timer and asking for payment (ransom) to regain access to hostage files.

Modern crypto ransomware requests payment mostly via the Bitcoin cryptocurrency.

The majority of crypto ransomware infections will not damage the victim’s operating system files and will leave it functional so the user can perform some basic functions, without the ability to access hostage data that has been encrypted.

<br/>

#### Differences Between Ransomware and Other Malware Types

> Ransomware is a subtype of malware; however, there are many distinct characteristics that distinguish it from other malware types.

-   Some malware types aim to steal user confidential information (e.g., usernames, passwords, keystrokes, and personal files) or to provide outsider access to the victim machine. More malicious malware types will bring damage (e.g., deleting files, changing system configurations, or reformatting and corrupting the underlying OS files) to the infected OS files, making it inoperable. Ransomware, on the other hand, encrypts victim machine files and announces its presence with a ransom note. The ultimate purpose of ransomware is to extort money from its victims without damaging the underlying OS or stored data.
-   Ransomware does not require administrative privileges to encrypt files on the victim machine. Unlike other malware, which mostly requires admin access on the target machine, ransomware depends on the current permission assigned to the victim machine within the organization to encrypt all personal files, whether it is stored locally or on a network share, that this victim has access to.
-   Encryption ransomware has the ability to encrypt all file types, in addition to its ability to scramble file names, making victims unaware of the actual number of files encrypted.
-   Ransomware requests payments via anonymous payment methods, typically Bitcoin.
-   Ransomware uses different evasion techniques to surpass security solutions like antivirus software and firewalls.
-   Some ransomware types connect the victim machine to other networks of botnets to use it as a weapon in other cyberattacks.
-   Ransomware can propagate across internal networks and through the Internet.
-   Ransomware can steal sensitive information from the victim’s machine and send it to its operators for blackmail purposes.
-   Sophisticated ransomware is location-aware, meaning that it targets victims according to their geographical area and presents ransom
    notes using the target area’s language.

<br/>

### Ransomware Symptoms

It is relatively easy to find out if you are affected by ransomware. The symptoms include the following:

-   You cannot open your files; you always receive an error message that the file you are trying to access has the wrong extension (e.g.,
    Windows asks you “How do you want to open this file?”) or it is corrupted.

-   The ransomware may change your desktop wallpaper and replace it with a ransom note.
-   Your computer is locked, and you cannot access your desktop. A splash screen displaying the ransom note appears instead and covers the whole screen asking you to pay a ransom within a limited time frame; otherwise, your data will get lost forever.
-   A ransom note may appear in a form of a program window that does not cover the whole screen, and the user cannot close it. A countdown timer is available within this window to alert the user about the remaining time before increasing the ransom or losing the data if the user fails to pay the ransom.
-   You see instruction files in all directories that contain files encrypted by the ransomware; these files have different formats such as TXT, PNG, and HTML and the name is written in capital letters (e.g., YOUR_FILES_ARE_ENCRYPTED.HTML and YOUR_FILES_ARE_ENCRYPTED.TXT).
-   Your stored file names are scrambled and have a different extension or no extension at all.

<br/>

### Primary Targets of Ransomware Attacks

Before 2015, the majority of ransomware victims were individuals; however, in 2015, ransomware operators shifted their attention to target enterprises and academic organizations to acquire more guaranteed money from their attacks.
In these cases, Microsoft Office and database files were the primary targets.
Enterprises are a big target of ransomware; however, anyone is subject to being a victim of such attacks such as celebrities, politicians, individuals, public and private organizations, and even charity and nonprofit organizations.
Ransomware campaigns are sent in bulk (for example, sending spam e-mails with a link to download the ransomware) to infect as many devices as possible.
In 2016, the healthcare industry became a top target of ransomware attacks for many reasons.
The rapid adoption of IT technology in hospitals and healthcare centers was not accompanied the necessary IT security training to combat potential cyberattacks;
in addition, the health sector is particularly sensitive to any disruption of service, which makes the healthcare industry attractive to ransomware attacks.
Ransomware infects almost all IT devices types including servers, mobile devices, and many types of IoT devices in addition to storage devices attached to victim machines such as USB sticks, SD cards, digital cameras, and external hard drives.
Most ransomware campaigns target Windows OS and Android devices because the global market share for OSs is dominated by these two operating systems, according to recent statistics published by StatCounter in January 2019.
However, this does not mean that cybercriminals do not target other device types.
According to Datto’s report “Global State of the Channel Ransomware Report 2018”, ransomware attacks on Apple OS and iOS have increased about 500 percent compared to 2017.
Legacy systems, especially industrial and healthcare equipment, that’s still in operation and cannot receive further updates (patches) are also predicted to become a top target of ransomware attacks in the future.
To conclude, the crucial factor in determining the best target of ransomware is not the type of business or the work nature of an individual.
Successful ransomware attacks rely on the type of technologies used by the victim, the level of IT knowledge, vulnerabilities existing on the victim’s computing devices and connected networks, and outdated operating systems and applications that cannot receive further updates from the manufacturer, in addition to the overall cybersecurity strategy implemented by the organization.

<br/>

### Ransomware Families (The Most Prominent Ransomware Strains)

Ransomware can be classified into groups using different criteria, for example, according to its function such as whether it is a locker or encryption ransomware.
Security experts prefer to classify ransomware into families according to its code signature, which contains the sequence of commands and instructions responsible for the malicious action.

# Return-to-libc Attack

## Overview

This Python script, named `exploit.py`, is developed for educational purposes to execute a return-to-libc attack on a vulnerable program. The attack utilizes a buffer-overflow vulnerability, redirecting program execution to existing code like the `system()` and `exit()` functions within the libc library. The provided script generates a malicious file named "badfile" containing the required addresses for the attack. Before running the script, users must replace placeholder addresses with the actual addresses from the target system's libc.

## Script Details

### Addresses

-   **sh_addr:** Actual address for "/bin/sh"
-   **system_addr:** Actual address for the `system()` function
-   **exit_addr:** Actual address for the `exit()` function

### File Structure

The script fills a 300-byte bytearray with non-zero values (0xAA) and replaces sections with specified addresses in little-endian format:

-   Bytes 0-7: "/bin/sh" address
-   Bytes 8-15: `system()` function address
-   Bytes 16-23: `exit()` function address

The generated "badfile" is saved in the "/app/" directory.

## Usage

1. Replace placeholder addresses with actual addresses from the target system's libc.
2. Execute the script in a Python 3 environment:

```bash
./exploit.py
```

3. Check the generated "badfile" in the "/app/" directory.

## Disclaimer

This script is provided for educational purposes only. It demonstrates a simulated attack scenario and should not be used for any malicious activities. Users are responsible for ensuring the legality and ethical use of the provided materials.

<!-- Please prefix the notes with the date as in [22/12/2020] -->

[01/06/2022]

**Trusted Execution Environments (TEE)** are an increasingly popular solution to the problem of protecting sensitive computations and data against co-located attackers. While they differ in their implementation, they aim to provide **four high level security protections**:

1. ***Verifiable launch of the execution environment*** for the sensitive code and data so that a remote entity can ensure it was set up correctly.
2. ***Run-time isolation*** to protect the confidentiality and integrity of sensitive code and data.
3. ***Trusted IO*** to enable secure access to peripherals and accelerators.
4. ***Secure storage for TEE data*** that must be stored persistently and made available only to authorized entities at a later point in time.

A comparison of the solutions considering those four points is presented. Its methodology consists of different characteristics for each point:

(1) refers to the proof regarding the correctness of the initial state of the TEE. It establishes a *Root of Trust for Measurement (RTM)*, uses it to measure the state of the code/data within the TEE and makes it available for verification.

(2) is qualified using two dimensions, *resource partitioning* and *isolation enforcement*. Those dimensions are used to discuss their resource advantages and suitability for isolating CPU and memory against different adversaries. The corresponding components are then compared.

(3) involves two components: a *trusted path to the device* and a *trusted device architecture to protect security sensitive data just like the CPU*. The trusted paths are either *logical* or *cryptographic* and the same taxonomy as (2) is used to qualify the trusted device architecture.

(4) ensures that any sensitive data that is persistent is only available

 ##### tags: hardware, security, sok, tee
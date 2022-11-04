<!-- Please prefix the notes with the date as in [22/12/2020] -->

**ASIST** extension is able to protect both user- and kernel-level processes transparently without any program modifications. It utilizes a combination of techniques to increase security and performance. It uses highly secure cryptographic algorithms that can provide resilience against several attacks. It takes advantage of efficient caching strategies, as well as the spatial locality of the code to decrease the execution overheads. This way, the number of decrypt operations needed decreases and the overall performance is improved. It adds less than 1.5% overhead for XOR or transposition and around 10% for AES.

##### tags: defense, isr, security
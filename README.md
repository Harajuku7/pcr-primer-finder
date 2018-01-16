# pcr-primer-finder
A command-line tool that find optimized PCR-primer for a given fasta file region.

### Functionalities
Results of this tool follows somes rules:
* 17 to 25 nucleotids-long primer
* Primer has to end with a C or G
* Both primer has to have the same hybridation temps  

To be implemented:
* addition of restriction sites 
* addition of promotor

### How to use
```bash
python main.py -f filename.fasta -b [begining of region interest] -e [end of region of interest]
```
Example:
```bash
python main.py -f test.fasta -b 10 -e 200
```
(python3)

### Screenshot (with test.fasta)
![Screenshot of the Application](https://i.imgur.com/Wxf2Zfe.png)

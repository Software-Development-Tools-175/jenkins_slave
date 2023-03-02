```
python myscript.py args.csv

```

### Explaination

```
1. After trigger by commit, master pipeline call parsingCSV.py to test if CSV is usable then call Slave pipeline with argument CSV path

2. Slave pipeline call args.csv to myscript.py then run function inside
```

#### Video: [master-slave testing video](https://drive.google.com/file/d/1eVcvVKcjYDhDURZCD3VAaWwa1uGUyXw3/view?usp=sharing)

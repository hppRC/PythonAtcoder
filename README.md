# Python AtCoder


```bash
acc config default-template python
acc config default-test-dirname-format test
mkdir -p  (acc config-dir)/python
mkdir -p  (acc config-dir)/pypy
cp ./main.py (acc config-dir)/python
cp ./template.json (acc config-dir)/python
cp ./main.py (acc config-dir)/pypy
cp ./template.json (acc config-dir)/pypy
```


```bash
oj login https://atcoder.jp/
oj login https://beta.atcoder.jp/
```


## test

```
cd task_dir
acct
```

## submit

```
acc s
```
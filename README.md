# Taiwan_e_hospital_fetcher

> **Warning**
> Education purpose only

## Introduction

An script can crawler web data from Internet, the raw data will be html files, need processing before using it.

It's based on [台灣e院](https://sp1.hso.mohw.gov.tw/doctor/)

```text
Example: https://sp1.hso.mohw.gov.tw/doctor/All/ShowDetail.php?q_no=$page
```

# How to use

Linux:
```bash
./fetch.sh
# or
start_page=1
./fetch.sh $start_page
```

![Result](./screenshot/result.png)

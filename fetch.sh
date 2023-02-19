#!/bin/bash

lower_bound=2500
base_dir='./raw_data'
function generate {
  page=$1
  echo "https://sp1.hso.mohw.gov.tw/doctor/All/ShowDetail.php?q_no=$page"
}

function fetch {
  index=$1
  steps=$2
  limit=$3
  while true
  do
    url=$(generate $index)
    save="$base_dir/$index"
    echo Fetch $index...
    result="$(curl $url -s)"
    echo "$result" > $save
    length=$(echo "$result" | grep -o '[0-9a-zA-Z]' | wc -l)
    hashs=$(echo $result | md5sum)
    echo $index $hashs $length, Done.
    let "index = index + steps"
    if [[ $index -gt $limit ]];then
      break
    fi
  done
}

start=$1
if [ -z "$1" ]; then
  start=1
fi

# fetch $start $increase_every_req $the_last_page
fetch $start 1 1 # 80193 # 23/02/19

